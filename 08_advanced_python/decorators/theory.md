# Decorators: The Art of Wrapping Functions

A **Decorator** is a design pattern in Python that allows you to add new functionality to an existing object (usually a function) without modifying its structure. It's like wrapping a gift: the gift inside stays the same, but the wrapping paper adds extra value.

---

## 1. Prerequisites: First-Class Functions
To understand decorators, you must remember that in Python, functions are "First-Class Citizens." This means:
1. You can assign a function to a variable.
2. You can pass a function as an argument to another function.
3. You can return a function from a function.

---

## 2. The Mental Model: Function Factories
Think of a decorator as a **factory** for functions.
1. You give the factory your original function (`func`).
2. The factory creates a new, enhanced version of that function (`wrapper`).
3. The factory gives you back the enhanced version.

From that point on, whenever you call your function, you are actually calling the **wrapper**.

---

## 3. Step-by-Step: What Happens Behind the Scenes?
When you use the `@` syntax, Python performs a hidden assignment.

```python
@my_decorator
def say_hello():
    pass

# IS THE SAME AS:
say_hello = my_decorator(say_hello)
```

### The Execution Flow:
1. **Definition**: Python reads the `say_hello` function.
2. **Decoration**: Python immediately passes `say_hello` to `my_decorator`.
3. **Assignment**: `say_hello` now points to the `wrapper` function inside the decorator.
4. **Invocation**: When you call `say_hello()`, you are actually calling `wrapper()`.
5. **Inside the Wrapper**: The `wrapper` does its extra work, then calls the original `func()`.

---

## 4. Handling Arguments & Returns (The "Pro" Pattern)
To make a decorator truly "universal," it must handle three things:
1. **Any arguments**: Use `*args` and `**kwargs`.
2. **Returning values**: The wrapper **MUST** return the result of the original function.
3. **Metadata**: Use `@wraps(func)`.

```python
def universal_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Action BEFORE
        result = func(*args, **kwargs) # 2. Execute original
        # 3. Action AFTER
        return result                  # 4. Give the result back
    return wrapper
```

---

## 5. Best Practice: `functools.wraps`
When you wrap a function, it "loses" its metadata (like its name and docstring). To fix this, always use the `@wraps` decorator from the `functools` module inside your own decorator.

```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## 6. Advanced: Decorators with Arguments
Sometimes you want to pass data *to* the decorator itself (e.g., `@repeat(3)`). This requires **three layers**:
1. **The Factory**: Takes the decorator's arguments (e.g., `num_times`).
2. **The Decorator**: Takes the function (`func`).
3. **The Wrapper**: Takes the function's arguments (`*args`, `**kwargs`).

```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
```

---

> [!IMPORTANT]
> Decorators are evaluated at **import time** (when the script starts), not when the decorated function is called. This makes them extremely efficient for setting up configurations or protections.
