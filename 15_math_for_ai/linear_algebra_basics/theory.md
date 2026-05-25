# Linear Algebra Basics for AI and Machine Learning

Linear Algebra is the mathematical language of Artificial Intelligence. In machine learning, almost all data is represented as vectors and matrices, and the operations performed by algorithms (such as training a Neural Network or calculating similarity) are fundamentally linear algebra operations.

Understanding these concepts is crucial to grasping how models store weights, transform features, and make predictions.

---

## 1. Vectors: The Core Data Element

A **vector** is an ordered 1-dimensional array of numbers. Geometrically, it represents a point or a directed arrow in multi-dimensional space.

### Key Vector Concepts:
*   **Dimensionality**: A vector with $n$ elements is an $n$-dimensional vector (written as $\mathbf{v} \in \mathbb{R}^n$).
*   **Vector Operations**:
    *   **Addition / Subtraction**: Performed element-wise (vectors must be of identical length).
        $$\mathbf{u} + \mathbf{v} = [u_1 + v_1, u_2 + v_2, \dots, u_n + v_n]$$
    *   **Scalar Multiplication**: Multiplying a vector by a single number scales its magnitude without changing its core direction.
        $$c \cdot \mathbf{v} = [c \cdot v_1, c \cdot v_2, \dots, c \cdot v_n]$$

### The Dot Product
The **dot product** (or inner product) of two vectors yields a single scalar value. It is computed by multiplying corresponding elements and summing the results:
$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = u_1 v_1 + u_2 v_2 + \dots + u_n v_n$$

In NumPy:
```python
import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

dot_prod = np.dot(u, v)  # Or: u @ v
# Result: (1*4) + (2*5) + (3*6) = 4 + 10 + 18 = 32
```

### Vector Norms (Magnitude)
A **norm** measures the length or magnitude of a vector.
*   **$L_2$ Norm (Euclidean Distance)**: The standard geometric distance from the origin.
    $$\|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$$
    In NumPy: `np.linalg.norm(v)`
*   **$L_1$ Norm (Manhattan Distance)**: The sum of absolute values.
    $$\|\mathbf{v}\|_1 = |v_1| + |v_2| + \dots + |v_n|$$

### Cosine Similarity
Geometrically, the dot product is related to the angle $\theta$ between two vectors:
$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|_2 \|\mathbf{v}\|_2 \cos(\theta)$$

Thus, we can measure how similar the directions of two vectors are using **Cosine Similarity**:
$$\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$$
*   $\cos(\theta) = 1$: Vectors point in identical directions.
*   $\cos(\theta) = 0$: Vectors are orthogonal (perpendicular, completely independent).
*   $\cos(\theta) = -1$: Vectors point in opposite directions.

*AI Application*: Used heavily in recommendation engines, text similarity (embeddings), and semantic search.

---

## 2. Matrices: High-Dimensional Transforms

A **matrix** is a 2D grid of numbers. If a matrix has $m$ rows and $n$ columns, it is an $m \times n$ matrix (written as $A \in \mathbb{R}^{m \times n}$).

### Transpose ($A^T$)
Transposing a matrix flips it over its diagonal, swapping its rows and columns. If $A$ is $m \times n$, then $A^T$ is $n \times m$.
$$\text{If } A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}, \text{ then } A^T = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{bmatrix}$$

In NumPy: `A.T`

### Matrix Multiplication (Dot Product)
Multiplying two matrices is **not** element-wise. Instead, it is the dot product of rows from the first matrix and columns from the second.

*   **Shape Rule**: You can only multiply matrix $A$ by matrix $B$ if the number of columns in $A$ matches the number of rows in $B$.
    $$\text{Shape: } (m \times n) \times (n \times p) \rightarrow (m \times p)$$

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x & y \\ z & w \end{bmatrix} = \begin{bmatrix} ax+bz & ay+bw \\ cx+dz & cy+dw \end{bmatrix}$$

In NumPy, always use the `@` operator or `np.dot()` for matrix multiplication (using `*` will perform slow element-wise multiplication):
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = A @ B  # Correct matrix multiplication
```

---

## 3. Special Matrices & Operations

### Identity Matrix ($I$)
The identity matrix is a square matrix with $1$s on the main diagonal and $0$s elsewhere. Multiplying any matrix by the identity matrix yields the original matrix ($A I = I A = A$).
$$I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

In NumPy: `np.eye(3)`

### Determinant ($\det(A)$)
The determinant is a scalar value calculated from a square matrix. It describes how much matrix scaling alters area or volume. If $\det(A) = 0$, the matrix squashes space into a lower dimension, making it impossible to undo its transformation.

In NumPy: `np.linalg.det(A)`

### Matrix Inverse ($A^{-1}$)
The inverse of a square matrix $A$ is a matrix $A^{-1}$ such that:
$$A A^{-1} = A^{-1} A = I$$

An inverse only exists if $\det(A) \neq 0$. If a matrix has no inverse, it is called **singular**.

In NumPy: `np.linalg.inv(A)`

---

## 4. Why This Matters in AI/ML

### Datasets are Matrices
In ML, datasets are structured as matrices ($X$).
*   **Rows** represent individual data points (samples).
*   **Columns** represent measured features.

### Neural Networks are Matrix Operations
A single layer in a neural network takes an input feature vector $\mathbf{x}$, multiplies it by a weights matrix $W$, adds a bias vector $\mathbf{b}$, and applies an activation function $\sigma$ (such as Sigmoid or ReLU):

$$\mathbf{y} = \sigma(W\mathbf{x} + \mathbf{b})$$

When predicting on a whole batch of inputs ($X$), the computation becomes a clean, vectorized matrix operation:
$$Y = \sigma(X W^T + \mathbf{b})$$

Using GPUs to perform these large-scale matrix multiplications is what makes modern Deep Learning possible.

## Resources

- **3Blue1Brown: Essence of Linear Algebra (YouTube)** – https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- **Khan Academy: Linear Algebra** – https://www.khanacademy.org/math/linear-algebra
- **MIT OpenCourseWare: 18.06 Linear Algebra (Gilbert Strang)** – https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- **Mathematics for Machine Learning (Book, Free)** – https://mml-book.github.io/
- **NumPy Linear Algebra Module** – https://numpy.org/doc/stable/reference/routines.linalg.html
- **Deep Learning Book – Chapter 2: Linear Algebra (Goodfellow)** – https://www.deeplearningbook.org/contents/linear_algebra.html
