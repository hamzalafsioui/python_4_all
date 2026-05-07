# Loop Control: break, continue, pass

Sometimes you need to interrupt or modify the standard flow of a loop. Python provides three keywords for this: `break`, `continue`, and `pass`.

---

## 1. The `break` Statement
The `break` statement is used to exit the loop entirely, even if the loop condition is still `True`.

```python
for i in range(1, 10):
    if i == 5:
        break  # Loop stops here
    print(i)
# Output: 1, 2, 3, 4
```

---

## 2. The `continue` Statement
The `continue` statement skips the rest of the code inside the loop for the **current iteration** and jumps back to the start of the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue  # Skip 3
    print(i)
# Output: 1, 2, 4, 5
```

---

## 3. The `pass` Statement
The `pass` statement is a **null operation**. It does nothing. It is used as a placeholder when a statement is syntactically required but you don't want to write any code yet.

```python
if True:
    pass  # Todo: Implement this later
```

---

## 4. Loop `else` with `break`
A loop's `else` block will **NOT** run if the loop was terminated by a `break` statement. This is useful for searching.

```python
for n in [1, 2, 3]:
    if n == 2:
        break
else:
    print("Loop finished normally") # This will NOT print
```

---

> [!TIP]
> Use `break` for "early exits" and `continue` to filter out specific cases you want to ignore.
