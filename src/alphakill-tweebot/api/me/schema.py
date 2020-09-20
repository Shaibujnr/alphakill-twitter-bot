from uuid import UUID
from alphakill-tweebot.database.models import UserRole
from ..schema import BaseSchema, OrmSchema


class ProfileSchema(OrmSchema):
    first_name: str
    last_name: str
    username: str
    email: str
    phone_number: str
    role: UserRole
    is_active: bool
