# Handling Multiple Exceptions

Real-world code often has multiple points of failure. Python allows you to handle different types of errors in different ways within the same `try` block.

---

## 1. Multiple `except` Blocks
You can chain multiple `except` blocks. Python will execute the first one that matches the error type.

```python
try:
    # Some risky code
    x = int(input("Enter number: "))
    result = 10 / x
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

---

## 2. Parentheses for Grouping
If you want to handle several different errors with the same piece of code, you can group them in a tuple.

```python
try:
    # Some code
    pass
except (ValueError, TypeError):
    print("Something was wrong with the input types.")
```

---

## 3. The `Exception` Base Class
All built-in exceptions inherit from a base class called `Exception`. You can catch this to handle "anything else" that you didn't specifically list.

```python
try:
    # Code
    pass
except ValueError:
    print("Specific Value Error")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

---

> [!WARNING]
> Always list your most specific exceptions first and the general `Exception` last. If you put `except Exception` at the top, it will "swallow" all errors before the specific blocks get a chance to run.

## Resources

- **Official Python Exception Hierarchy Documentation** – https://docs.python.org/3/library/exceptions.html
- **Real Python: Python Exception Handling** – https://realpython.com/python-exceptions/
- **Corey Schafer: Python Errors and Exceptions (YouTube)** – https://www.youtube.com/watch?v=NIWwJbo-9_8
- **Python Docs: try...except...else...finally** – https://docs.python.org/3/tutorial/errors.html#handling-exceptions
- **Effective Python: 3.6 Use exceptions wisely (Book)** – https://effectivepython.com/
