# Product Browser API

A backend service built with FastAPI and PostgreSQL that efficiently browses 200,000+ products using cursor-based pagination.

## Features

- FastAPI
- PostgreSQL (Neon)
- SQLAlchemy ORM
- Cursor-based Pagination (Keyset Pagination)
- Category Filtering
- Batch Seed Script (200,000 Products)
- Swagger Documentation
- Optimized Database Indexes

---

## Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Faker

---

## Project Structure

```
product-browser/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── routes.py
│   └── utils.py
│
├── scripts/
│   └── seed.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Seed Database

```bash
python -m scripts.seed
```

Generates **200,000 products** using batch inserts.

---

## API Endpoints

### Home

```
GET /
```

### Products

```
GET /products
```

Query Parameters

| Parameter | Description |
|-----------|-------------|
| limit | Number of products |
| cursor | Cursor for next page |
| category | Filter by category |

Example

```
GET /products?limit=20
```

```
GET /products?category=Books
```

```
GET /products?cursor=<next_cursor>
```

---

## Why Cursor Pagination?

Offset pagination becomes slower on very large datasets because the database scans skipped rows.

Cursor pagination:

- O(log n) lookup
- No duplicate rows during inserts
- Fast on large datasets
- Uses indexed columns

---

## Database

Products table

- id
- name
- category
- price
- created_at
- updated_at

---

## Author

Hanshitha Dudipala