from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.config import settings
from app.crud import get_categories, get_products
from app.dependencies import get_db
from app.schemas import ProductListResponse

router = APIRouter()


@router.get(
    "/products",
    response_model=ProductListResponse,
)
def list_products(
    limit: int = Query(
        settings.DEFAULT_PAGE_SIZE,
        ge=1,
        le=settings.MAX_PAGE_SIZE,
    ),
    cursor: str | None = None,
    category: str | None = None,
    db: Session = Depends(get_db),
):
    return get_products(
        db=db,
        limit=limit,
        cursor=cursor,
        category=category,
    )


@router.get("/categories")
def list_categories(
    db: Session = Depends(get_db),
):
    return get_categories(db)