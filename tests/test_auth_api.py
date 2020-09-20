from alphakill-tweebot.database.models import User
from tests.conftest import existing_user
import pytest
from uuid import UUID
from fastapi.testclient import TestClient
from alphakill-tweebot.api.user.schema import UserCreateSchema, UserSchema
from alphakill-tweebot.api.me.schema import ProfileSchema
from alphakill-tweebot.api.auth.schema import TokenSchema
from pytest_mock import MockFixture
from alphakill-tweebot.app import Application
from alphakill-tweebot.app.error import ApplicationError
from sqlalchemy.orm.session import Session


def test_user_auth_ok(client: TestClient, existing_user: User, new_user_data: dict):
    response = client.post(
        f"/api/auth/",
        data={
            "username": existing_user.email,
            "password": new_user_data["password"],
        },
    )
    result = response.json()
    assert response.status_code == 200
    assert "access_token" in result
    assert "token_type" in result


def test_user_auth_fail(client: TestClient, existing_user: User, new_user_data: dict):
    response = client.post(
        f"/api/auth/",
        data={
            "username": "wrong email",
            "password": "wrongpassword",
        },
    )
    result = response.json()
    assert response.status_code == 401
    assert "access_token" not in result
    assert "token_type" not in result
