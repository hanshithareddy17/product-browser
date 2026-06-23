import base64
from datetime import datetime


SEPARATOR = "|"


def encode_cursor(created_at: datetime, product_id: int) -> str:
    """
    Encode cursor as:
    created_at|id
    then Base64 encode it.
    """

    raw = f"{created_at.isoformat()}{SEPARATOR}{product_id}"

    return base64.urlsafe_b64encode(
        raw.encode("utf-8")
    ).decode("utf-8")


def decode_cursor(cursor: str):

    decoded = base64.urlsafe_b64decode(
        cursor.encode("utf-8")
    ).decode("utf-8")

    created_at, product_id = decoded.split(SEPARATOR)

    return (
        datetime.fromisoformat(created_at),
        int(product_id),
    )