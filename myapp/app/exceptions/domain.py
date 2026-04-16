class DomainError(Exception):
    """Base class for domain exceptions."""
    pass


class UserAlreadyExistsError(DomainError):
    """Raised when trying to register a user that already exists."""
    pass


class InvalidCredentialsError(DomainError):
    """Raised when authentication fails."""
    pass


class InsufficientStockError(DomainError):
    """Raised when trying to purchase more items than are in stock."""
    pass


class ProductNotFoundError(DomainError):
    """Raised when a product could not be found."""
    pass


class EmptyCartError(DomainError):
    """Raised when trying to checkout with an empty cart."""
    pass