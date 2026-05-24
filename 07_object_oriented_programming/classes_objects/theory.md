# OOP Part 1: Classes & Objects

Object-Oriented Programming (OOP) is a paradigm based on the concept of **"objects"**, which can contain data (attributes) and code (methods). It is the standard for building complex, maintainable software.

---

## 1. The Blueprint Analogy
Think of a **Class** as a blueprint for a house. The blueprint itself isn't a house, but it describes exactly how a house should be built.
An **Object** (or **Instance**) is the actual house built from that blueprint. You can build 100 houses from one blueprint each might have different paint colors, but they all have the same structure.

---

## 2. Anatomy of a Class

### The `__init__` Method (The Constructor)
This special method runs automatically when you create a new object. It sets up the initial state of the object.

### The `self` Keyword
`self` represents the specific instance of the object being created. It allows the code to distinguish between "my name" and "your name" when multiple objects exist.

```python
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def ring(self):         # Method
        print(f"Your {self.brand} {self.model} is ringing!")
```

---

## 3. Best Practices & Professional Standards

### Naming Conventions
- **Classes**: Use `PascalCase` (e.g., `UserAccount`, `DataProcessor`).
- **Methods/Attributes**: Use `snake_case` (e.g., `get_balance()`, `user_id`).

### Documentation (Docstrings)
Professional Python classes always include a docstring explaining the purpose of the class and its parameters.

### Encapsulation (Basics)
In Python, we use a single underscore `_` to suggest an attribute is "private" and shouldn't be touched from outside the class.
```python
class BankAccount:
    def __init__(self, amount):
        self._balance = amount  # Suggests "Don't touch this directly!"
```

### Single Responsibility Principle (SRP)
A class should have one job. Don't create a `GodClass` that handles database connection, user logic, and email sending all at once. Break it down!

---

> [!TIP]
> Use `isinstance(obj, ClassName)` to check if an object belongs to a certain class. This is much better than comparing types directly.

## Resources

- **Official Python OOP Documentation** – https://docs.python.org/3/tutorial/classes.html
- **Real Python: Object-Oriented Programming (OOP) in Python** – https://realpython.com/python3-object-oriented-programming/
- **Corey Schafer: OOP Tutorial (YouTube)** – https://www.youtube.com/watch?v=JeznW_7DlB0
- **Python Docs: Data Model** – https://docs.python.org/3/reference/datamodel.html
- **Effective Python: 12. Use properties instead of public data attributes** – https://effectivepython.com/
