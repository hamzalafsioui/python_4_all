# Examples: Harnessing Multiple Cores

import time
import multiprocessing

# --- A Heavy CPU-Bound Task ---
def heavy_computation(number):
    """Simulates a heavy mathematical operation."""
    result = 0
    for i in range(100_000_000):
        result += i * number
    return result

# --- Serial vs Parallel ---
def run_serial(numbers):
    print("--- Running Serial (1 Core) ---")
    start = time.time()
    
    results = []
    for n in numbers:
        results.append(heavy_computation(n))
        
    end = time.time()
    print(f"Serial Time: {end - start:.4f} seconds")

def run_parallel(numbers):
    print("\n--- Running Parallel (Multiple Cores) ---")
    start = time.time()
    
    # Create a Pool of workers (uses all CPU cores by default)
    with multiprocessing.Pool() as pool:
        # map() automatically splits the 'numbers' list among the cores
        results = pool.map(heavy_computation, numbers)
        
    end = time.time()
    print(f"Parallel Time: {end - start:.4f} seconds")

# --- Usage ---

# CRITICAL: On Windows, multiprocessing MUST be inside this block!
if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print(f"Your computer has {cores} CPU cores available.\n")
    
    # A list of 4 tasks
    tasks = [1, 2, 3, 4]
    
    run_serial(tasks)
    run_parallel(tasks)
