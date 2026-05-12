# Examples: Power-Testing with Pytest

import pytest

# --- Code to Test ---
def divide(a, b):
    if b == 0:
        raise ValueError("Zero Division!")
    return a / b

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# --- Pytest Suite ---

# 1_ Using Fixtures
@pytest.fixture
def laptop():
    """Provides a fresh Product object for tests."""
    return Product("MacBook", 1200)

def test_product_initialization(laptop):
    assert laptop.name == "MacBook"
    assert laptop.price == 1200

# 2_ Testing Exceptions
def test_divide_error():
    with pytest.raises(ValueError):
        divide(10, 0)

# 3_ Parametrization (Testing multiple cases)
@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 5),
    (20, 4, 5),
    (100, 10, 10),
    (1, 1, 1)
])
def test_divide_bulk(x, y, expected):
    assert divide(x, y) == expected

# --- Note on Running ---
# To run this, you must have pytest installed: 'pip install pytest' or 'python -m pip install pytest'
# Then run: 'pytest examples.py' or 'python -m pytest 10_testing_debugging/pytest/examples.py'
