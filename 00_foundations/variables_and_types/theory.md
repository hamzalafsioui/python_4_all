# Variables and Data Types

Welcome to the first step of your Python journey! In this module, we'll explore how Python stores and manages information using **variables** and **data types**.

---

## 1. What is a Variable?
A variable is a symbolic name that refers to a value stored in the computer's memory. Think of it as a **labeled box** where you can store data and retrieve it later using the label.

```python
name = "Alice"
age = 25
```

### Key Concepts:
- **Assignment**: The `=` operator is used to assign a value to a variable.
- **Dynamic Typing**: In Python, you don't need to declare the type of a variable. It is determined automatically based on the value assigned.

---

## 2. Basic Data Types
Python has several built-in data types that you'll use frequently:

| Type | Description | Example |
| :--- | :--- | :--- |
| `int` | Integers (whole numbers) | `10`, `-5`, `0` |
| `float` | Floating-point numbers (decimals) | `3.14`, `-0.01`, `2.0` |
| `str` | Strings (text) | `"Hello"`, `'Python'` |
| `bool` | Booleans (truth values) | `True`, `False` |

---

## 3. Type Checking and Casting
You can check the type of any variable using the `type()` function.

```python
x = 42
print(type(x))  # <class 'int'>
```

### Type Casting (Conversion)
Sometimes you need to convert a value from one type to another. This is called **casting**.

```python
# Convert to integer
score = int("100") 

# Convert to float
price = float(5)   # 5.0

# Convert to string
message = str(123) # "123"
```

---

## 4. Naming Conventions (PEP 8)
To write clean, readable Python code, follow these naming rules:
- **Snake Case**: Use lowercase words separated by underscores (e.g., `user_name`, `total_score`).
- **Descriptive**: Choose names that reflect the variable's purpose.
- **Rules**:
    - Must start with a letter or underscore.
    - Cannot start with a number.
    - Can only contain alphanumeric characters and underscores (A-z, 0-9, and _).
    - Case-sensitive (`Age` and `age` are different).

---

> Use `print()` to see the value of your variables during development !!!
