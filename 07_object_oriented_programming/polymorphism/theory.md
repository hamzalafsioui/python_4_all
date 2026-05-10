# Polymorphism: One Interface, Many Forms

**Polymorphism** (from Greek *poly* meaning "many" and *morph* meaning "form") is the ability of different objects to respond to the same method call in their own way.

---

## 1. The Core Concept
In Python, polymorphism allows you to define methods in a child class that have the same name as methods in the parent class. It also allows you to write functions that can take different types of objects and interact with them as long as they follow a certain "interface."

---

## 2. Duck Typing
Python uses a concept called **Duck Typing**: 
> "If it walks like a duck and quacks like a duck, it's a duck."

This means Python doesn't care about the *type* of an object as much as it cares about what the object can *do*. If two different classes both have a `draw()` method, you can put them in a list and call `draw()` on both without checking their class.

```python
def start_engine(vehicle):
    vehicle.start() # Works for Car, Boat, or Plane as long as they have a start() method
```

---

## 3. Abstract Base Classes (ABCs)
While Duck Typing is flexible, sometimes you want to **force** a group of classes to implement certain methods. This is where the `abc` module comes in. An **Abstract Class** is a class that cannot be instantiated it exists only to be inherited from.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

## 4. Polymorphic Functions
Functions like `len()` are polymorphic. You can pass it a string, a list, or a dictionary, and it knows how to handle each one correctly.

---

## 5. Best Practices
1. **Focus on Behavior**: Write functions that rely on what an object can do, not what it is.
2. **Use ABCs for Large Projects**: When working in teams, ABCs act as a "contract" that ensures everyone implements the required methods.
3. **Avoid Complex Type Checking**: Instead of checking `if type(x) == Y`, just try calling the method and handle the error, or use polymorphism to let the object handle itself.
