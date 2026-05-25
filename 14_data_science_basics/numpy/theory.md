# NumPy: Numerical Python Basics

When working with Data Science, Machine Learning, or AI, Python's standard lists are simply too slow and memory-intensive. To process millions of data points efficiently, we use **NumPy** (Numerical Python).

---

## 1. What is NumPy?
NumPy is the fundamental package for scientific computing in Python.
- **The ndarray**: The core of NumPy is the **N-dimensional array** (an object that stores items of the same type in a contiguous block of memory).
- **Speed**: NumPy arrays are written in C, making mathematical operations up to **100x faster** than standard Python lists.
- **Vectorization**: Instead of writing `for` loops to perform operations on every item, you can perform math on the entire array at once!

---

## 2. Standard Lists vs. NumPy Arrays
| Feature | Python List | NumPy Array |
| :--- | :--- | :--- |
| **Data Types** | Can hold mixed types (strings, ints, dicts) | Must hold homogeneous types (e.g., all float64) |
| **Memory** | Highly fragmented (stores pointers to objects) | Highly compact (stores contiguous raw values) |
| **Operations** | Element-wise math requires explicit loops | Element-wise math is native (`arr * 2`) |
| **Dimensionality**| Nested lists | Native support for 1D, 2D (matrices), and N-D grids |

---

## 3. Basic Operations

### Array Creation
```python
import numpy as np

# From a list
arr = np.array([1, 2, 3, 4])

# Helper functions
zeros = np.zeros((3, 3))       # 3x3 matrix of zeros
ones = np.ones((2, 5))         # 2x5 matrix of ones
arange = np.arange(0, 10, 2)   # Array of [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)# 5 evenly spaced numbers: [0., 0.25, 0.5, 0.75, 1.]
```

### Array Indexing & Slicing
Slicing in NumPy is extremely powerful.
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0, 1])   # Row 0, Col 1 -> 2
print(arr[:, 1])   # All rows, Col 1 -> [2, 5]
```

### Broadcasting and Element-wise Math
```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)  # [11, 22, 33] (Element-wise addition)
print(a * 2)  # [2, 4, 6]    (Broadcasting scalar multiplication)
```

---

## 4. Fundamental Functions and Aggregations
- **`arr.shape`**: Returns a tuple showing the dimensions (e.g., `(3, 4)` for 3 rows, 4 columns).
- **`arr.reshape(rows, cols)`**: Changes the shape without modifying the data.
- **`arr.mean()`**: Computes the average value.
- **`arr.sum()`**: Sums all elements.
- **`arr.std()`**: Computes the standard deviation.

---

## 5. Best Practices
1. **Never loop over NumPy arrays**: If you write `for item in arr:`, you lose all the C-speed benefits of NumPy. Use vectorized expressions.
2. **Specify dtypes**: If you know your data is only small integers, specifying `dtype=np.int8` saves massive amounts of RAM.
3. **Avoid Copies (Be careful with Slices)**: Slicing an array creates a **view**, not a copy. If you modify a slice, the original array changes too! Use `.copy()` if you need an isolated copy.

## Resources

- **Official NumPy Documentation** – https://numpy.org/doc/stable/
- **NumPy Quickstart Tutorial** – https://numpy.org/doc/stable/user/quickstart.html
- **Real Python: NumPy Tutorial** – https://realpython.com/numpy-tutorial/
- **Stanford CS231n: Python NumPy Tutorial** – https://cs231n.github.io/python-numpy-tutorial/
- **From Python to NumPy (Book)** – https://www.labri.fr/perso/nrougier/from-python-to-numpy/
- **NumPy Illustrated (Visual Guide)** – https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
