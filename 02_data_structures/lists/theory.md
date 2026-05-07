# Python Lists

Lists are one of the most powerful and flexible built-in data types in Python. They are used to store multiple items in a single variable.

---

## 1. What is a List?
A list is a collection which is **ordered**, **mutable** (changeable), and allows **duplicate** members.

```python
fruits = ["apple", "banana", "cherry"]
```

---

## 2. Indexing and Slicing
Lists are zero-indexed, meaning the first item has index `0`.

### Indexing
- `fruits[0]` -> "apple"
- `fruits[-1]` -> "cherry" (negative indexing starts from the end)

### Slicing
You can specify a range of indexes to get a sub-list.
`list[start:stop:step]`

```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[::2])   # [0, 2, 4]
```

---

## 3. List Methods
Python provides many built-in methods to manipulate lists:

| Method | Description |
| :--- | :--- |
| `.append(item)` | Adds an item to the end of the list. |
| `.insert(index, item)` | Adds an item at a specific position. |
| `.extend(iterable)` | Adds all elements of another list to the current list. |
| `.remove(item)` | Removes the first occurrence of a specific item. |
| `.pop(index)` | Removes and returns the item at a specific index (default is last). |
| `.sort()` | Sorts the list in ascending order. |
| `.reverse()` | Reverses the order of the list. |
| `.clear()` | Removes all items from the list. |

---

## 4. Mutability
Unlike strings, lists are **mutable**. You can change an item by referring to its index.

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits) # ["apple", "blueberry", "cherry"]
```

---

## 5. Nested Lists
Lists can contain other lists (multi-dimensional arrays).

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1]) # 2
```

---

> [!TIP]
> Use `len(my_list)` to find out how many items are in your list!
