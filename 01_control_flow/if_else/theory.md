# Conditional Statements (if, elif, else)

Control flow allows your program to make decisions and execute different blocks of code based on certain conditions.

---

## 1. The `if` Statement
The `if` statement is the most basic form of control flow. It executes a block of code only if a specified condition is `True`.

```python
age = 18
if age >= 18:
    print("You are an adult.")
```

---

## 2. Adding `else` and `elif`
- **`else`**: Provides a fallback block of code if the `if` condition is `False`.
- **`elif`** (short for else if): Allows you to check multiple conditions in sequence.

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

---

## 3. Comparison Operators
Conditions usually involve comparing values:

| Operator | Description | Example |
| :--- | :--- | :--- |
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater than or equal to | `x >= 5` |
| `<=` | Less than or equal to | `x <= 5` |

---

## 4. Logical Operators
You can combine multiple conditions using logical operators:
- **`and`**: Returns `True` if both conditions are true.
- **`or`**: Returns `True` if at least one condition is true.
- **`not`**: Reverses the boolean value (True becomes False, and vice versa).

```python
is_weekend = True
is_sunny = False

if is_weekend and is_sunny:
    print("Go to the beach!")
elif is_weekend and not is_sunny:
    print("Stay home and watch a movie.")
```

---

## 5. Ternary Operator (One-liner)
For simple conditions, Python provides a shorthand way to write an `if-else` statement.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

### **IMPORTANT**
Indentation is CRITICAL in Python. All code within an `if`, `elif`, or `else` block must be indented by the same amount (usually 4 spaces).
