class DomainError(Exception):
    """Base class for domain exceptions."""
    pass


class UserAlreadyExistsError(DomainError):
    """Raised when trying to register a user that already exists."""
    pass


class InvalidCredentialsError(DomainError):
    """Raised when authentication fails."""
    pass