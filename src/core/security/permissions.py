from typing import Any, List

from fastapi import Depends

from src.core.dependencies import get_current_user
from src.core.exceptions import AccountNotVerified, InsufficientPermission
from src.models.user_model import User


class RoleChecker:
    def __init__(self, allowed_roles: List[str]) -> None:
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: User = Depends(get_current_user)) -> Any:
        if not current_user.is_verified:
            raise AccountNotVerified()

        if current_user.role in self.allowed_roles:
            return True

        raise InsufficientPermission()
