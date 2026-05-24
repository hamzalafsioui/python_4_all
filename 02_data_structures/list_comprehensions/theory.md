# List Comprehensions

List comprehensions offer a shorter syntax when you want to create a new list based on the values of an existing list.

---

## 1. The Basic Syntax
A list comprehension consists of brackets containing an expression followed by a `for` clause.

**Standard Loop:**
```python
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
    squares.append(n * n)
```

**List Comprehension:**
```python
squares = [n * n for n in numbers]
```

---

## 2. Adding a Condition (Filter)
You can add an `if` statement at the end to filter items.

```python
# Only even numbers
evens = [n for n in range(10) if n % 2 == 0]
```

---

## 3. If-Else in Comprehensions
If you want to perform an operation on items that meet a condition and a *different* operation on items that don't, move the condition to the **start**.

```python
# ["Even", "Odd", "Even", ...]
labels = ["Even" if n % 2 == 0 else "Odd" for n in range(5)]
```

---

## 4. Why use them?
- **Readability**: Once you're used to the syntax, it's often easier to read than a 4-line loop.
- **Performance**: List comprehensions are slightly faster than manual `.append()` calls because they are optimized internally by Python.

---

## 5. Other Comprehensions
Python also supports Set and Dictionary comprehensions using similar logic.

- **Set**: `{n * n for n in [1, 2, 2, 3]}` -> `{1, 4, 9}`
- **Dict**: `{n: n * n for n in range(3)}` -> `{0: 0, 1: 1, 2: 4}`

---

> [!CAUTION]
> Avoid making comprehensions too long or complex. If you have nested loops or too many conditions, a standard `for` loop is usually better for readability.

---

## Resources

- **Official Python List Comprehensions Documentation** – https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- **Real Python: List Comprehensions in Python** – https://realpython.com/list-comprehensions-python/
- **Corey Schafer: List Comprehensions (YouTube)** – https://www.youtube.com/watch?v=3dt4ozlU7c8
- **GeeksforGeeks: Python List Comprehension** – https://www.geeksforgeeks.org/python-list-comprehension/
- **Fluent Python (Book) – Chapter on Data Structures** – https://www.oreilly.com/library/view/fluent-python/9781491946237/
