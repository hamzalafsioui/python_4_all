# The Collections Module: Beyond Basics

Python's built-in `list`, `dict`, and `tuple` are great, but sometimes you need something more specialized. The `collections` module provides "High-performance container datatypes" that make your code cleaner and more efficient.

---

## 1. NamedTuple: Tuples with Labels
A `namedtuple` is like a regular tuple but with field names. It's a great middle-ground between a tuple and a full Class.
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x) # Much clearer than p[0]!
```

---

## 2. Counter: The Automatic Tally
The `Counter` is a dictionary subclass specifically designed for counting items.
```python
from collections import Counter
c = Counter("mississippi")
print(c.most_common(2)) # [('i', 4), ('s', 4)]
```

---

## 3. DefaultDict: No More KeyError
A `defaultdict` automatically creates a default value if you try to access a key that doesn't exist.
```python
from collections import defaultdict
counts = defaultdict(int) # Default value is 0
counts['apples'] += 1     # No need to check if 'apples' exists!
```

---

## 4. Deque: The Fast Queue
A `deque` (Double-Ended Queue) is optimized for adding and removing items from **both ends**. It is significantly faster than a list for these operations.
```python
from collections import deque
q = deque(["a", "b", "c"])
q.appendleft("start")
q.pop() # Removes "c"
```

---

## 5. Why Use Collections?
1. **Performance**: `deque` is $O(1)$ for appends/pops at the start, whereas a list is $O(n)$.
2. **Readability**: `namedtuple` makes your data structures self-documenting.
3. **Productivity**: `Counter` and `defaultdict` remove boilerplate "check if key exists" code.

---

## 6. Best Practices
1. **Use NamedTuple for Data**: If you just need to store data without complex methods, use `namedtuple` instead of a class.
2. **Clean Loops**: Use `Counter` to simplify logic that counts frequencies.
3. **Queue Safety**: Use `deque(maxlen=10)` to automatically keep only the last 10 items (perfect for logs).

## Resources

- **Official Python collections Documentation** – https://docs.python.org/3/library/collections.html
- **Real Python: Python's collections Module** – https://realpython.com/python-collections-module/
- **Corey Schafer: Python Tutorial - Collections Module** – https://www.youtube.com/watch?v=cg3Z96-uQmA
- **Python Deque (Real Python)** – https://realpython.com/python-deque/
- **Effective Python (Book by Brett Slatkin)** – https://effectivepython.com/
