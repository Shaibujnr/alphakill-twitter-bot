from alphakill-tweebot.core.services.auth import AuthService
from alphakill-tweebot.core.services.user import UserService


class ApplicationBase:
    def __init__(
        self,
        auth_service: AuthService,
        user_service: UserService
    ) -> None:
        self.auth_service = auth_service
        self.user_service: UserService = user_service
