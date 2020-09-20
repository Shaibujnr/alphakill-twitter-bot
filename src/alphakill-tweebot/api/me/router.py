from fastapi import APIRouter, Depends
from alphakill-tweebot.database.models import User
from .schema import ProfileSchema
import alphakill-tweebot.api.dependencies as dependencies


router = APIRouter()


@router.get("/", response_model=ProfileSchema)
async def me(user: User = Depends(dependencies.get_current_user)):
    return user
