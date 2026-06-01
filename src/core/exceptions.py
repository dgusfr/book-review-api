class BooklyException(Exception):
    """Base class for all Bookly application exceptions."""


class InvalidToken(BooklyException):
    """User has provided an invalid or expired token."""


class RevokedToken(BooklyException):
    """User has provided a token that has been revoked."""


class AccessTokenRequired(BooklyException):
    """User has provided a refresh token when an access token is needed."""


class RefreshTokenRequired(BooklyException):
    """User has provided an access token when a refresh token is needed."""


class UserAlreadyExists(BooklyException):
    """User has provided an email for a user who already exists."""


class InvalidCredentials(BooklyException):
    """User has provided wrong email or password during login."""


class InsufficientPermission(BooklyException):
    """User does not have the necessary permissions to perform an action."""


class BookNotFound(BooklyException):
    """Book not found."""


class TagNotFound(BooklyException):
    """Tag not found."""


class TagAlreadyExists(BooklyException):
    """Tag already exists."""


class UserNotFound(BooklyException):
    """User not found."""


class AccountNotVerified(BooklyException):
    """Account not yet verified."""
