# Context Managers: Safe Resource Management

A **Context Manager** is a Python object that automates the "Setup" and "Teardown" phases of a task. It is most commonly used with the `with` statement to ensure that resources (like files, database connections, or network sockets) are properly closed, even if an error occurs.

---

## 1. The "Setup and Teardown" Pattern
Whenever you see a pattern like this:
1. **Setup**: Open a file.
2. **Body**: Write data to the file.
3. **Teardown**: Close the file.

...you should use a Context Manager. It guarantees that step 3 always happens.

---

## 2. Class-Based Context Managers
To create a context manager using a class, you must implement two magic methods:
- `__enter__(self)`: Runs at the start of the `with` block. Returns the resource.
- `__exit__(self, exc_type, exc_val, exc_tb)`: Runs at the end of the block. Handles cleanup and exceptions.

```python
class MyContext:
    def __enter__(self):
        print("Setup...")
        return self
        
    def __exit__(self, type, value, traceback):
        print("Teardown...")
```

---

## 3. Function-Based Context Managers (`contextlib`)
The `contextlib` module provides a decorator that makes it much easier to write context managers using a generator function.

```python
from contextlib import contextmanager

@contextmanager
def simple_manager():
    print("Setup...")
    yield  # The 'with' block body runs here
    print("Teardown...")
```

---

## 4. Why Use Them?
1. **Prevent Resource Leaks**: Ensures you don't leave files or connections open.
2. **Error Handling**: You can catch and handle exceptions inside `__exit__`.
3. **Cleaner Code**: Removes the need for messy `try...finally` blocks.

---

## 5. Best Practices
1. **Keep it Small**: A context manager should focus on one resource.
2. **Don't Swallow Errors**: Unless you have a good reason, let exceptions propagate through `__exit__` so the user knows something went wrong.
3. **Use for Transactions**: Perfect for database commits/rollbacks.
