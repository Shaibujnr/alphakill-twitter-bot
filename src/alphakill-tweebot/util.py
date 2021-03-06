import jwt
from typing import Union
from datetime import datetime, timedelta
from alphakill-tweebot.core.config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, JWT_ALGORITHM


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)


def decode_access_token(token: Union[str, bytes]) -> str:
    # scenario token is not valid
    payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
    user_id: str = payload.get("sub")  # type: ignore
    return user_id
