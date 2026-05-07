# While Loops

A `while` loop repeats a block of code as long as a specified condition is `True`.

---

## 1. Basic Syntax
The loop will continue to run as long as the condition remains true.

```python
count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1  # Important: Update the condition!
```

---

## 2. Infinite Loops
If the condition never becomes `False`, the loop will run forever. This can crash your program.

```python
# WARNING: This is an infinite loop
# while True:
#     print("Stuck!")
```

---

## 3. The `while-else` Statement
Python allows an optional `else` block after a `while` loop. The `else` block runs when the loop condition becomes `False`.

```python
i = 1
while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished!")
```

---

## 4. When to use `while` vs `for`?
- **`for`**: Use when you know exactly how many times to loop (e.g., iterating over a list).
- **`while`**: Use when the number of iterations depends on a condition (e.g., waiting for user input).

---

> [!CAUTION]
> Always make sure your `while` loop has a clear exit strategy (a way for the condition to become `False`)!
