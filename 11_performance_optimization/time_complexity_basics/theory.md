# Time Complexity Basics: Writing Scalable Code

As a developer, it's not enough to write code that *works*; you must write code that is *efficient*. **Time Complexity** (often described using **Big O Notation**) is the language we use to measure how well our code performs as the amount of data grows.

---

## 1. What is Big O Notation?
Big O tells us how the execution time of an algorithm increases as the input size ($n$) increases. It ignores small details (like the speed of your CPU) and focuses on the "shape" of the growth.

---

## 2. Common Time Complexities

### $O(1)$ - Constant Time
The fastest possible. The time is always the same, regardless of how much data you have.
- **Example**: Accessing an item in a list by index or a dictionary by key.

### $O(n)$ - Linear Time
The time grows proportionally to the data. If you have 10x more data, it takes 10x longer.
- **Example**: A single `for` loop, or `if x in my_list`.

### $O(n^2)$ - Quadratic Time
The "Performance Killer." If you have 10x more data, it takes **100x** longer.
- **Example**: Nested for loops (a loop inside a loop).

### $O(\log n)$ - Logarithmic Time
Very efficient. Even with millions of items, it only takes a few steps.
- **Example**: Binary Search.

---

## 3. Lists vs. Sets: The Big Lesson
One of the most important performance tips in Python:
- Searching a **List** is $O(n)$.
- Searching a **Set** (or Dict) is $O(1)$.
If you have 1 million items, the list search might take seconds, while the set search takes microseconds.

---

## 4. How to Measure Performance
You can use Python's `time` module to see how long a function takes.

```python
import time
start = time.time()
# ... run code ...
end = time.time()
print(f"Time taken: {end - start}s")
```

---

## 5. Best Practices
1. **Avoid Nested Loops**: If you see a loop inside a loop, ask yourself: "Can I use a dictionary or set to make this $O(n)$?"
2. **Choose the Right Tool**: Use a list for ordered data, but use a set if you need to check "Is this item here?" frequently.
3. **Don't Optimize Too Early**: Write clean code first. Only optimize the parts that are actually slow (use profiling to find them).
