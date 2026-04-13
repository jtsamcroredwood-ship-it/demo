from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserLogin
from ..repositories import user_repo
from ..utils.hashing import hash_password, verify_password
from ..exceptions.domain import UserAlreadyExistsError, InvalidCredentialsError


def register(db: Session, user_data: UserCreate) -> dict:
    """Register a new user."""
    # Check if user already exists
    existing_user = user_repo.get_by_email(db, user_data.email)
    if existing_user:
        raise UserAlreadyExistsError("User with this email already exists")

    # Hash password and create user
    hashed_password = hash_password(user_data.password)
    user = user_repo.create(db, user_data.username, user_data.email, hashed_password)

    return {"message": "User registered successfully", "user_id": user.id}


def authenticate(db: Session, login_data: UserLogin) -> dict:
    """Authenticate a user."""
    user = user_repo.get_by_email(db, login_data.email)
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise InvalidCredentialsError("Invalid email or password")

    return {"user": user}