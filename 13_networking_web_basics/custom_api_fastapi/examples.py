# Examples: Your First FastAPI Application

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# --- 1. Basic GET Route ---
@app.get("/")
def read_root():
    """Returns a simple JSON welcome message."""
    return {"hello": "world", "status": "online"}

# --- 2. Path Parameters ---
# Access this at: http://127.0.0.1:8000/items/42
@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Path parameters are automatically converted to the correct type (int)."""
    return {"item_id": item_id, "message": f"Fetching item {item_id}"}

# --- 3. Query Parameters ---
# Access this at: http://127.0.0.1:8000/search?q=python&limit=10
@app.get("/search")
def search_items(q: str, limit: Optional[int] = 10):
    """Query parameters are optional if you provide a default value."""
    return {"query": q, "limit": limit}

# --- 4. POST Request with Body ---
class Product(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.post("/products")
def create_product(product: Product):
    """FastAPI validates that the JSON body matches the Product model."""
    return {"message": "Product created", "data": product}

# --- How to Run ---
# 1. Install: pip install fastapi uvicorn
# 2. Run: uvicorn examples:app --reload
# 3. Visit: http://127.0.0.1:8000/docs

# ------------------------------------
# If you get any errors when you try to install fast api 
# then try to run the below commands
# (Note: These commands assume you have a virtual environment (venv) activated.)
#  run this first in cmd (.venv\Scripts\Activate) 
# # 1. Install the missing tools inside your venv
# python -m pip install fastapi uvicorn
# 
# # 2. Run uvicorn by pointing to the correct folder path
# python -m uvicorn 13_networking_web_basics.custom_api_fastapi.examples:app --reload
# -------------------------------------
