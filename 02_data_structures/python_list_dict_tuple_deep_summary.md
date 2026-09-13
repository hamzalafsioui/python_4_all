# Python Deep Summary: List, Dict & Tuple

> **A complete reference**: how they work internally, every important method, problem-solving patterns 

---

## Table of Contents

1. [List: Deep Dive](#1-list-deep-dive)
2. [Dictionary: Deep Dive](#2-dictionary-deep-dive)
3. [Tuple: Deep Dive](#3-tuple-deep-dive)
4. [Comparison Table](#4-comparison-table)
5. [How Python Stores Them Internally](#5-how-python-stores-them-internally)
6. [Problem-Solving Patterns and Strategies](#6-problem-solving-patterns-and-strategies)
7. [Solved Problems from Your Notebooks](#7-solved-problems-from-your-notebooks)
8. [Common Mistakes and Gotchas](#8-common-mistakes-and-gotchas)
9. [Quick Cheat Sheet](#9-quick-cheat-sheet)

---

## 1. List: Deep Dive

### 1.1 What Is a List?

A list is an **ordered, mutable, heterogeneous** collection of items.

```python
# Creating lists
empty       = []
numbers     = [1, 2, 3, 4, 5]
mixed       = ["hello", 42, 3.14, True, [1, 2]]
from_range  = list(range(10))        # [0, 1, 2, ..., 9]
from_string = list("Python")         # ['P', 'y', 't', 'h', 'o', 'n']
```

**Why use lists?**
- When order matters.
- When you need to add/remove items frequently.
- When you need duplicate values.

---

### 1.2 How a List Works Internally (CPython)

Under the hood, a Python list is **not** a linked list. It is a **dynamic array**, a contiguous block of memory holding **pointers** to Python objects.

```
List object
┌──────────────────────────────┐
│  ob_refcnt   (reference cnt) │
│  ob_type     (→ list type)   │
│  ob_size     (length = 5)    │
│  allocated   (capacity = 8)  │  ← may be larger than ob_size
│  ob_item     ─────────────┐  │
└──────────────────────────────┘
                             │
                             ▼
               ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
   C array →   │ ptr │ ptr │ ptr │ ptr │ ptr │ --- │ --- │ --- │
               └──┬──┴──┬──┴──┬──┴──┬──┴──┬──┴─────┴─────┴─────┘
                  ▼     ▼     ▼     ▼     ▼
                 10    20    30    40    50   (actual Python int objects)
```

**Key points:**
| Operation | Time Complexity | Why |
|---|---|---|
| `lst[i]` (index) | **O(1)** | Direct pointer offset: `base_addr + i * sizeof(ptr)` |
| `lst.append(x)` | **O(1)** amortized | If capacity available, just set pointer. If not, reallocate (grow by ~12.5%) |
| `lst.insert(0, x)` | **O(n)** | Must shift every pointer one position right |
| `lst.pop()` | **O(1)** | Remove last pointer |
| `lst.pop(0)` | **O(n)** | Must shift every pointer one position left |
| `x in lst` | **O(n)** | Linear scan (no hash table) |
| `lst.sort()` | **O(n log n)** | Timsort (hybrid merge + insertion sort) |

**Over-allocation strategy:** When the array is full and you `append`, Python allocates extra space (roughly `new_size = old_size + (old_size >> 3) + 6`). This is why `append` is O(1) *amortized*: most calls are instant, occasional ones trigger reallocation.

---

### 1.3 All List Methods Explained

#### Adding Elements

```python
lst = [1, 2, 3]

# append(x) → adds to the END, O(1) amortized
lst.append(4)           # [1, 2, 3, 4]

# insert(i, x) → adds at index i, O(n) because of shifting
lst.insert(0, 0)        # [0, 1, 2, 3, 4]
lst.insert(2, 99)       # [0, 1, 99, 2, 3, 4]

# extend(iterable) → adds ALL items from iterable, O(k) where k = len(iterable)
lst.extend([5, 6, 7])   # [0, 1, 99, 2, 3, 4, 5, 6, 7]
# Same as: lst += [5, 6, 7]
```

> **Why `extend` and not `append` for multiple items?**
> `lst.append([5, 6])` adds the list *as one element*: `[..., [5, 6]]`.
> `lst.extend([5, 6])` adds each element individually: `[..., 5, 6]`.

#### Removing Elements

```python
lst = [10, 20, 30, 20, 40]

# remove(x) → removes FIRST occurrence of x, O(n)
lst.remove(20)          # [10, 30, 20, 40]

# pop(i) → removes and RETURNS item at index i (default: last), O(1) for last, O(n) for first
val = lst.pop()         # val = 40, lst = [10, 30, 20]
val = lst.pop(0)        # val = 10, lst = [30, 20]

# clear() → removes ALL elements, O(1)
lst.clear()             # []

# del statement
lst = [1, 2, 3, 4, 5]
del lst[2]              # [1, 2, 4, 5]
del lst[1:3]            # [1, 5]
```

#### Searching & Counting

```python
lst = [7, 23, 5, 23, 7, 19, 23, 12, 29]

# index(x) → returns FIRST index of x, raises ValueError if not found
lst.index(23)           # 1

# count(x) → counts occurrences of x, O(n)
lst.count(23)           # 3

# 'in' operator → boolean check, O(n)
23 in lst               # True
99 in lst               # False
```

#### Sorting & Reversing

```python
lst = [3, 1, 4, 1, 5, 9]

# sort() → sorts IN-PLACE, returns None, O(n log n) (Timsort)
lst.sort()              # [1, 1, 3, 4, 5, 9]
lst.sort(reverse=True)  # [9, 5, 4, 3, 1, 1]
lst.sort(key=lambda x: -x)  # same as reverse=True

# sorted() → returns a NEW sorted list, original unchanged
new_lst = sorted(lst)

# reverse() → reverses IN-PLACE, O(n)
lst.reverse()

# reversed() → returns an iterator (lazy), doesn't modify original
for item in reversed(lst):
    print(item)
```

> **`sort()` vs `sorted()`:**
> - `sort()` modifies the list in-place, returns `None`. Faster (no copy).
> - `sorted()` returns a new list. Original is untouched. Works on any iterable.

#### Copying

```python
lst = [1, [2, 3], 4]

# Shallow copy: new list, but inner objects are shared
copy1 = lst.copy()        # or lst[:]  or list(lst)
copy1[0] = 99             # lst is unchanged
copy1[1][0] = 99          # Warning: lst[1][0] is ALSO changed! (shared reference)

# Deep copy: fully independent copy
import copy
copy2 = copy.deepcopy(lst)
copy2[1][0] = 999         # lst is unchanged [OK]
```

---

### 1.4 List Comprehensions

The most Pythonic way to create and transform lists.

```python
# Basic: [expression for item in iterable]
squares = [x**2 for x in range(10)]          # [0, 1, 4, 9, ..., 81]

# With filter: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0] # [0, 2, 4, ..., 18]

# Nested
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]    # [1, 2, 3, 4, 5, 6]

# With transformation + filter
notes = [12, 32, 34, 1, 56, 8, 4, 2, 12]
moyen = sum(notes) / len(notes)
above_avg = [n for n in notes if n > moyen]  # Notes above average
```

---

### 1.5 Functional Tools: `map()`, `filter()`, `reduce()`

```python
numbers = [1, 2, 3, 4, 5]

# map(function, iterable) → applies function to every element
doubled = list(map(lambda x: x * 2, numbers))    # [2, 4, 6, 8, 10]

# filter(function, iterable) → keeps only elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# reduce(function, iterable, initial) → accumulates into single value
from functools import reduce
total = reduce(lambda x, y: x + y, numbers, 0)  # 15
```

> **When to use what?**
> - Use **list comprehension** for simple transformations/filters (more readable).
> - Use **`map()`/`filter()`** when you have an existing named function to apply.
> - Use **`reduce()`** for fold operations (sum, product, etc.).

---

### 1.6 Slicing

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst[2:5]      # [2, 3, 4]          (from index 2 to 4, 5 excluded)
lst[:3]       # [0, 1, 2]          (first 3 elements)
lst[7:]       # [7, 8, 9]          (from index 7 to end)
lst[::2]      # [0, 2, 4, 6, 8]   (every 2nd element)
lst[::-1]     # [9, 8, 7, ..., 0]  (reversed)
lst[1:7:2]    # [1, 3, 5]          (from 1 to 6, step 2)

# Slice assignment (replace a portion)
lst[2:5] = [20, 30]  # [0, 1, 20, 30, 5, 6, 7, 8, 9]
```

---

## 2. Dictionary: Deep Dive

### 2.1 What Is a Dictionary?

A dictionary is an **unordered** (insertion-ordered since Python 3.7+), **mutable** collection of **key-value pairs**. Keys must be **hashable** (immutable).

```python
# Creating dictionaries
empty  = {}
person = {"nom": "Ali", "age": 25, "ville": "Ouled_Teima"}
from_zip   = dict(zip(["a", "b", "c"], [1, 2, 3]))     # {'a': 1, 'b': 2, 'c': 3}
from_comp  = {x: x**2 for x in range(5)}                # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
from_keys  = dict.fromkeys(["a", "b", "c"], 0)           # {'a': 0, 'b': 0, 'c': 0}
```

---

### 2.2 How a Dictionary Works Internally (Hash Table)

A Python dict is a **hash table**, one of the most important data structures in computer science.

#### The Process: How `d[key] = value` Works

```
Step 1: Compute hash
   hash("nom") → 7065939384614856067  (a big integer)

Step 2: Compute index into the internal array
   index = hash_value % table_size    (e.g., 7065939384614856067 % 8 = 3)

Step 3: Store at that slot
   table[3] → (hash, key_ptr, value_ptr)

Step 4: On lookup d["nom"], repeat steps 1-2, then compare key at that slot
```

#### Hash Collisions

When two different keys produce the same index, it's called a **collision**. Python uses **open addressing with probing**: it looks for the next available slot.

```
table_size = 8

hash("nom")  % 8 = 3  → slot 3 [OK]
hash("age")  % 8 = 3  → slot 3 occupied! → probe → slot 4 [OK]
hash("ville")% 8 = 5  → slot 5 [OK]
```

#### Performance

| Operation | Average | Worst Case | Why |
|---|---|---|---|
| `d[key]` | **O(1)** | O(n) | Hash → index → compare. Worst = all keys collide |
| `d[key] = val` | **O(1)** | O(n) | Same as above |
| `del d[key]` | **O(1)** | O(n) | Same as above |
| `key in d` | **O(1)** | O(n) | Hash lookup (not a linear scan like lists) |
| `len(d)` | **O(1)** | O(1) | Stored as attribute |

> **This is why `key in dict` is O(1) but `item in list` is O(n).**
> The dict uses a hash table; the list does a linear scan.

#### Why Must Keys Be Hashable (Immutable)?

If a key's hash could change after insertion, we'd never find it again. That's why:
- `str`, `int`, `float`, `bool`, `tuple` (of hashables), `frozenset` → **hashable**
- `list`, `dict`, `set` → **NOT hashable** (mutable, hash could change)

---

### 2.3 All Dictionary Methods Explained

#### Accessing Values

```python
d = {"nom": "Ali", "age": 25, "ville": "Ouled_Teima"}

# d[key] → raises KeyError if key doesn't exist
d["nom"]             # "Ali"
# d["email"]         # KeyError: 'email'

# get(key, default=None) → safe access, returns default if key missing
d.get("nom")         # "Ali"
d.get("email")       # None (no error)
d.get("email", "N/A")# "N/A"
```

> **Always prefer `get()` over `d[key]`** when the key might not exist. It avoids crashes.

#### Adding / Updating

```python
d = {"a": 1, "b": 2}

# Direct assignment
d["c"] = 3                    # adds new: {'a': 1, 'b': 2, 'c': 3}
d["a"] = 10                   # updates: {'a': 10, 'b': 2, 'c': 3}

# update(other_dict) → merges another dict into this one
d.update({"b": 20, "d": 4})  # {'a': 10, 'b': 20, 'c': 3, 'd': 4}

# setdefault(key, default) → if key exists, return its value. If not, SET it and return default
d.setdefault("e", 5)          # adds 'e': 5, returns 5
d.setdefault("a", 999)        # 'a' already exists, returns 10 (unchanged)

# Merge operator (Python 3.9+)
merged = d | {"f": 6}         # new dict with all keys
d |= {"g": 7}                 # in-place merge
```

#### Removing

```python
d = {"a": 1, "b": 2, "c": 3}

# pop(key, default) → removes and returns value. KeyError if no default and key missing
val = d.pop("b")              # val = 2, d = {'a': 1, 'c': 3}
val = d.pop("z", None)        # val = None, no error

# popitem() → removes and returns last inserted (key, value) pair
item = d.popitem()            # ('c', 3)

# del d[key]
del d["a"]                    # d = {}

# clear()
d.clear()                     # {}
```

#### Iterating

```python
d = {"nom": "Ali", "age": 25, "ville": "Ouled_Teima"}

# keys() → view of all keys
list(d.keys())      # ['nom', 'age', 'ville']

# values() → view of all values
list(d.values())    # ['Ali', 25, 'Ouled_Teima']

# items() → view of (key, value) tuples
list(d.items())     # [('nom', 'Ali'), ('age', 25), ('ville', 'Ouled_Teima')]

# Looping: most common patterns
for key in d:                      # iterate over keys (default)
    print(key, d[key])

for key, value in d.items():       # iterate over key-value pairs (BEST)
    print(f"{key}: {value}")
```

---

### 2.4 Dictionary Comprehensions

```python
# Basic
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With filter
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys and values
d = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in d.items()}  # {1: 'a', 2: 'b', 3: 'c'}

# Partition a dict (from your notebook challenge)
notes_eleves = {"Amine": 15.5, "Yassine": 19.0, "Malak": 8.7, "Ahmed": 7.5}
admis     = {k: v for k, v in notes_eleves.items() if v >= 10}
non_admis = {k: v for k, v in notes_eleves.items() if v < 10}
```

---

## 3. Tuple: Deep Dive

### 3.1 What Is a Tuple?

A tuple is an **ordered, immutable** collection. Once created, its contents **cannot be changed**.

```python
# Creating tuples
empty       = ()
single      = (42,)            # Note: Comma is required for single element!
student     = ("Yasmine", 22, "Informatique", 17.4)
from_list   = tuple([1, 2, 3])
nested      = (1, (2, 3), (4, 5, 6))
```

> **Why the comma for single elements?**
> `(42)` is just the integer `42` in parentheses. `(42,)` is a tuple.

---

### 3.2 How a Tuple Works Internally

A tuple is stored as a **fixed-size C array** of pointers, exactly like a list, but without any resizing machinery.

```
Tuple object
┌──────────────────────────────┐
│  ob_refcnt   (reference cnt) │
│  ob_type     (→ tuple type)  │
│  ob_size     (length = 4)    │
│  ob_item     ─────────────┐  │  ← NO 'allocated' field (no over-allocation)
└──────────────────────────────┘
                             │
                             ▼
               ┌──────┬──────┬──────┬──────┐
   C array →   │ ptr  │ ptr  │ ptr  │ ptr  │
               └──┬───┴──┬───┴──┬───┴──┬───┘
                  ▼      ▼      ▼      ▼
              "Yasmine"  22  "Info"   17.4
```

**Differences from list internally:**
| Feature | List | Tuple |
|---|---|---|
| Over-allocation | Yes (capacity > length) | No (capacity == length) |
| Resize support | Yes (`append`, `insert`, etc.) | No |
| Memory | ~56 bytes + 8/element | ~40 bytes + 8/element |
| Free list cache | No | Yes (small tuples are cached and reused) |

**Performance:**
| Operation | Time | Notes |
|---|---|---|
| `t[i]` | O(1) | Same as list |
| `x in t` | O(n) | Same as list (linear scan) |
| Creating | Faster than list | Less overhead, small tuples cached |
| Iteration | Slightly faster | Contiguous memory, no mutation checks |

> **Tuples are ~10-20% faster than lists** for creation and iteration because they're simpler internally.

---

### 3.3 Tuple Operations

```python
t = ("Yasmine", 22, "Informatique", 17.4)

# Indexing: same as list
t[0]                # "Yasmine"
t[-1]               # 17.4

# Slicing: returns a new tuple
t[0:2]              # ("Yasmine", 22)

# Concatenation: creates a new tuple
t2 = t + ("Très Bien", 2024)
# ("Yasmine", 22, "Informatique", 17.4, "Très Bien", 2024)

# Repetition
t3 = (1, 2) * 3    # (1, 2, 1, 2, 1, 2)

# Unpacking
name, age, field, avg = t
print(name)         # "Yasmine"

# Extended unpacking
first, *rest = t
# first = "Yasmine", rest = [22, "Informatique", 17.4]

# count() and index()
t = (1, 2, 3, 2, 4, 2)
t.count(2)          # 3
t.index(2)          # 1 (first occurrence)

# Immutability
# t[0] = "Ali"      # TypeError: 'tuple' object does not support item assignment
```

---

### 3.4 When to Use Tuples vs Lists

| Use Tuple When... | Use List When... |
|---|---|
| Data shouldn't change (coordinates, DB rows) | You need to add/remove items |
| You need a dictionary key | You're building a collection dynamically |
| Returning multiple values from a function | Order may need sorting |
| Slightly better performance matters | You need `append`, `sort`, etc. |

```python
# Tuple as dict key (because it's hashable)
locations = {
    (48.8566, 2.3522): "Paris",
    (34.0522, -118.2437): "Los Angeles"
}

# Returning multiple values
def min_max(lst):
    return (min(lst), max(lst))    # returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5, 9])  # lo=1, hi=9
```

---

### 3.5 Named Tuples: Self-Documenting Tuples

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "field", "average"])
s = Student("Yasmine", 22, "Informatique", 17.4)

s.name      # "Yasmine"  (much more readable than s[0])
s.average   # 17.4
s[0]        # Still works: "Yasmine"
```

---

## 4. Comparison Table

| Feature | List | Dict | Tuple |
|---|---|---|---|
| **Syntax** | `[1, 2, 3]` | `{"a": 1}` | `(1, 2, 3)` |
| **Ordered** | Yes | Yes (3.7+) | Yes |
| **Mutable** | Yes | Yes | No |
| **Duplicates** | Allowed | Keys unique | Allowed |
| **Indexed** | By position | By key | By position |
| **Hashable** | No | No | Yes* |
| **Lookup speed** | O(n) | **O(1)** | O(n) |
| **Memory** | Medium | Highest | Lowest |
| **Use case** | Ordered collections | Key-value mapping | Fixed records |

\* *Only if all elements are hashable*

---

## 5. How Python Stores Them Internally

### Memory Layout Summary

```
╔══════════════╦════════════════════════════════════════════╗
║  Structure   ║  Internal Implementation                  ║
╠══════════════╬════════════════════════════════════════════╣
║  list        ║  Dynamic array of pointers                ║
║              ║  Over-allocates for amortized O(1) append ║
╠══════════════╬════════════════════════════════════════════╣
║  dict        ║  Hash table (open addressing)             ║
║              ║  Separate dense + sparse arrays (3.6+)    ║
╠══════════════╬════════════════════════════════════════════╣
║  tuple       ║  Fixed-size array of pointers             ║
║              ║  Small tuples cached in free list         ║
╚══════════════╩════════════════════════════════════════════╝
```

### Measuring Memory

```python
import sys

lst = [1, 2, 3, 4, 5]
tpl = (1, 2, 3, 4, 5)
dct = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

print(sys.getsizeof(lst))  # ~96 bytes
print(sys.getsizeof(tpl))  # ~80 bytes
print(sys.getsizeof(dct))  # ~232 bytes
```

---

## 6. Problem-Solving Patterns and Strategies

### Pattern 1: Frequency Counting

**Problem:** Count occurrences of each element.

```python
# Simple but slow: O(n²)
def count_manual(lst):
    result = {}
    for item in lst:
        count = 0
        for x in lst:
            if x == item:
                count += 1
        result[item] = count
    return result

# Better: O(n) using dict
def count_with_dict(lst):
    result = {}
    for item in lst:
        result[item] = result.get(item, 0) + 1
    return result
# WHY: get(item, 0) returns 0 if key doesn't exist, avoiding KeyError.
# Each element is visited once → O(n).

# Best: O(n) using Counter
from collections import Counter
counter = Counter(lst)
# WHY: Built-in, optimized in C, handles edge cases, supports arithmetic.
```

### Pattern 2: Finding Duplicates

```python
# Simple: O(n²)
def find_duplicates_naive(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates

# Better: O(n) with set
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
# WHY: set lookup is O(1), so total is O(n) instead of O(n²).
```

### Pattern 3: Partitioning / Grouping

**Problem:** Split a collection into groups based on a condition.

```python
# Simple: two loops
def partition_simple(lst, predicate):
    yes = []
    no = []
    for item in lst:
        if predicate(item):
            yes.append(item)
        else:
            no.append(item)
    return yes, no
# WHY: Clear and readable. One pass through the data → O(n).

# Best: using filter (from your notebook)
def partition_filter(lst, critere):
    satisfaits = list(filter(critere, lst))
    non_satisfaits = list(filter(lambda x: not critere(x), lst))
    return satisfaits, non_satisfaits
# WHY: Functional style. BUT iterates twice → 2*O(n). Still O(n).
# For truly large data, the simple version is better (single pass).
```

### Pattern 4: Two-Pointer / Complement with Set

**Problem:** Find pairs that sum to a target.

```python
# Brute force: O(n²)
def find_pair_naive(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (lst[i], lst[j])
    return None

# Best: O(n) with set
def find_pair_set(lst, target):
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None
# WHY: For each number, we check if (target - number) was already seen.
# Set lookup is O(1) → total O(n).
```

### Pattern 5: Dict as Cache / Memoization

```python
# Fibonacci: exponential without cache
def fib_slow(n):
    if n <= 1: return n
    return fib_slow(n-1) + fib_slow(n-2)  # O(2^n) (slow)

# With dict cache: O(n)
def fib_fast(n, cache={}):
    if n in cache: return cache[n]
    if n <= 1: return n
    cache[n] = fib_fast(n-1, cache) + fib_fast(n-2, cache)
    return cache[n]
# WHY: Each fib(k) computed only once, stored in dict for O(1) lookup.
```

### Pattern 6: Flatten Nested Structures

```python
# Recursive flatten (from your notebook)
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Example
flatten([1, [2, 3, [4, 5]], 6])  # [1, 2, 3, 4, 5, 6]
# WHY: isinstance() checks if element is a list → recurse deeper.
# extend() adds all flattened elements. Works for any nesting depth.
```

### Pattern 7: Zip for Parallel Iteration

```python
keys = ["nom", "age", "ville"]
values = ["Ali", 25, "Ouled_Teima"]

# Create dict from two lists
result = dict(zip(keys, values))   # {'nom': 'Ali', 'age': 25, 'ville': 'Ouled_Teima'}

# Iterate in parallel
for k, v in zip(keys, values):
    print(f"{k}: {v}")

# Unzip
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)    # ('a', 'b', 'c'), (1, 2, 3)
```

### Pattern 8: Grouping with defaultdict

```python
from collections import defaultdict

# Group students by grade range
students = [("Alice", 85), ("Bob", 72), ("Charlie", 91), ("Diana", 68)]

groups = defaultdict(list)
for name, grade in students:
    if grade >= 80:
        groups["excellent"].append(name)
    elif grade >= 70:
        groups["good"].append(name)
    else:
        groups["needs_improvement"].append(name)

# {'excellent': ['Alice', 'Charlie'], 'good': ['Bob'], 'needs_improvement': ['Diana']}
# WHY: defaultdict(list) auto-creates an empty list for new keys.
# No need for setdefault() or checking if key exists.
```

### Pattern 9: Enumerate for Index + Value

```python
fruits = ["pomme", "banana", "orange", "kiwi"]

# Avoid in Python (C-style indexing)
for i in range(len(fruits)):
    print(i, fruits[i])

# Pythonic
for i, fruit in enumerate(fruits):
    print(i, fruit)

# With start index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# WHY: enumerate() returns (index, value) tuples: clean and readable.
```

---

## 7. Solved Problems from Your Notebooks

### Problem 1: Notes Above Average (from Listes.ipynb)

**Task:** Extract all grades above the average.

```python
notes = [12, 32, 34, 1, 56, 8, 4, 2, 12]

# --- Simple Solution (loop) ---
moyen = sum(notes) / len(notes)
notes_supp = []
for note in notes:
    if note > moyen:
        notes_supp.append(note)
# WHY: Straightforward. Calculate average first, then filter.
# Time: O(n) for sum + O(n) for loop = O(n).

# --- Best Solution (list comprehension) ---
moyen = sum(notes) / len(notes)
notes_supp = [n for n in notes if n > moyen]
# WHY: Same logic, one line. Comprehensions are ~30% faster than
# equivalent for-loops because they're optimized in CPython bytecode.
```

---

### Problem 2: Common Words (from Listes.ipynb)

**Task:** Find common words between two strings.

```python
ch1 = "python is languague more popular than vb"
ch2 = "c# is a languague oop and compiler language"

# --- Simple Solution (loop) --- O(n*m)
words_1 = ch1.split()
words_2 = ch2.split()
common_words = []
for word in words_1:
    if word in words_2 and word not in common_words:
        common_words.append(word)
# WHY: 'word in words_2' is O(m) for each word → total O(n*m).
# 'word not in common_words' prevents duplicates.

# --- Best Solution (set intersection) --- O(n+m)
common_words = list(set(words_1) & set(words_2))
# WHY: Converting to set is O(n) + O(m). Set intersection is O(min(n,m)).
# Total: O(n + m) instead of O(n * m). MUCH faster for large inputs.
# Note: set loses original order.
```

---

### Problem 3: Search Element (from Listes.ipynb)

**Task:** Return index of element, or False if not found.

```python
# --- Simple Solution ---
def rechercheElement(item, items):
    for i in range(len(items)):
        if items[i] == item:
            return i
    return False
# WHY: Manual search with index tracking. O(n).

# --- Best Solution ---
def rechercheElement(item, items):
    if item in items:
        return items.index(item)
    return False
# WHY: Cleaner. 'in' check is O(n), index() is O(n) → still O(n) total.
# But reads more naturally.

# --- Alternative with try/except ---
def rechercheElement(item, items):
    try:
        return items.index(item)
    except ValueError:
        return False
# WHY: Only one traversal when element exists. More "Pythonic" (EAFP style).
```

---

### Problem 4: Count Occurrences Without Built-ins (from Listes.ipynb)

```python
# --- Simple Solution (your notebook) --- O(n)
def countOccurrences(element, L):
    count = 0
    for item in L:
        if item == element:
            count += 1
    return count
# WHY: Required by the challenge (no built-in functions).
# Manual counting with loop. Clean and efficient O(n).

# --- Built-in Solution --- O(n)
L = [7, 23, 5, 23, 7, 19, 23, 12, 29]
L.count(23)   # 3
# WHY: Same complexity but implemented in C → faster.

# --- Count ALL occurrences at once --- O(n)
from collections import Counter
counter = Counter(L)  # {23: 3, 7: 2, 5: 1, 19: 1, 12: 1, 29: 1}
# WHY: One pass counts everything. Perfect when you need multiple lookups.
```

---

### Problem 5: Advanced Filter with Lambda (from Listes_avance.ipynb)

```python
# --- Clean and Correct Solution ---
def filtrer_liste(liste, critere):
    return list(filter(critere, liste))

filtrer_liste([1, 12, 9, 15, 20, 3], lambda x: x > 10)   # [12, 15, 20]
filtrer_liste([1, 12, 9, 15, 20, 3], lambda x: x % 3 == 0) # [12, 9, 15, 3]
# WHY: filter() is lazy (iterator), list() materializes it.
# Passing the criterion as a parameter makes the function reusable.

# --- Alternative with comprehension ---
def filtrer_liste(liste, critere):
    return [x for x in liste if critere(x)]
# WHY: Comprehension is often faster and more readable for simple cases.
```

---

### Problem 6: Merge Dicts with Custom Fusion (from dic_tuples_avancer.ipynb)

```python
# --- Solution ---
def fusionner_dictionnaires(dict1, dict2, fusion_func):
    result = dict1.copy()           # Preserve original
    for key, value in dict2.items():
        if key in result:
            result[key] = fusion_func(result[key], value)  # Apply custom merge
        else:
            result[key] = value     # Add new key
    return result

# Test
fusionner_dictionnaires({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, lambda x, y: x + y)
# {'a': 1, 'b': 5, 'c': 4}
# WHY: dict1.copy() avoids modifying original.
# The fusion_func parameter makes it flexible (sum, max, min, concat...).
```

---

### Problem 7: Flatten Nested Dict (from dic_tuples_avancer.ipynb)

```python
# --- Note on Notebook Bug: checked isinstance(v, tuple) instead of dict ---

# --- Corrected and Best Solution ---
def aplatir_dictionnaire(dicts, prefix=""):
    result = []
    for k, v in dicts.items():
        new_key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):                          # ← must check for dict, not tuple
            result.extend(aplatir_dictionnaire(v, new_key))  # recurse
        else:
            result.append((new_key, v))
    return result

D = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print(aplatir_dictionnaire(D))
# [('a', 1), ('b.c', 2), ('b.d.e', 3)]
# WHY: Recursion handles arbitrary nesting depth.
# Prefix concatenation builds the dotted key path.
```

---

### Problem 8: Recursive Transformation (from Listes_avance.ipynb)

```python
# --- Solution 1: Explicit Loop ---
def transformer_imbriquee(liste, transformation):
    resultat = []
    for element in liste:
        if isinstance(element, list):
            resultat.append(transformer_imbriquee(element, transformation))
        else:
            resultat.append(transformation(element))
    return resultat
# WHY: isinstance() check determines recursion. Structure is preserved.

# --- Solution 2: map() one-liner ---
def transform(li, fn):
    return list(map(lambda x: transform(x, fn) if isinstance(x, list) else fn(x), li))
# WHY: Same logic compressed. map() applies the lambda to each element.
# The lambda itself recurses when it finds a sub-list.
# Note: Less readable for beginners. Solution 1 is better for learning.

transformer_imbriquee([1, [2, 3, [4, 5]], 6], lambda x: x * 2)
# [2, [4, 6, [8, 10]], 12]
```

---

### Problem 9: Custom Reduce Without `functools` (from Listes_avance.ipynb)

```python
# --- Solution ---
def reduire_list(lst, operation, valeur_initial):
    result = valeur_initial
    for element in lst:
        result = operation(result, element)
    return result

reduire_list([1, 2, 3, 4], lambda x, y: x + y, 0)   # 10 (sum)
reduire_list([1, 2, 3, 4], lambda x, y: x * y, 1)   # 24 (product)
# WHY: Accumulator pattern. Start with initial value, apply operation
# with each element. This IS how functools.reduce works internally.
# Using 0 for sum (identity element for +) and 1 for product (identity for *).
```

---

## 8. Common Mistakes and Gotchas

### Mistake 1: Modifying a list while iterating

```python
# WRONG: skips elements, unpredictable behavior
lst = [1, 2, 3, 4, 5]
for item in lst:
    if item % 2 == 0:
        lst.remove(item)   # Modifying during iteration!

# CORRECT: iterate over a copy, or use comprehension
lst = [x for x in lst if x % 2 != 0]
```

### Mistake 2: Mutable default arguments

```python
# WRONG: the list is shared across all calls!
def add_item(item, lst=[]):
    lst.append(item)
    return lst

add_item(1)   # [1]
add_item(2)   # [1, 2]  ← unexpected!

# CORRECT
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### Mistake 3: Shallow copy surprise

```python
# Both point to the same inner list
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]]  ← modified!

# Use deepcopy for nested structures
import copy
deep = copy.deepcopy(original)
```

### Mistake 4: `is` vs `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b    # True  (same content)
a is b    # False (different objects in memory)

# 'is' checks identity (same object), '==' checks equality (same value)
```

### Mistake 5: Using list as dict key

```python
# TypeError: unhashable type: 'list'
d = {[1, 2]: "value"}

# Convert to tuple
d = {(1, 2): "value"}
```

### Mistake 6: Forgetting that `sort()` returns None

```python
# WRONG: result is None
result = [3, 1, 2].sort()   # result = None!

# CORRECT
lst = [3, 1, 2]
lst.sort()                   # lst is now [1, 2, 3]

# OR use sorted()
result = sorted([3, 1, 2])  # result = [1, 2, 3]
```

### Mistake 7: Dict key overwriting

```python
# Note: Second 'a' silently overwrites the first
d = {"a": 1, "b": 2, "a": 3}
print(d)  # {'a': 3, 'b': 2}
# No error! The last value wins.
```

---

## 9. Quick Cheat Sheet

### List

```python
lst = [1, 2, 3]
lst.append(4)            # Add to end
lst.insert(0, 0)         # Add at index
lst.extend([5, 6])       # Add multiple
lst.remove(3)            # Remove by value
lst.pop()                # Remove last
lst.pop(0)               # Remove first
lst.sort()               # Sort in-place
lst.reverse()            # Reverse in-place
lst.index(2)             # Find index
lst.count(2)             # Count occurrences
len(lst)                 # Length
lst[1:3]                 # Slice
lst[::-1]                # Reversed copy
[x**2 for x in lst]      # Comprehension
```

### Dict

```python
d = {"a": 1, "b": 2}
d["c"] = 3               # Add / Update
d.get("x", 0)            # Safe access
d.pop("a")               # Remove by key
d.update({"d": 4})       # Merge
d.setdefault("e", 5)     # Set if missing
d.keys()                 # All keys
d.values()               # All values
d.items()                # All (key, value) pairs
del d["b"]               # Delete key
len(d)                   # Size
"a" in d                 # Check key exists (O(1)!)
{k: v for k, v in d.items() if v > 1}  # Comprehension
```

### Tuple

```python
t = (1, 2, 3)
t[0]                     # Index access
t[1:3]                   # Slice
t + (4, 5)               # Concatenate (new tuple)
t * 2                    # Repeat
len(t)                   # Length
t.count(2)               # Count
t.index(2)               # Find index
a, b, c = t              # Unpack
a, *rest = t             # Extended unpack
```

---

> **Remember:** Choose `list` for dynamic collections, `dict` for fast lookups by key, and `tuple` for fixed, lightweight records. Understanding their internals helps you write code that's not just correct, but **fast**.
