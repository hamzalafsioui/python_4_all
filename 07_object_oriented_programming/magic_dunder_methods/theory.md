# Magic (Dunder) Methods: Giving Your Objects Superpowers

**Magic Methods** (also called **Dunder Methods** for "Double Under") are special methods that start and end with double underscores (like `__init__`). They allow your custom objects to behave like built-in Python types.

---

## 1. Representation Methods
These control how your object looks when printed or inspected.

- **`__str__(self)`**: Returns a user-friendly string representation of the object. Used by `print()` and `str()`.
- **`__repr__(self)`**: Returns an unambiguous string representation, mainly for developers (debugging).

---

## 2. Mathematical Operators
You can define how objects interact with operators like `+`, `-`, and `*`.

- **`__add__(self, other)`**: Handles the `+` operator.
- **`__sub__(self, other)`**: Handles the `-` operator.
- **`__mul__(self, other)`**: Handles the `*` operator.

---

## 3. Comparison Operators
- **`__eq__(self, other)`**: Handles `==`.
- **`__lt__(self, other)`**: Handles `<`.
- **`__gt__(self, other)`**: Handles `>`.

---

## 4. Collection Methods
- **`__len__(self)`**: Allows you to use `len(obj)`.
- **`__getitem__(self, index)`**: Allows you to use `obj[index]`.

---

## 5. How It Works
When you write `a + b`, Python secretly looks for `a.__add__(b)`. If it finds it, it runs your code! This is called **Operator Overloading**.

---

## 6. Best Practices
1. **Be Consistent**: If you implement `__add__`, users expect it to behave like addition. Don't use `+` to delete files!
2. **Always Implement `__str__`**: It makes debugging and logging much easier.
3. **Check Types**: In methods like `__add__`, always check if the `other` object is of the type you expect before performing operations.
---

## Resources

- **Official Python Data Model Documentation** – https://docs.python.org/3/reference/datamodel.html
- **Real Python: Python Magic Methods and Operator Overloading** – https://realpython.com/python-magic-methods/
- **Corey Schafer: Python OOP Tutorial - Dunder Methods (YouTube)** – https://www.youtube.com/watch?v=3ohzBxoFHAY
- **GeeksforGeeks: Python Magic Methods** – https://www.geeksforgeeks.org/magic-methods-in-python/
- **Fluent Python (Book) – Chapter on Data Model** – https://www.oreilly.com/library/view/fluent-python/9781491946237/
