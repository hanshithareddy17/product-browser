from datetime import timedelta
import random

from faker import Faker
from sqlalchemy import text

from app.database import SessionLocal
from app.models import Product

fake = Faker()

TOTAL_PRODUCTS = 200000
BATCH_SIZE = 1000

CATEGORIES = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home",
    "Beauty",
    "Toys",
    "Grocery",
]


def generate_products(batch_size: int):

    products = []

    for _ in range(batch_size):

        created_at = fake.date_time_between(
            start_date="-2y",
            end_date="now",
        )

        updated_at = created_at + timedelta(
            days=random.randint(0, 100)
        )

        products.append(
            Product(
                name=fake.sentence(nb_words=3).rstrip("."),
                category=random.choice(CATEGORIES),
                price=round(
                    random.uniform(100, 100000),
                    2,
                ),
                created_at=created_at,
                updated_at=updated_at,
            )
        )

    return products


def seed():

    db = SessionLocal()

    try:

        print("Deleting existing products...")

        db.execute(text("TRUNCATE TABLE products RESTART IDENTITY"))

        db.commit()

        print("Generating products...")

        inserted = 0

        while inserted < TOTAL_PRODUCTS:

            products = generate_products(BATCH_SIZE)

            db.bulk_save_objects(products)

            db.commit()

            inserted += BATCH_SIZE

            print(
                f"Inserted {inserted}/{TOTAL_PRODUCTS}"
            )

        print("\nDatabase seeded successfully!")

    finally:

        db.close()


if __name__ == "__main__":
    seed()