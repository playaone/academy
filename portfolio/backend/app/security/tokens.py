from datetime import datetime, timedelta, timezone

import jwt
from flask import current_app


def create_access_token(user_id: str):

    jwt_secret = current_app.config.get("JWT_SECRET_KEY")
    jwt_algorithm = current_app.config.get("JWT_ALGORITHM")

    payload = {
        "sub": user_id,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    }

    return jwt.encode(payload=payload, key=jwt_secret, algorithm=jwt_algorithm)


def decode_access_token(token: str):

    jwt_secret = current_app.config.get("JWT_SECRET_KEY")
    jwt_algorithm = current_app.config.get("JWT_ALGORITHM")

    try:
        return jwt.decode(jwt=token, key=jwt_secret, algorithms=jwt_algorithm)
    except jwt.InvalidTokenError:
        return False
