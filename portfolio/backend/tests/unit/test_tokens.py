import uuid
from datetime import datetime, timedelta, timezone

import jwt

from app.security.tokens import create_access_token, decode_access_token


def test_create_access_token(app):
    user_id = str(uuid.uuid4())

    token = create_access_token(user_id=user_id)

    assert token is not None

    assert isinstance(token, str)

    assert token != ""


def test_decode_access_token(app):
    user_id = str(uuid.uuid4())

    token = create_access_token(user_id=user_id)

    assert isinstance(token, str)
    assert token != ""

    payload = decode_access_token(token=token)

    assert payload is not None

    assert isinstance(payload, dict)

    assert payload["sub"] == user_id


def test_decode_expired_access_token(app):
    user_id = str(uuid.uuid4())

    payload = {
        "sub": user_id,
        "iat": datetime.now(timezone.utc) - timedelta(hours=2),
        "exp": datetime.now(timezone.utc) - timedelta(hours=1),
    }

    token = jwt.encode(
        payload=payload,
        key=app.config["JWT_SECRET_KEY"],
        algorithm=app.config["JWT_ALGORITHM"],
    )

    result = decode_access_token(token)

    assert result is False


def test_decode_tampered_access_token(app):
    user_id = str(uuid.uuid4())

    token = create_access_token(user_id)

    parts = token.split(".")

    tampered_payload = parts[1][:-1] + ("A" if parts[1][-1] != "A" else "B")

    tampered_token = ".".join([parts[0], tampered_payload, parts[2]])

    result = decode_access_token(tampered_token)

    assert result is False
