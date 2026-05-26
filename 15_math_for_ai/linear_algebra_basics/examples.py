# Examples: Linear Algebra in NumPy

import numpy as np

def vector_operations_demo():
    print("--- 1. Vector Operations ---")
    u = np.array([3, -1, 2])
    v = np.array([1, 5, -2])
    
    print(f"Vector u: {u}")
    print(f"Vector v: {v}")
    
    # 1. Addition & Subtraction
    print(f"Addition (u + v): {u + v}")
    print(f"Subtraction (u - v): {u - v}")
    
    # 2. Scalar Multiplication
    print(f"Scalar scaling (3 * u): {3 * u}")
    
    # 3. Dot Product
    dot_prod = np.dot(u, v) # or: u @ v
    print(f"Dot product (u . v): {dot_prod}")
    
    # 4. Vector Norms (Magnitude)
    l1_norm = np.linalg.norm(u, ord=1)
    l2_norm = np.linalg.norm(u, ord=2) # default
    print(f"L1 Norm of u (Manhattan distance): {l1_norm}")
    print(f"L2 Norm of u (Euclidean distance): {l2_norm:.4f}")
    
    # 5. Cosine Similarity Calculation
    # Cos(theta) = (u . v) / (||u|| * ||v||)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    cosine_sim = np.dot(u, v) / (norm_u * norm_v)
    print(f"Cosine Similarity between u and v: {cosine_sim:.4f}")
    print("-" * 50)

def matrix_operations_demo():
    print("\n--- 2. Matrix Operations ---")
    A = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6]]) # Shape: (3, 2)
                  
    B = np.array([[7, 8, 9], 
                  [10, 11, 12]]) # Shape: (2, 3)
                  
    print(f"Matrix A (Shape {A.shape}):\n{A}")
    print(f"Matrix B (Shape {B.shape}):\n{B}")
    
    # 1. Transpose
    print(f"Transpose of A (A.T, Shape {A.T.shape}):\n{A.T}")
    
    # 2. Matrix Multiplication (Dot Product)
    # (3x2) @ (2x3) -> (3x3)
    C = A @ B
    print(f"Matrix multiplication (A @ B, Shape {C.shape}):\n{C}")
    
    # 3. Element-wise Multiplication (Caution!)
    # Element-wise multiplication requires identical shapes. Let's showcase it with square matrices.
    X = np.array([[1, 2], [3, 4]])
    Y = np.array([[5, 6], [7, 8]])
    print(f"\nMatrix X:\n{X}")
    print(f"Matrix Y:\n{Y}")
    print(f"Element-wise multiplication (X * Y):\n{X * Y}")
    print(f"True Matrix multiplication (X @ Y):\n{X @ Y}")
    print("-" * 50)

def advanced_matrix_demo():
    print("\n--- 3. Determinants, Inverses, and Linear Solvers ---")
    
    A = np.array([[2, 1], 
                  [1, 3]]) # Shape: (2, 2)
    print(f"Square Matrix A:\n{A}")
    
    # 1. Determinant
    det_A = np.linalg.det(A)
    print(f"Determinant of A: {det_A:.4f}")
    
    # 2. Inverse
    A_inv = np.linalg.inv(A)
    print(f"Inverse of A (A_inv):\n{A_inv}")
    
    # Verify: A @ A_inv should equal Identity matrix (within float tolerance)
    identity_check = A @ A_inv
    print(f"Verification (A @ A_inv):\n{identity_check}")
    print(f"Is it equal to Identity Matrix? {np.allclose(identity_check, np.eye(2))}")
    
    # 3. Solving a System of Linear Equations
    # Suppose we have:
    # 2x +  y = 8
    #  x + 3y = 9
    # Written as A * x = y_vec
    y_vec = np.array([8, 9])
    
    # Explicit (Unstable) method: x = A_inv @ y
    # Professional (Stable) method: np.linalg.solve(A, y)
    solution = np.linalg.solve(A, y_vec)
    print(f"\nSolving system A * x = [8, 9]...")
    print(f"Solution vector x (values of x and y): {solution}")
    
    # Verify solution:
    print(f"Verification (A @ solution): {A @ solution} (Expected: [8. 9.])")
    print("-" * 50)

if __name__ == "__main__":
    print("=== STARTING LINEAR ALGEBRA BASICS DEMO ===")
    vector_operations_demo()
    matrix_operations_demo()
    advanced_matrix_demo()
    print("=== DEMO FINISHED SUCCESSFULLY ===")
