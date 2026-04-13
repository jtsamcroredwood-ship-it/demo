# Seed script for inserting test products into the database
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.product import Product
from datetime import datetime

def seed_products():
    db: Session = SessionLocal()
    products = [
        Product(
            name="Wireless Mouse",
            description="A smooth and responsive wireless mouse.",
            price=19.99,
            stock=50,
            image_url="/static/img/mouse.jpg",
            created_at=datetime.utcnow(),
        ),
        Product(
            name="Mechanical Keyboard",
            description="A tactile mechanical keyboard with RGB lighting.",
            price=89.99,
            stock=30,
            image_url="/static/img/keyboard.jpg",
            created_at=datetime.utcnow(),
        ),
        Product(
            name="HD Monitor",
            description="24-inch Full HD monitor with vibrant colors.",
            price=149.99,
            stock=20,
            image_url="/static/img/monitor.jpg",
            created_at=datetime.utcnow(),
        ),
    ]
    for product in products:
        db.add(product)
    db.commit()
    db.close()
    print("Seeded test products.")

if __name__ == "__main__":
    seed_products()
