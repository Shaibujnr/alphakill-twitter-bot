from alphakill-tweebot.database.models import User
from tests.conftest import existing_user, new_user_data
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


def test_fetch_profile_ok(
    client: TestClient, existing_user: User, user_auth_header: dict
):
    response = client.get(f"/api/me/", headers=user_auth_header)
    result = response.json()
    assert response.status_code == 200
    assert "firstName" in result
    assert "lastName" in result
    assert "email" in result
    assert "username" in result
    assert "id" in result
    assert "phoneNumber" in result


def test_fetch_profile_without_token_fail(client: TestClient, existing_user: User):
    response = client.get(f"/api/me/")
    assert response.status_code == 401
