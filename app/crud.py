from datetime import datetime

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from app.models import Product
from app.utils import decode_cursor, encode_cursor


def get_products(
    db: Session,
    limit: int,
    cursor: str | None = None,
    category: str | None = None,
):
    query = db.query(Product)

    if category:
        query = query.filter(
            Product.category == category
        )

    if cursor:
        cursor_created_at, cursor_id = decode_cursor(cursor)

        query = query.filter(
            or_(
                Product.created_at < cursor_created_at,
                and_(
                    Product.created_at == cursor_created_at,
                    Product.id < cursor_id,
                ),
            )
        )

    query = query.order_by(
        Product.created_at.desc(),
        Product.id.desc(),
    )

    products = query.limit(limit + 1).all()

    next_cursor = None

    if len(products) > limit:
        last_product = products[limit - 1]

        next_cursor = encode_cursor(
            last_product.created_at,
            last_product.id,
        )

        products = products[:limit]

    return {
        "items": products,
        "next_cursor": next_cursor,
    }


def get_categories(db: Session):

    categories = (
        db.query(Product.category)
        .distinct()
        .order_by(Product.category)
        .all()
    )

    return [row[0] for row in categories]