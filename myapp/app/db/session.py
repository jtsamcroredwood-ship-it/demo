from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config import settings
# Import all models to ensure they're registered with SQLAlchemy
from ..models import Base, User, Product, Order, OrderItem

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)