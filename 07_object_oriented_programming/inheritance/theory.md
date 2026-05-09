# Inheritance: Building Hierarchies

Inheritance is a fundamental concept in OOP that allows a class (the **Child** or **Subclass**) to inherit attributes and methods from another class (the **Parent** or **Base Class**).

---

## 1. Why Use Inheritance?
- **Code Reuse**: Write code once in the parent class and use it in all children.
- **Organization**: Model "is a" relationships (e.g., a `Student` **is a** `Person`).
- **DRY (Don't Repeat Yourself)**: Avoid copying and pasting the same attributes across multiple classes.

---

## 2. Basic Syntax
```python
class Parent:
    # Attributes and Methods

class Child(Parent):
    # Inherits everything from Parent
```

---

## 3. The `super()` Function
The `super()` function is the most common way to call methods from the parent class inside the child class. This is almost always used in the `__init__` method to ensure the parent part of the object is set up correctly.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # Let the Parent handle name and age
        self.student_id = student_id
```

---

## 4. Method Overriding
A child class can provide its own implementation of a method that already exists in the parent class. This is called **overriding**.

---

## 5. Multiple Inheritance
Python allows a class to inherit from more than one parent.
```python
class Child(Parent1, Parent2):
    pass
```
Python uses the **MRO (Method Resolution Order)** to decide which parent's method to run if they share the same name. You can see this order by calling `ClassName.mro()`.

---

## 6. Best Practices
1. **The "Is-A" Test**: Only use inheritance if you can say "Child IS A Parent." If it's just "Child HAS A Parent," use **Composition** instead (making the parent an attribute of the child).
2. **Don't Over-inherit**: Deep hierarchies (5+ levels) become very hard to debug. Keep it shallow!
3. **Use `isinstance()` and `issubclass()`**: Professional ways to check relationships at runtime.
