"""
PROJECT: E-commerce Cart Test Suite

Goal: Build a ShoppingCart class and test it thoroughly using pytest fixtures and parametrization.

Requirements:

1. The Class 'ShoppingCart':
   - 'items': A list of dictionaries {"name": str, "price": float}.
   - 'add_item(name, price)': Adds to list.
   - 'total_price()': Returns sum of all item prices.
   - 'item_count()': Returns number of items.

2. The Pytest Suite:
   - Fixture 'cart': Returns a fresh ShoppingCart instance.
   - Test 'add_items': Add 2 items and check total_price and item_count.
   - Parametrized Test 'bulk_pricing': 
     - Test adding different items and verify the total is correct each time.
     - Scenarios: [(item1, 10.0), (item2, 20.5)] -> 30.5

Real-World Logic:
- This demonstrates how fixtures replace 'setUp' from unittest, and how parametrization makes your tests much more compact and powerful.
"""

import pytest

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def total_price(self):
        return sum(item["price"] for item in self.items)

    def item_count(self):
        return len(self.items)

# TODO: Implement the Pytest Suite

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_items(cart):
    cart.add_item("Book", 10.0)
    cart.add_item("Pen", 5.0)
    assert cart.total_price() == 15.0
    assert cart.item_count() == 2

@pytest.mark.parametrize("item_name, price, expected_total", [
    ("Book", 10.0, 10.0),
    ("Pen", 5.0, 5.0),
    ("Laptop", 1000.0, 1000.0)
])
def test_bulk_pricing(cart, item_name, price, expected_total):
    cart.add_item(item_name, price)
    assert cart.total_price() == expected_total
