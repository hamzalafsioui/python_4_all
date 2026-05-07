# Match Case (Structural Pattern Matching)

Introduced in Python 3.10, the `match` statement is a more powerful and readable alternative to multiple `if-elif` statements.

---

## 1. Basic Syntax
The `match` statement takes an expression and compares its value to successive patterns given as one or more `case` blocks.

```python
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Something went wrong")
```

---

## 2. The Wildcard `_`
The underscore `_` acts as a **catch-all** pattern. If none of the previous `case` blocks match, the `case _` block will execute. It is similar to the `else` in an `if-elif-else` chain.

---

## 3. Combining Patterns with `|` (OR)
You can combine multiple literals in a single case using the pipe `|` operator.

```python
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("It's a weekday.")
```

---

## 4. Guards (Adding Conditions)
You can add an `if` clause to a pattern, known as a **guard**. If the guard is false, `match` continues to the next case.

```python
point = (3, 5)

match point:
    case (x, y) if x == y:
        print(f"The point is on the diagonal at {x}")
    case (x, y):
        print(f"Point is at {x}, {y}")
```

---

> [!IMPORTANT]
> `match` case is only available in **Python 3.10** and later. If you are using an older version, you must use `if-elif-else`.
