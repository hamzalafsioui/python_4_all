# Pytest: Modern Testing in Python

While `unittest` is built into Python, **pytest** is the most popular testing framework in the Python community. It is known for its simple syntax, powerful features like fixtures, and its ability to run `unittest` tests as well.

---

## 1. Why `pytest`?
- **Less Boilerplate**: No need to create classes or remember complex assertion names like `assertEqual`. Just use standard Python `assert`.
- **Informative Failures**: When a test fails, `pytest` shows you exactly what the values were and why they didn't match.
- **Fixtures**: A modular way to handle setup and teardown.
- **Parametrization**: Run the same test multiple times with different data using a single function.

---

## 2. Basic Syntax
In `pytest`, a test is just a function that starts with `test_`.

```python
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
```

---

## 3. Fixtures (`@pytest.fixture`)
Fixtures are functions that provide data or setup for your tests. You pass them as arguments to your test functions.

```python
import pytest

@pytest.fixture
def sample_user():
    return {"name": "Hamza", "admin": True}

def test_user_is_admin(sample_user):
    assert sample_user["admin"] is True
```

---

## 4. Parametrization (`@pytest.mark.parametrize`)
This allows you to test multiple scenarios in one function.

```python
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (10, -2, 8)
])
def test_add_many(a, b, expected):
    assert a + b == expected
```

---

## 5. How to Run Tests
1. Install it: `pip install pytest`
2. Run: `pytest` (It will find all files starting with `test_` or ending with `_test.py`).

---

## 6. Best Practices
1. **Keep Assertions Simple**: One `assert` per test is a good rule of thumb for clarity.
2. **Use Fixtures for Reusability**: If you need a database connection or a complex object in 5 tests, make it a fixture.
3. **Group by Logic**: Even though classes aren't required, you can still use them to group related tests.
