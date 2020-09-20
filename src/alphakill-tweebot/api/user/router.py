from fastapi import APIRouter, Depends, HTTPException
from alphakill-tweebot.app.error import ApplicationError
from alphakill-tweebot.api.auth.schema import TokenSchema
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from alphakill-tweebot.app import Application
import alphakill-tweebot.api.dependencies as dependencies
from alphakill-tweebot.database.models import User
from .schema import UserCreateSchema, UserSchema

router = APIRouter()


@router.post("/", response_model=UserSchema)
async def register(
    data: UserCreateSchema,
    application: Application = Depends(dependencies.get_application),
    session: Session = Depends(dependencies.get_database_session),
):
    try:
        return application.create_user(session, **data.dict())
    except ApplicationError as e:
        raise HTTPException(401, str(e))
