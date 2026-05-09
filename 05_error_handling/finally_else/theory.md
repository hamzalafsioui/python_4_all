# Else & Finally: The Cleanup Crew

Beyond `try` and `except`, Python provides two more keywords to make your error handling more precise and reliable: `else` and `finally`.

---

## 1. The `else` Block
The `else` block runs **only if no exceptions were raised** in the `try` block.
- **Why?** It separates the "risky" code (inside `try`) from the code that should only run if the risky part succeeded.

```python
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File missing!")
else:
    print("Success! Reading file now...")
    content = f.read()
```

---

## 2. The `finally` Block
The `finally` block runs **no matter what**, even if an error occurred, even if the program crashes, and even if you used a `return` statement.
- **Why?** It is used for "cleanup" actions, like closing files, releasing database connections, or disconnecting from a server.

```python
try:
    f = open("data.txt", "r")
    # ... process file ...
except Exception:
    print("Error occurred")
finally:
    f.close()
    print("File closed safely.")
```

---

## 3. The Full Pattern
```python
try:
    # 1. Attempt something risky
except:
    # 2. Handle errors if they happen
else:
    # 3. Do this if NO errors happened
finally:
    # 4. Do this ALWAYS (cleanup)
```

---

> [!TIP]
> Use `finally` to ensure that resources (like memory or file handles) are always released, preventing leaks in your application.
