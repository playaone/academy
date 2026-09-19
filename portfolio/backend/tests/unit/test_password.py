from app.security.passwords import hash_password, verify_password


def test_hash_password():
    password = "my-secret-password"

    password_hash = hash_password(password)

    assert password_hash != password


def test_verify_password():
    hashed_password = hash_password("my-password")

    assert verify_password(password_hash=hashed_password, password="my-password")


def test_wrong_password():
    hash = hash_password("my-password")

    assert not verify_password(password_hash=hash, password="wrong-password")
