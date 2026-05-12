# Unittest: The Safety Net for Your Code

The `unittest` module is Python's built-in framework for writing and running tests. It helps you ensure that your code works as expected and stays working as you add new features. In professional development, writing tests is just as important as writing the actual code.

---

## 1. Why Write Tests?
- **Catch Bugs Early**: Find errors before your users do.
- **Prevent Regressions**: Ensure new changes don't break old features.
- **Better Design**: Code that is easy to test is usually better organized.
- **Documentation**: Tests show exactly how a function is supposed to behave.

---

## 2. Basic Structure
A test file usually follows this structure:
1. Import `unittest` and the code you want to test.
2. Create a class that inherits from `unittest.TestCase`.
3. Write methods that start with `test_`.

```python
import unittest

class TestMyCode(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)
```

---

## 3. Key Assertions
Assertions are the "checks" in your tests.
- `assertEqual(a, b)`: Checks if `a == b`.
- `assertNotEqual(a, b)`: Checks if `a != b`.
- `assertTrue(x)`: Checks if `x` is True.
- `assertFalse(x)`: Checks if `x` is False.
- `assertRaises(Error)`: Checks if a specific error is raised.

---

## 4. Test Fixtures: `setUp` and `tearDown`
- **`setUp()`**: This method runs **before every single test**. Use it to prepare data or objects.
- **`tearDown()`**: This method runs **after every single test**. Use it to clean up (e.g., delete temp files).

---

## 5. How to Run Tests
In your terminal, run:
`python -m unittest filename.py`

Or, if you have many files:
`python -m unittest discover`

---

## 6. Best Practices
1. **One Thing at a Time**: Each test method should check one specific behavior.
2. **Descriptive Names**: Name your tests like `test_withdraw_insufficient_funds` so it's clear what failed.
3. **Keep Tests Independent**: One test should not depend on the result of another.
4. **Test Edge Cases**: Don't just test the "happy path." Test what happens with empty lists, zero, or invalid inputs.
