# Examples: Generators vs Lists

import sys
import time

# 0_ The Execution Trace (Step-by-Step)
def countdown(n):
    print(f"--- Starting countdown from {n} ---")
    while n > 0:
        print(f"   [Yielding {n}]")
        yield n
        print(f"   [Resuming after {n}]")
        n -= 1
    print("--- Countdown finished! ---")

# 1_ Memory Comparison
def compare_memory():
    n = 1_000_000
    
    # Eager List
    start_list = time.perf_counter()
    my_list = [i for i in range(n)]
    end_list = time.perf_counter()
    list_size = sys.getsizeof(my_list) / (1024 * 1024) # MB
    
    # Lazy Generator
    start_gen = time.perf_counter()
    my_gen = (i for i in range(n))
    end_gen = time.perf_counter()
    gen_size = sys.getsizeof(my_gen) / 1024 # KB
    
    print(f"List:      {list_size:.2f} MB | Time: {end_list-start_list:.4f}s")
    print(f"Generator: {gen_size:.2f} KB | Time: {end_gen-start_gen:.4f}s")

# 2_ Infinite Generator
def infinite_ids():
    """Generates unique IDs forever."""
    n = 1
    while True:
        yield f"USER_{n:04d}"
        n += 1

# --- Usage ---

if __name__ == "__main__":
    print(">>> PART 0: THE EXECUTION TRACE")
    counter = countdown(3)
    print(f"Result from next(): {next(counter)}")
    print(f"Result from next(): {next(counter)}")
    
    print("\n>>> PART 1: MEMORY EFFICIENCY")
    compare_memory()
    
    print("\n>>> PART 2: INFINITE STREAM (First 5 IDs)")
    id_stream = infinite_ids()
    for _ in range(5):
        print(next(id_stream))
