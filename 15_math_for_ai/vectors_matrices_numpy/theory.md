# Vectors and Matrices with NumPy

While our previous Linear Algebra module covered mathematical formulas, this module focuses strictly on the computational engine that makes AI possible: **NumPy Arrays**. In Python, NumPy is the gold standard for high-performance vector and matrix calculations.

---

## 1. Tensors, Matrices, and Vectors

In Machine Learning, data is organized into structures of varying dimensions, often referred to generally as **Tensors**.

*   **Scalar (0D Tensor):** A single number (e.g., `5`, `3.14`).
*   **Vector (1D Tensor):** A 1-dimensional array of numbers. Represents a point in space, or a single data record.
    *   *NumPy Shape:* `(N,)`
*   **Matrix (2D Tensor):** A 2-dimensional grid of numbers (rows and columns). Used to represent a dataset (rows = samples, columns = features) or weights in a neural network.
    *   *NumPy Shape:* `(M, N)`
*   **3D Tensor and Beyond:** Collections of matrices. For example, a color image is a 3D tensor: `(Height, Width, Color Channels)`.

---

## 2. The Power of Vectorization

In standard Python, applying a mathematical operation to a list of 1 million numbers requires a `for` loop, which is notoriously slow.

**Vectorization** is the process of applying an operation to an entire array at once. Under the hood, NumPy delegates these operations to highly optimized C code, making it hundreds or thousands of times faster than Python loops.

*   *Bad (Python Loop):* `[x * 2 for x in my_list]`
*   *Good (Vectorized NumPy):* `my_array * 2`

---

## 3. Broadcasting

**Broadcasting** is a powerful mechanism that allows NumPy to perform mathematical operations on arrays of different shapes.

Instead of writing loops to match dimensions, NumPy automatically "broadcasts" (stretches) the smaller array across the larger array so that they have compatible shapes.

*   **Scalar Broadcasting:** If you add a scalar to a matrix (`matrix + 5`), NumPy implicitly treats the scalar as a matrix of 5s of the same shape and performs element-wise addition.
*   **Vector to Matrix Broadcasting:** If you add a 1D vector `(3,)` to a 2D matrix `(4, 3)`, NumPy stretches the vector across all 4 rows of the matrix, adding it to each row individually.

*Rule of Broadcasting:* Two dimensions are compatible when they are equal, or one of them is 1.

---

## 4. Element-wise vs. Dot Product

A common source of bugs in AI code is confusing element-wise multiplication with matrix multiplication.

1.  **Element-wise Multiplication (`*`):** Multiplies corresponding elements.
    *   `A * B` requires `A` and `B` to have the exact same shape (or be broadcastable).
    *   If `A` is `(2, 2)` and `B` is `(2, 2)`, the output is `(2, 2)`.
2.  **Matrix Multiplication / Dot Product (`@` or `np.dot`):** Multiplies rows by columns following the rules of linear algebra.
    *   `A @ B` requires the inner dimensions to match. If `A` is `(M, N)` and `B` is `(N, P)`, the output is `(M, P)`.
    *   This is the core operation for Neural Network forward passes!

---

## 5. Advanced Initialization

You rarely initialize large matrices by typing out numbers. NumPy provides utility functions to generate them:
*   `np.zeros((M, N))`: Matrix of all zeros (useful for initializing biases).
*   `np.ones((M, N))`: Matrix of all ones.
*   `np.random.randn(M, N)`: Matrix of random numbers from a standard normal distribution (crucial for initializing Neural Network weights).
*   `np.eye(N)`: Identity matrix of size N x N (1s on the diagonal, 0s elsewhere).

---

## 6. Resources

*   **NumPy Official Quickstart Tutorial** – https://numpy.org/doc/stable/user/quickstart.html
*   **Broadcasting in NumPy (Documentation)** – https://numpy.org/doc/stable/user/basics.broadcasting.html
*   **NumPy Illustrated: The Visual Guide to NumPy (Medium)** – Excellent visual representations of vectorization and broadcasting.
*   **SciPy Lecture Notes: NumPy Array Object** – http://scipy-lectures.org/intro/numpy/index.html
*   **Deep Learning Book (Goodfellow) – Chapter 2: Linear Algebra** – https://www.deeplearningbook.org/contents/linear_algebra.html
