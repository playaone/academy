from app.exceptions import AuthenticationError
from app.repositories.user_repository import UserRepository
from app.security.passwords import verify_password


class AuthenticationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)

        if user is None:
            raise AuthenticationError("Invalid email or password.")

        if not verify_password(user.password_hash, password):
            raise AuthenticationError("Invalid email or password.")

        if not user.is_active:
            raise AuthenticationError("Invalid email or password")

        return user
