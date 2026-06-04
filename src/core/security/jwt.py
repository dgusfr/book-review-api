import logging
import uuid
from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import Request
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from itsdangerous import URLSafeTimedSerializer

from src.core.config import Config
from src.core.exceptions import AccessTokenRequired, InvalidToken, RefreshTokenRequired
from src.core.redis import token_in_blocklist

ACCESS_TOKEN_EXPIRY = 3600


def create_access_token(
    user_data: dict,
    expiry: Optional[timedelta] = None,
    refresh: bool = False,
) -> str:
    payload = {
        "user": user_data,
        "exp": datetime.now()
        + (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY)),
        "jti": str(uuid.uuid4()),
        "refresh": refresh,
    }

    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET,
        algorithm=Config.JWT_ALGORITHM,
    )

    return token


def decode_token(token: str) -> Optional[dict]:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=Config.JWT_SECRET,
            algorithms=[Config.JWT_ALGORITHM],
        )
        return token_data
    except jwt.PyJWTError as exc:
        logging.exception(exc)
        return None


serializer = URLSafeTimedSerializer(
    secret_key=Config.JWT_SECRET,
    salt="email-configuration",
)


def create_url_safe_token(data: dict) -> str:
    token = serializer.dumps(data)
    return token


def decode_url_safe_token(token: str) -> Optional[dict]:
    try:
        token_data = serializer.loads(token)
        return token_data
    except Exception as exc:
        logging.error(str(exc))
        return None


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> dict | None:
        credentials: HTTPAuthorizationCredentials | None = await super().__call__(
            request
        )

        if credentials is None:
            raise InvalidToken()

        token = credentials.credentials
        token_data = decode_token(token)

        if not self.token_valid(token):
            raise InvalidToken()

        if await token_in_blocklist(token_data["jti"]):
            raise InvalidToken()

        self.verify_token_data(token_data)

        return token_data

    def token_valid(self, token: str) -> bool:
        token_data = decode_token(token)
        return token_data is not None

    def verify_token_data(self, token_data: dict) -> None:
        raise NotImplementedError("Please override this method in child classes")


class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and token_data["refresh"]:
            raise AccessTokenRequired()


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and not token_data["refresh"]:
            raise RefreshTokenRequired()
