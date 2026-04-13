from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session
from .db import get_db
from ..repositories.user_repo import get_by_id
from ..models.user import User


def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    """Get the current authenticated user from session."""
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user