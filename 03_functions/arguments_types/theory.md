# Argument Types: Positional, Keyword, and Default

Python provides several ways to pass arguments to a function, giving you great flexibility in how functions are used.

---

## 1. Positional Arguments
By default, arguments are passed in the order they are defined.

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("Dog", "Rex") # Order matters!
```

---

## 2. Keyword Arguments
You can pass arguments using the name of the parameter. This makes the order irrelevant.

```python
describe_pet(name="Rex", animal="Dog") # Order doesn't matter here
```

---

## 3. Default Arguments
You can assign a default value to a parameter in the function definition. If the argument is missing in the call, the default is used.

```python
def greet(name, msg="Good morning"):
    print(f"{msg}, {name}!")

greet("Hamza") # Good morning, Hamza!
greet("Ali", "Hello") # Hello, Ali!
```

---

## 4. Variable-Length Arguments (`*args` and `**kwargs`)
Sometimes you don't know how many arguments will be passed.

- **`*args`**: Receives a **tuple** of additional positional arguments.
- **`**kwargs`**: Receives a **dictionary** of additional keyword arguments.

```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5)) # 15
```

---

> [!IMPORTANT]
> **The Order Rule**: When defining a function, positional parameters must come **before** default parameters!
> `def func(a, b=10):` ✅
> `def func(a=10, b):` ❌ (Syntax Error)

---

## Resources

- **Official Python Docs** – Function definitions and argument conventions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- **Real Python** – *How to Use Arguments in Python Functions*: https://realpython.com/python-arguments/
- **Corey Schafer** – *Python Function Arguments* (YouTube): https://www.youtube.com/watch?v=9Os0o3wzS_k
- **GeeksforGeeks** – *Python Function Arguments*: https://www.geeksforgeeks.org/python-function-arguments/
- **Fluent Python** – Chapter 3 “Functions” (covers positional, keyword, default, *args, **kwargs)
