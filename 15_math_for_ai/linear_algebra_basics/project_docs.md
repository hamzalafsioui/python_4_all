# Linear Algebra Basics: Project Documentation

This document explains the two core Artificial Intelligence (AI) components built in the `project.py` file, breaking down the linear algebra concepts behind them in a simple and clear way.

---

## 1. Content-Based Movie Recommendation Engine

**What it does:**
It takes a user's movie taste (e.g., how much they like Action, Sci-Fi, Comedy) and recommends movies that closely match their preferences.

**How it works (The Concepts):**
*   **Vectors (Data Representation):** Both the movies and the user's preferences are represented as arrays of numbers called vectors. For example, a 5D vector `[5.0, 5.0, 1.0, 2.0, 1.0]` represents scores for `[Action, Sci-Fi, Comedy, Drama, Romance]`.
*   **Dot Product:** This is a mathematical operation that multiplies matching components of two vectors and adds them up. It acts as a rough measure of how much two vectors "overlap."
*   **Vector Norm (Magnitude):** The "length" of a vector in space. 
*   **Cosine Similarity:** This is the core concept. It measures the angle between two vectors rather than the distance between them. 
    *   If the angle is 0° (Cosine = 1.0), the vectors point in the exact same direction (a perfect match).
    *   If the angle is 90° (Cosine = 0.0), they share nothing in common.
    *   **Formula:** `(User Vector • Movie Vector) / (||User|| * ||Movie||)`. We use this score to rank and recommend the top movies.

---

## 2. Neural Network Layer Forward Pass

**What it does:**
It simulates a single "layer" of a Neural Network. It takes input data (like details of a house: square footage, bedrooms, age) and mathematically processes it to output a prediction probability (e.g., probability of selling fast vs. slow).

**How it works (The Concepts):**
*   **Vectors (Inputs & Biases):** 
    *   The input data is represented as a column vector `x` (Shape: 3x1).
    *   The biases are represented as a column vector `b` (Shape: 2x1), which acts as a base threshold for each output.
*   **Matrices (Weights):** The connections between the inputs and the outputs are represented as a Matrix `W` (Shape: 2x3). This matrix stores the "learned knowledge" or importance of each input feature.
*   **Matrix Multiplication (Linear Combination):** The core operation of neural networks is `z = W @ x + b`. 
    *   `W @ x` transforms the 3D input into a 2D output by multiplying the matrix rows by the input vector column.
    *   We then add the bias `b` to shift the result.
*   **Sigmoid Activation Function:** The result `z` can be any raw number. The Sigmoid function mathematically squishes this number into a probability range between `0.0` and `1.0`, making it easy to interpret as a percentage likelihood (e.g., an 85% chance it will sell fast).


