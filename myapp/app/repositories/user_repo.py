from sqlalchemy.orm import Session
from ..models.user import User


def get_by_id(db: Session, user_id: int) -> User | None:
    """Get a user by ID."""
    return db.query(User).filter(User.id == user_id).first()


def get_by_email(db: Session, email: str) -> User | None:
    """Get a user by email."""
    return db.query(User).filter(User.email == email).first()


def create(db: Session, username: str, email: str, hashed_password: str) -> User:
    """Create a new user."""
    user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user