# Custom Exceptions & Raising Errors

Sometimes, Python's built-in errors (like `ValueError`) aren't specific enough for your needs. In these cases, you can create your own **Custom Exceptions**.

---

## 1. The `raise` Keyword
You can manually trigger an error using the `raise` keyword. This is useful when code is technically valid but logically wrong (e.g., a person's age being -5).

```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative!")
```

---

## 2. Creating Custom Exceptions
To create a custom exception, you simply create a class that inherits from Python's built-in `Exception` class.

```python
class WithdrawalError(Exception):
    """Exception raised when a bank withdrawal fails."""
    pass

# Usage
balance = 100
amount = 200

if amount > balance:
    raise WithdrawalError("Insufficient funds for this withdrawal.")
```

---

## 3. Why Use Custom Exceptions?
1. **Clarity**: It makes it obvious exactly what went wrong in your business logic.
2. **Specific Catching**: You can catch your custom error without accidentally catching other built-in errors.

```python
try:
    withdraw(200)
except WithdrawalError as e:
    print(f"Bank Error: {e}")
except Exception as e:
    print(f"System Error: {e}")
```

---

> [!IMPORTANT]
> When creating custom exceptions, always give them descriptive names ending in `Error` (e.g., `NetworkTimeoutError`, `InvalidInputError`). This follows the standard Python naming convention.
