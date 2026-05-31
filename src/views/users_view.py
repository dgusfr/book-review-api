from controllers.users import UsersController


class UsersView:
    """View layer for user-related operations."""

    def __init__(self):
        self.__users_controller = UsersController()

    async def handle_list_users(self, http_request) -> dict:
        """Handle the HTTP request for listing users."""
        response = await self.__users_controller.list_users()
        http_response = {"body": response, "status_code": 200}
        return http_response
