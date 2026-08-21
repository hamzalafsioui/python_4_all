# Vectors, Matrices, and NumPy Mechanics

This document explains the core mechanics of NumPy through examples. NumPy is the foundational library for numerical computing in Python, widely used in Data Science, Machine Learning, and AI.

---

## 1. Array Creation & Shapes

### 1D Vector

A vector is a one-dimensional array of numbers.

```python
vector = np.array([1, 2, 3, 4, 5])
```

**Output:**
```text
Vector:
[1 2 3 4 5]
Shape: (5,)
```

### 2D Matrix

A matrix is a two-dimensional array (rows and columns).

```python
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])
```

**Output:**
```text
Matrix:
[[1 2 3]
 [4 5 6]]
Shape: (2, 3)
```

### Initialization Shortcuts

NumPy provides fast ways to initialize arrays without typing out every element.

**Zeros Matrix:**

```python
zeros_mat = np.zeros((2, 3))
```

**Random Weights Matrix (Standard Normal Distribution):**

```python
random_mat = np.random.randn(3, 3)
```

---

## 2. Vectorization vs Python Loops

**Vectorization** is what makes NumPy fast. Under the hood, NumPy runs highly optimized C code instead of slow Python loops.

Let's multiply 5,000,000 random numbers by 5.

```python
size = 5_000_000
big_array = np.random.rand(size)
big_list = list(big_array)
```

### The Slow Way: Python Loop

```python
result_list = [x * 5 for x in big_list]
```

### The Fast Way: NumPy Vectorization

```python
result_array = big_array * 5
```

Vectorization applies the operation to the entire array at once. It is typically **50x to 100x faster** than a standard Python list comprehension.

---

## 3. Broadcasting Magic

**Broadcasting** allows NumPy to perform operations on arrays of different shapes by automatically "stretching" the smaller array to match the larger one.

```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60]]) # Shape (2, 3)
```

### Scalar Broadcasting

Adding a single number (scalar) to a matrix.

```python
matrix + 5
```

NumPy automatically adds 5 to *every single element*:

```text
[[15 25 35]
 [45 55 65]]
```

### Vector Broadcasting

Adding a 1D vector to a 2D matrix.

```python
vector = np.array([1, 2, 3]) # Shape (3,)
matrix + vector
```

NumPy stretches the vector `[1, 2, 3]` across all rows of the matrix:

```text
[[11 22 33]
 [41 52 63]]
```

---

## 4. Element-wise vs Matrix Multiplication

One of the most important distinctions in linear algebra and NumPy is between element-wise multiplication and true matrix multiplication (dot product).

```python
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 0],
              [1, 2]])
```

### Element-wise Multiplication (`*`)

Multiplies elements at the exact same positions.

```python
element_wise = A * B
```

**Output:**
```text
[[2 0]
 [3 8]]
```

Formula:

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix} * \begin{bmatrix} e & f \\ g & h \end{bmatrix} = \begin{bmatrix} a \times e & b \times f \\ c \times g & d \times h \end{bmatrix}
$$

### Matrix Multiplication (`@` or `np.dot`)

Follows the standard linear algebra rules of row-by-column dot products.

```python
dot_product = A @ B
```

**Output:**
```text
[[ 4  4]
 [10  8]]
```

Formula:

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix} @ \begin{bmatrix} e & f \\ g & h \end{bmatrix} = \begin{bmatrix} a \times e + b \times g & a \times f + b \times h \\ c \times e + d \times g & c \times f + d \times h \end{bmatrix}
$$

In AI and Deep Learning, `@` is heavily used for calculating neural network layer outputs (Weights $\times$ Inputs).
