# Python Functions

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

---

## 1. Why use Functions?
- **DRY (Don't Repeat Yourself)**: Instead of writing the same code 10 times, write it once in a function and call it 10 times.
- **Organization**: Functions break large programs into smaller, manageable pieces.
- **Reusability**: You can use the same function in different parts of your program or even in other projects.

---

## 2. Defining a Function
In Python, a function is defined using the `def` keyword.

```python
def my_function():
    print("Hello from a function!")
```

To call a function, use the function name followed by parenthesis:
```python
my_function()
```

---

## 3. Parameters and Arguments
Information can be passed into functions as arguments.

- **Parameter**: The variable listed inside the parentheses in the function definition (the placeholder).
- **Argument**: The value that is sent to the function when it is called (the actual value).

```python
def greet(name): # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Hamza") # "Hamza" is an argument
```

---

## 4. Docstrings
It is best practice to include a description of what the function does. This is called a **docstring** and is written inside triple quotes `"""`.

```python
def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b
```

---

> [!TIP]
> Functions in Python must be defined **before** they are called!
