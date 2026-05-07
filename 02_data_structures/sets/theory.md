# Python Sets

Sets are used to store multiple items in a single variable. They are unique among Python collections because they are **unordered** and contain **only unique** items.

---

## 1. What is a Set?
A set is a collection which is **unordered**, **unindexed**, and allows **no duplicate** members. Sets are written with curly brackets `{}`.

```python
my_set = {"apple", "banana", "cherry"}
```

---

## 2. Uniqueness
If you try to add a duplicate item to a set, Python will simply ignore it. This makes sets perfect for **removing duplicates** from a list.

```python
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers) # {1, 2, 3}
```

---

## 3. Basic Operations
- **Add**: `my_set.add("orange")`
- **Remove**: `my_set.remove("banana")` (raises error if not found)
- **Discard**: `my_set.discard("banana")` (no error if not found)
- **Pop**: Removes a random item (since sets are unordered).

---

## 4. Mathematical Set Operations
One of the most powerful features of sets is their ability to perform mathematical operations:

| Operation | Method / Operator | Description |
| :--- | :--- | :--- |
| **Union** | `s1.union(s2)` or `s1 \| s2` | All items from both sets. |
| **Intersection** | `s1.intersection(s2)` or `s1 & s2` | Only items present in both sets. |
| **Difference** | `s1.difference(s2)` or `s1 - s2` | Items in s1 but NOT in s2. |
| **Sym. Difference**| `s1.symmetric_difference(s2)` or `s1 ^ s2` | Items in either s1 or s2, but NOT both. |

---

## 5. Performance
Checking if an item is in a set (`"apple" in my_set`) is **extremely fast** (O(1) time complexity), regardless of how many millions of items are in the set.

---

> [!IMPORTANT]
> To create an **empty set**, you must use `set()`, not `{}`. Empty curly brackets `{}` create an empty **dictionary**.
