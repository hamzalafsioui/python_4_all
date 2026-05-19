# Examples: Harnessing the Power of Vectorized Calculations

import numpy as np

# --- 1. Vectorized Speed Comparison ---
def speed_demo():
    print("--- Speed: Python List vs. NumPy Array ---")
    size = 1_000_000
    
    # Standard Python list approach
    python_list = list(range(size))
    # We want to add 2 to every item. In standard Python, we must loop:
    import time
    start = time.perf_counter()
    python_list_result = [x + 2 for x in python_list]
    end = time.perf_counter()
    list_duration = end - start
    print(f"Python List comprehension: {list_duration:.5f} seconds")
    
    # NumPy array approach
    numpy_array = np.arange(size)
    # We do the exact same addition using native vectorization!
    start = time.perf_counter()
    numpy_array_result = numpy_array + 2
    end = time.perf_counter()
    array_duration = end - start
    print(f"NumPy Vectorized addition: {array_duration:.5f} seconds")
    print(f"NumPy is ~{list_duration / array_duration:.1f}x faster!\n")

# --- 2. Multi-Dimensional Array (Matrices) ---
def matrix_demo():
    print("--- Matrix Manipulations ---")
    # Create a 2D array (3 rows, 4 columns)
    matrix = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    
    print("Original Matrix:")
    print(matrix)
    print(f"Shape: {matrix.shape}")  # (3, 4)
    print(f"Number of dimensions: {matrix.ndim}")  # 2
    
    # Indexing and slicing: [row_slice, col_slice]
    print("\nRow 1 (second row):", matrix[1])  # [5, 6, 7, 8]
    print("Column 2 (third column):", matrix[:, 2])  # [3, 7, 11]
    print("Sub-matrix (top-left 2x2):\n", matrix[0:2, 0:2]) # [[1 2] [5 6]]
    
    # Reshaping: Transform to 2 rows, 6 columns
    reshaped = matrix.reshape(2, 6)
    print("\nReshaped Matrix (2x6):\n", reshaped)

# --- 3. Boolean Masking (Filtering) ---
def filtering_demo():
    print("\n--- Boolean Masking (Smart Filtering) ---")
    grades = np.array([85, 42, 90, 78, 61, 55, 95])
    
    # Create a condition mask
    passed_mask = grades >= 60
    print("Condition Mask (grades >= 60):", passed_mask)
    
    # Apply the mask to retrieve values
    passing_grades = grades[passed_mask]
    print("Filtered Passing Grades:", passing_grades)
    
    # Modify values matching a condition (e.g., curved grade for failing students)
    grades[grades < 60] += 5
    print("Curved Grades:", grades)

if __name__ == "__main__":
    # Note: Make sure to run 'pip install numpy' in your active environment!
    speed_demo()
    matrix_demo()
    filtering_demo()
