# Nested Structures

In Python, you can place any object inside another collection. This allows you to create complex, hierarchical data structures like lists of lists, dictionaries of dictionaries, or lists of dictionaries.

---

## 1. Lists of Lists (Matrices)
Often used for 2D grids, spreadsheets, or mathematical matrices.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing: row 1, column 2
print(matrix[1][2]) # 6
```

---

## 2. Dictionaries of Dictionaries (JSON-like)
Commonly used to represent objects or database records.

```python
employees = {
    "emp1": {"name": "Ali", "role": "Dev"},
    "emp2": {"name": "Hamza", "role": "Lead"}
}

# Accessing
print(employees["emp2"]["name"]) # "Hamza"
```

---

## 3. Lists of Dictionaries
The most common way to represent a list of items where each item has multiple properties (e.g., a product catalog).

```python
products = [
    {"id": 1, "name": "Phone", "price": 500},
    {"id": 2, "name": "Laptop", "price": 1200}
]

# Accessing
print(products[0]["name"]) # "Phone"
```

---

## 4. Deep Copy vs. Shallow Copy
When you copy a nested structure using standard assignment (`list2 = list1`), only the **reference** to the inner objects is copied. If you change a nested item in `list1`, it will also change in `list2`.

To create a completely independent copy, use the `copy` module:
```python
import copy
new_structure = copy.deepcopy(old_structure)
```

---

> [!TIP]
> When working with deeply nested data (like API responses), always use `.get()` for dictionaries to avoid `KeyError` if a level is missing!
---

## Resources

- **Official Python Data Structures Documentation** – https://docs.python.org/3/tutorial/datastructures.html
- **Real Python: Working with Nested Data Structures** – https://realpython.com/python-nested-data-structures/
- **Corey Schafer: Working with JSON Data (YouTube)** – https://www.youtube.com/watch?v=9LgyK7X5Z9U
- **GeeksforGeeks: Nested Dictionaries in Python** – https://www.geeksforgeeks.org/python-nested-dictionaries/
- **Fluent Python (Book) – Chapter on Data Structures** – https://www.oreilly.com/library/view/fluent-python/9781491946237/
