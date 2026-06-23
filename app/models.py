from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Index,
    Integer,
    String,
)

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = Column(
        String(255),
        nullable=False,
    )

    category = Column(
        String(100),
        nullable=False,
    )

    price = Column(
        Float,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    __table_args__ = (
        # Used for newest-first keyset pagination
        Index(
            "idx_products_created_id",
            created_at.desc(),
            id.desc(),
        ),

        # Used when filtering by category
        Index(
            "idx_products_category_created_id",
            category,
            created_at.desc(),
            id.desc(),
        ),
    )