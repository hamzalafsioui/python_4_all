# For Loops

A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

---

## 1. Basic Iteration
The most common use of a `for` loop is to process each item in a collection.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

## 2. The `range()` Function
To loop through a set of code a specified number of times, we use the `range()` function.

- `range(5)`: 0, 1, 2, 3, 4
- `range(2, 6)`: 2, 3, 4, 5
- `range(1, 10, 2)`: 1, 3, 5, 7, 9 (step of 2)

```python
for i in range(3):
    print(f"Iteration {i}")
```

---

## 3. The `enumerate()` Function
If you need both the **index** and the **value** while looping, use `enumerate()`.

```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
```

---

## 4. Looping Through Strings
Strings are iterable objects—they contain a sequence of characters.

```python
word = "Python"
for char in word:
    print(char.upper())
```

---

> [!TIP]
> You can nest loops inside each other to work with multi-dimensional data like matrices!
