from types import SimpleNamespace

import pytest

from app.exceptions import AuthenticationError
from app.security.passwords import hash_password
from app.services.authentication_service import AuthenticationService

dummy = {"email": "my_test@email.com", "password": "easypassword!", "is_active": True}

inactive_dummy = {
    "email": "my_inactive@email.com",
    "password": "inactivepassword!2",
    "is_active": False,
}


class FakeUserRepository:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def create_user(self, email: str, password: str, is_active: bool):

        password_hash = hash_password(password)

        user = SimpleNamespace(
            email=email,
            password_hash=password_hash,
            id=self.next_id,
            is_active=is_active,
        )

        self.users[user.id] = user
        self.next_id += 1

        return user

    def get_by_email(self, email: str):
        for user in self.users.values():
            if user.email == email:
                return user

        return None


@pytest.fixture
def repository():
    repo = FakeUserRepository()

    repo.create_user(
        email=dummy["email"], password=dummy["password"], is_active=dummy["is_active"]
    )
    repo.create_user(
        email=inactive_dummy["email"],
        password=inactive_dummy["password"],
        is_active=inactive_dummy["is_active"],
    )

    return repo


@pytest.fixture
def service(repository):
    return AuthenticationService(repository)


# Valid credentials
def test_valid_user_credentials(service):
    user = service.authenticate(email=dummy["email"], password=dummy["password"])

    assert user is not None


# Unknown email
def test_unknown_user_email(service):
    with pytest.raises(AuthenticationError):
        service.authenticate(email="messy_email", password=dummy["password"])


# Wrong password
def test_wrong_user_password(service):
    with pytest.raises(AuthenticationError):
        service.authenticate(email=dummy["email"], password="myfakepassword")


# Inactive user
def test_inactive_user_raises_authentication_error(service):
    with pytest.raises(AuthenticationError):
        service.authenticate(
            email=inactive_dummy["email"], password=inactive_dummy["password"]
        )


# Do not leak credential information
def test_user_model_does_not_store_plain_text_password(service):
    user = service.authenticate(email=dummy["email"], password=dummy["password"])

    assert "password" not in vars(user).keys()

    assert user.password_hash != dummy["password"]
