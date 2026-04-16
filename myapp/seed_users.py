from app.db.session import SessionLocal
from app.models.user import User
from app.utils.hashing import hash_password

def seed():
    db = SessionLocal()
    try:
        # Check if already seeded
        if db.query(User).first():
            print("Database already seeded with users.")
            return

        users = [
            User(
                username="admin",
                email="admin@example.com",
                hashed_password=hash_password("admin123")
            ),
            User(
                username="testuser",
                email="test@example.com",
                hashed_password=hash_password("password123")
            )
        ]

        db.add_all(users)
        db.commit()
        print(f"Successfully seeded {len(users)} users.")
    except Exception as e:
        print(f"Error seeding users: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
