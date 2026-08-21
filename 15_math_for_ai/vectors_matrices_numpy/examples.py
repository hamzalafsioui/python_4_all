# Examples: Vectors, Matrices, and NumPy Mechanics

import numpy as np
import time

def creation_and_shapes_demo():
    print("--- 1. Array Creation & Shapes ---")
    
    # 1D Vector
    vector = np.array([1, 2, 3, 4, 5])
    print(f"Vector:\n{vector}\nShape: {vector.shape}\n")
    
    # 2D Matrix
    matrix = np.array([[1, 2, 3], 
                       [4, 5, 6]])
    print(f"Matrix:\n{matrix}\nShape: {matrix.shape}\n")
    
    # Initialization shortcuts
    zeros_mat = np.zeros((2, 3))
    print(f"Zeros Matrix (2x3):\n{zeros_mat}\n")
    
    random_mat = np.random.randn(3, 3) # Standard normal distribution
    print(f"Random Weights Matrix (3x3):\n{random_mat}")
    print("-" * 50)

def vectorization_speed_demo():
    print("\n--- 2. Vectorization vs Python Loops (Speed Test) ---")
    # Let's create an array of 5 million random numbers
    size = 5_000_000
    big_array = np.random.rand(size)
    big_list = list(big_array)
    
    # Objective: Multiply every number by 5
    
    # 1. Using a standard Python For Loop
    start_time = time.time()
    result_list = [x * 5 for x in big_list]
    loop_time = time.time() - start_time
    print(f"Python Loop Time:  {loop_time:.4f} seconds")
    
    # 2. Using NumPy Vectorization
    start_time = time.time()
    result_array = big_array * 5
    vec_time = time.time() - start_time
    print(f"NumPy Vector Time: {vec_time:.4f} seconds")
    
    # Calculate speedup
    speedup = loop_time / vec_time if vec_time > 0 else float('inf')
    print(f"-> NumPy was {speedup:.1f}x faster!")
    print("-" * 50)

def broadcasting_demo():
    print("\n--- 3. Broadcasting Magic ---")
    matrix = np.array([[10, 20, 30],
                       [40, 50, 60]]) # Shape (2, 3)
                       
    print(f"Original Matrix (Shape {matrix.shape}):\n{matrix}\n")
    
    # 1. Scalar Broadcasting
    # Adds 5 to every single element automatically
    print(f"Matrix + 5 (Scalar Broadcasting):\n{matrix + 5}\n")
    
    # 2. Vector Broadcasting
    vector = np.array([1, 2, 3]) # Shape (3,)
    print(f"Vector (Shape {vector.shape}): {vector}")
    
    # NumPy stretches the vector across all rows to match the matrix shape
    result = matrix + vector
    print(f"Matrix + Vector (Vector Broadcasting):\n{result}")
    print("-" * 50)

def multiplication_types_demo():
    print("\n--- 4. Element-wise vs Matrix Multiplication ---")
    
    A = np.array([[1, 2],
                  [3, 4]])
    
    B = np.array([[2, 0],
                  [1, 2]])
                  
    print(f"Matrix A:\n{A}\n")
    print(f"Matrix B:\n{B}\n")
    
    # Element-wise multiplication (*)
    # Multiplies position (0,0) with (0,0), (0,1) with (0,1), etc.
    element_wise = A * B
    print(f"Element-wise Multiplication (A * B):\n{element_wise}\n")
    
    # Matrix Multiplication (@ or np.dot)
    # Uses linear algebra row-by-column rules
    dot_product = A @ B
    print(f"Matrix Multiplication (A @ B):\n{dot_product}")
    print("-" * 50)

if __name__ == "__main__":
    print("=" * 60)
    print("=== STARTING VECTORS & MATRICES DEMO ===")
    print("=" * 60)
    creation_and_shapes_demo()
    vectorization_speed_demo()
    broadcasting_demo()
    multiplication_types_demo()
    print("=== DEMO FINISHED SUCCESSFULLY ===")
    print("=" * 60)
