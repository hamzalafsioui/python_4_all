# Attributes & Methods: Deep Dive

In this section, we go beyond simple variables and functions. We'll explore how data and behavior can be shared across all instances of a class or kept strictly unique to one.

---

## 1. Instance vs. Class Attributes

### Instance Attributes
These are unique to each object. They are defined inside `__init__` using `self`.
```python
class Dog:
    def __init__(self, name):
        self.name = name  # Each dog has its own name
```

### Class Attributes
These are shared by **all** instances of a class. They are defined directly inside the class but outside any methods.
```python
class Dog:
    species = "Canine"  # All dogs belong to this species
```

---

## 2. The Three Types of Methods

### Instance Methods
The most common type. They take `self` as the first argument and can access/modify both instance and class data.

### Class Methods (`@classmethod`)
They take `cls` as the first argument. They are used when you need to access or modify class-level data (data that applies to the blueprint itself, not a specific house).
**Common Use**: "Factory methods" that create objects in a special way.

### Static Methods (`@staticmethod`)
They don't take `self` or `cls`. They are just normal functions that happen to live inside a class because they are logically related to it.

---

## 3. Getters, Setters, and `@property`
In professional Python, we don't usually write `get_name()` or `set_name()`. Instead, we use the `@property` decorator to make a method act like an attribute.

**Why?** It allows you to add validation logic (like checking if an age is negative) without changing how the user accesses the data.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value
```

---

## 4. Best Practices
1. **Prefer Instance Attributes**: Only use class attributes for constants or shared data (like a global counter).
2. **Use `@property` for Validation**: Never let a user modify "sensitive" data directly if there are rules to follow.
3. **Keep Methods Focused**: A method should do one thing well. If it's getting too long, break it into smaller helper methods.
---

## Resources

- **Official Python Documentation on Classes** – https://docs.python.org/3/tutorial/classes.html
- **Real Python: Python Classes and Objects – Attributes & Methods** – https://realpython.com/python3-object-oriented-programming/#attributes-and-methods
- **Corey Schafer: Python OOP – Class & Instance Attributes (YouTube)** – https://www.youtube.com/watch?v=ZDa-Z5JzLYM
- **GeeksforGeeks: Python Class Attributes and Methods** – https://www.geeksforgeeks.org/python-class-attributes-and-methods/
- **Fluent Python (Book) – Chapter on Data Model / Attributes** – https://www.oreilly.com/library/view/fluent-python/9781491946237/
