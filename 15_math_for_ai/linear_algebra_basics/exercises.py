"""
EXERCISES: The Vector Virtuoso

This script contains 3 practical exercises on linear algebra basics in NumPy.
Complete the TODO sections to solve them.
"""

import numpy as np

# =====================================================================
# EXERCISE 1: Vector Mechanics & Cosine Similarity
# =====================================================================
# In Recommendation Engines, users are represented as vectors in "preference space".
# Below are preference scores (Sci-Fi, Comedy, Action) for three users:
# range is 0.0 (hate) to 5.0 (love).
user_a = np.array([4.5, 1.0, 5.0]) # Loves Action/Sci-Fi, dislikes Comedy
user_b = np.array([1.2, 5.0, 0.5]) # Loves Comedy, dislikes Action/Sci-Fi
user_c = np.array([4.0, 1.5, 4.2]) # Similar to User A

def cosine_similarity(u, v):
    """
    Computes the cosine similarity between two vectors.
    Formula: (u . v) / (||u|| * ||v||)
    """
    # TODO: Implement the cosine similarity formula using NumPy
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    return dot_product / (norm_u * norm_v)

print("=== Exercise 1: Cosine Similarity ===")

# TODO: Calculate and print cosine similarities
sim_a_b = cosine_similarity(user_a, user_b)
sim_a_c = cosine_similarity(user_a, user_c)

print(f"Similarity between A and B (Expected: low): {sim_a_b:.4f}")
print(f"Similarity between A and C (Expected: high): {sim_a_c:.4f}")
print("-" * 50)


# =====================================================================
# EXERCISE 2: Dimensionality Matchmaker (Matrix Shapes)
# =====================================================================
# When composing multiple layers in a Neural Network, matrix shapes must align.
# Below are three matrix weight transformations with different sizes.
P = np.random.randn(4, 3) # Shape: (4, 3)
Q = np.random.randn(3, 5) # Shape: (3, 5)
R = np.random.randn(5, 4) # Shape: (5, 4)

print("\n=== Exercise 2: Shape Alignments ===")

# TODO 1: Multiply P, Q, and R together in sequence: S = P @ Q @ R
S = P @ Q @ R

print(f"Multiplied matrix S (Shape should be 4x4):")
print(S)
print(f"Shape of S: {S.shape}")

# TODO 2: Attempt to multiply Q @ P inside a try-except block.
# Explain why it fails in the exception print out.
try:
    result = Q @ P
except ValueError as e:
    print(f"\n[Expected Error Caught] Failed to multiply Q @ P:")
    print(f"  Reason: {e}")
    print(f"  Explanation: Q shape is {Q.shape} and P shape is {P.shape}.")
    print(f"  Columns of Q (5) do not match rows of P (4)!")

print("-" * 50)


# =====================================================================
# EXERCISE 3: Inverting Weights (Matrix Properties)
# =====================================================================
# In advanced machine learning optimizers, we calculate the inverse of weight matrices.
# Below is a 2D weight matrix.
W = np.array([[3, 4], 
              [2, 3]])

print("\n=== Exercise 3: Matrix Inversion ===")

# TODO 1: Calculate and print the Determinant of W
det_W = np.linalg.det(W)
print(f"Determinant of W: {det_W:.4f}")

# TODO 2: Calculate the Inverse matrix W_inv
W_inv = np.linalg.inv(W)
print(f"Inverse of W:\n{W_inv}")

# TODO 3: Verify W @ W_inv yields the Identity matrix using np.allclose()
product = W @ W_inv
is_identity = np.allclose(product, np.eye(2))

print(f"W @ W_inv product:\n{product}")
print(f"Does product equal Identity? {is_identity}")
print("=" * 60)

if __name__ == "__main__":
    print("\nAll linear algebra exercises completed successfully!")
