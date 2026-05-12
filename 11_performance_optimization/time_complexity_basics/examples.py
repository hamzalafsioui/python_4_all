# Examples: Visualizing Big O in Action

import time

# 1_ Constant Time O(1)
def constant_demo(data_list):
    # Accessing an index is instantaneous regardless of list size
    return data_list[0]

# 2_ Linear Time O(n)
def linear_demo(data_list, target):
    # We must check every single item until we find the target
    for item in data_list:
        if item == target:
            return True
    return False

# 3_ Quadratic Time O(n^2)
def quadratic_demo(data_list):
    # Nested loops - finding duplicates the "naive" way
    duplicates = []
    for i in range(len(data_list)):
        for j in range(i + 1, len(data_list)):
            if data_list[i] == data_list[j]:
                duplicates.append(data_list[i])
    return duplicates

# --- Measuring Performance ---

def benchmark():
    small_list = list(range(100))
    large_list = list(range(10000))

    # O(n) Search
    print("--- O(n) Search ---")
    start = time.time()
    linear_demo(large_list, 9999)
    print(f"Search 10,000 items: {time.time() - start:.6f}s")

    # O(n^2) Search (Notice how much longer this takes!)
    print("\n--- O(n^2) Duplicate Search ---")
    start = time.time()
    quadratic_demo(list(range(1000))) # Only 1,000 items!
    print(f"Duplicates in 1,000 items: {time.time() - start:.6f}s")
    
    start = time.time()
    quadratic_demo(list(range(2000))) # Double the data...
    print(f"Duplicates in 2,000 items: {time.time() - start:.6f}s") # ...4x the time!

if __name__ == "__main__":
    benchmark()
