from fastapi import Request

def get_cart_from_session(request: Request) -> dict[str, int]:
    """Retrieve the cart from the session. It's a dict mapping product_id (as str) to quantity."""
    return request.session.get("cart", {})

def save_cart_to_session(request: Request, cart: dict[str, int]) -> None:
    """Save the cart back into the session."""
    request.session["cart"] = cart
