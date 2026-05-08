# Try & Except: The Basics

Errors are a part of programming. Instead of letting your program crash, you can "catch" errors and handle them gracefully using `try` and `except`.

---

## 1. Why Handle Errors?
Without error handling, a single mistake (like dividing by zero) will stop your entire program immediately. This is a bad user experience.

---

## 2. Basic Syntax
The code that might cause an error goes inside the `try` block. If an error occurs, the code inside the `except` block runs.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except:
    print("Something went wrong!")
```

---

## 3. Catching Specific Exceptions
It is much better to catch specific errors rather than using a "catch-all" `except`. This prevents you from accidentally hiding bugs.

```python
try:
    val = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

Common built-in exceptions:
- `ZeroDivisionError`: Division by zero.
- `ValueError`: Incorrect type (e.g., passing a string to `int()`).
- `TypeError`: Operation on inappropriate type.
- `IndexError`: Accessing an index that doesn't exist in a list.

---

> [!TIP]
> Catch only the exceptions you expect and know how to handle. Let the others bubble up so you can find and fix the underlying bugs!
