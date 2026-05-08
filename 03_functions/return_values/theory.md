# Function Return Values

While some functions perform an action (like printing to the console), many functions are used to calculate and **return** a result back to the code that called them.

---

## 1. The `return` Keyword
The `return` statement is used to end the execution of the function call and "send back" a result.

```python
def add(a, b):
    return a + b

result = add(5, 3) # result now holds the value 8
print(result)
```

---

## 2. `print()` vs `return`
This is a common point of confusion for beginners:
- **`print()`**: Displays a value in the terminal for humans to see. The program cannot "use" this value later.
- **`return`**: Passes a value to the program. The program can store it in a variable, use it in another calculation, etc.

---

## 3. Returning Multiple Values
Python functions can return multiple values at once by separating them with commas. Behind the scenes, Python packs these into a **tuple**.

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([1, 2, 3, 4, 5])
```

---

## 4. Early Returns
A function stops immediately when it hits a `return` statement. You can use this for "guard clauses" or to stop processing early.

```python
def check_age(age):
    if age < 0:
        return "Invalid age" # Stops here if age is negative
    
    if age < 18:
        return "Minor"
    return "Adult"
```

---

## 5. The `None` Value
If a function doesn't have a `return` statement, it implicitly returns `None`.

---

> [!TIP]
> Use `return` whenever you want a function to produce a piece of data that will be used by other parts of your program.
