# Python Tuples

Tuples are used to store multiple items in a single variable. While they look similar to lists, they have one fundamental difference: **Immutability**.

---

## 1. What is a Tuple?
A tuple is a collection which is **ordered** and **unchangeable** (immutable). Tuples are written with round brackets `()`.

```python
point = (10, 20)
```

---

## 2. Why use Tuples?
- **Performance**: Tuples are slightly faster than lists.
- **Safety**: Use tuples for data that should never be changed by the program (like settings or coordinates).
- **Dictionary Keys**: Because they are immutable, tuples can be used as keys in dictionaries (lists cannot).

---

## 3. Tuple Packing and Unpacking
This is one of the most powerful features of tuples.

### Packing
```python
coordinates = 4.5, 5.8, 9.2 # Parentheses are optional when packing
```

### Unpacking
```python
x, y, z = coordinates
print(x) # 4.5
```

---

## 4. Immutability in Action
If you try to change an item in a tuple, Python will raise a `TypeError`.

```python
my_tuple = (1, 2, 3)
# my_tuple[1] = 10 # This will ERROR!
```

---

## 5. Tuple Methods
Since tuples cannot be changed, they have only two built-in methods:
- `.count(value)`: Returns the number of times a specified value occurs.
- `.index(value)`: Returns the index of the first occurrence of a specified value.

---

> [!IMPORTANT]
> To create a tuple with only **one item**, you must add a comma after the item, otherwise Python will not recognize it as a tuple:
> `single_item_tuple = ("Apple",)`

---

## Resources

- **Official Python Tuple Documentation** – https://docs.python.org/3/tutorial/datastructures.html#tuples
- **Real Python: Python Tuples** – https://realpython.com/python-tuples/
- **Corey Schafer: Python Tuples (YouTube)** – https://www.youtube.com/watch?v=W8KRzm-HU_I
- **GeeksforGeeks: Python Tuple** – https://www.geeksforgeeks.org/python-tuples/
- **Fluent Python (Book) – Chapter on Sequences** – https://www.oreilly.com/library/view/fluent-python/9781491946237/
