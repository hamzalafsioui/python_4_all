# Encapsulation: Protecting Your Data

**Encapsulation** is the practice of bundling data and methods inside a single unit (a class) and **restricting direct access** to some of the object's components. This prevents accidental modification and hides the internal complexity from the user.

---

## 1. Access Modifiers in Python
Unlike languages like Java or C++, Python doesn't have strict "private" keywords. Instead, it uses naming conventions to signal how an attribute should be used.

### A. Public (e.g., `self.name`)
Accessible from anywhere. These are part of your class's "Public API."

### B. Protected (e.g., `self._balance`)
Starts with a single underscore. This is a **convention** telling other developers: "This is internal; don't touch it unless you are a subclass." It is still technically accessible, but it's considered bad practice to do so.

### C. Private (e.g., `self.__password`)
Starts with a double underscore. This triggers **Name Mangling**, making it much harder (but not impossible) to access from outside.

---

## 2. Name Mangling
When you use `__private`, Python renames the attribute to `_ClassName__private`. This is intended to prevent name clashes in subclasses, but it also acts as a "strong warning" against external access.

---

## 3. The Pythonic Way: `@property`
Encapsulation isn't just about hiding data; it's about **controlling** how it's accessed. Instead of making everything public, use the `@property` decorator to create "Getters" and "Setters."

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        """Getter: Allows reading but adds logic (like hiding cents)."""
        return f"${self.__balance:,.2f}"

    @balance.setter
    def balance(self, value):
        """Setter: Adds validation before changing the data."""
        if value < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = value
```

---

## 4. Best Practices
1. **Default to Protected (`_`)**: Most internal data should be protected.
2. **Use Private (`__`) Sparingly**: Only use double underscores if you truly want to prevent name clashes or very strong warnings.
3. **Hide the "How," Show the "What"**: Users of your class should know *what* they can do (e.g., `account.deposit()`), but they shouldn't need to know *how* the balance is stored internally.
---

## Resources

- **Official Python Documentation on Encapsulation** – https://docs.python.org/3/tutorial/classes.html#private-variables
- **Real Python: Encapsulation in Python** – https://realpython.com/encapsulation-in-python/
- **Corey Schafer: Python OOP - Encapsulation (YouTube)** – https://www.youtube.com/watch?v=VJ6QZ-6L0I0
- **GeeksforGeeks: Encapsulation in Python** – https://www.geeksforgeeks.org/encapsulation-in-python/
- **Fluent Python (Book) – Chapter on Encapsulation** – https://www.oreilly.com/library/view/fluent-python/9781491946237/

