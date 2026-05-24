# Python Dictionaries

Dictionaries are used to store data values in **key:value** pairs. They are ordered (as of Python 3.7), changeable, and do not allow duplicate keys.

---

## 1. What is a Dictionary?
Think of a dictionary like a real-world dictionary or a phonebook. You look up a **key** (the word or name) to find its associated **value** (the definition or number).

```python
user = {
    "name": "Hamza",
    "age": 25,
    "is_pro": True
}
```

---

## 2. Accessing Items
You can access a value by referring to its key name inside square brackets `[]`.

```python
print(user["name"]) # "Hamza"
```

### Safe Access with `.get()`
If the key doesn't exist, `[]` will raise an error. Use `.get()` to return `None` (or a default value) instead.

```python
print(user.get("email", "No email found"))
```

---

## 3. Modifying & Adding
Dictionaries are mutable. You can change values or add new pairs easily.

```python
user["age"] = 26        # Update existing
user["city"] = "Rabat"  # Add new
```

---

## 4. Looping Through Dictionaries
You can loop through keys, values, or both:

- **Keys**: `for k in user.keys():`
- **Values**: `for v in user.values():`
- **Pairs**: `for k, v in user.items():`

---

## 5. Removing Items
- **`.pop("key")`**: Removes the specified key and returns its value.
- **`del user["key"]`**: Deletes the key-value pair.
- **`.clear()`**: Empties the entire dictionary.

---

> [!IMPORTANT]
> **Keys must be immutable!** You can use strings, numbers, or tuples as keys, but you cannot use **lists** because they can change.

---

## Resources

- **Official Python Dictionaries Documentation** – https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- **Real Python: Python Dictionaries** – https://realpython.com/python-dicts/
- **Corey Schafer: Python Dictionaries (YouTube)** – https://www.youtube.com/watch?v=daefaLgNkwk
- **GeeksforGeeks: Python Dictionary** – https://www.geeksforgeeks.org/python-dictionary/
- **Fluent Python (Book) – Chapter on Dictionaries** – https://www.oreilly.com/library/view/fluent-python/9781491946237/

