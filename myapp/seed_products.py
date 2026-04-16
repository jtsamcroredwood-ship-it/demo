from app.db.session import SessionLocal
from app.models.product import Product
from decimal import Decimal

def seed():
    db = SessionLocal()
    try:
        # Check if already seeded
        if db.query(Product).first():
            print("Database already seeded with products.")
            return

        products = [
            Product(
                name="Smartphone Alpha",
                description="A high-end smartphone with a stunning display and powerful processor.",
                price=Decimal("799.99"),
                stock=50,
                image_url="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
            ),
            Product(
                name="Laptop Pro 16",
                description="The ultimate laptop for creators and professionals.",
                price=Decimal("2499.00"),
                stock=25,
                image_url="https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
            ),
            Product(
                name="Wireless Headphones",
                description="Experience crystal clear sound with active noise cancellation.",
                price=Decimal("299.50"),
                stock=100,
                image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
            ),
            Product(
                name="Smart Watch S",
                description="Track your fitness and stay connected on the go.",
                price=Decimal("199.00"),
                stock=75,
                image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30"
            ),
            Product(
                name="Gaming Mouse G-Pro",
                description="Lightning-fast response time for competitive gaming.",
                price=Decimal("89.99"),
                stock=150,
                image_url="https://images.unsplash.com/photo-1527814050087-3793815479db"
            )
        ]

        db.add_all(products)
        db.commit()
        print(f"Successfully seeded {len(products)} products.")
    except Exception as e:
        print(f"Error seeding products: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
