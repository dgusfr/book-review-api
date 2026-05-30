from typing import List, Dict

from src.repos.users import get_all_users as repo_get_all


async def list_users() -> List[Dict]:
    """Business logic layer for listing users.

    Currently delegates to repository; place for future rules/validation.
    """
    rows = await repo_get_all()
    # Example transformation can be done here if needed
    return rows
