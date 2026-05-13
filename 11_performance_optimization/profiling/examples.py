# Examples: Identifying Slow Functions

import cProfile
import time

# --- A Sample "Complex" Program ---

def fast_task():
    # This represents a quick operation
    time.sleep(0.01)

def medium_task():
    # This takes a bit longer
    for _ in range(1000):
        sum(i for i in range(100))

def slow_task():
    # This is our intentional bottleneck
    time.sleep(1)
    # A heavy mathematical operation
    return [x**2 for x in range(1000000)]

def main():
    print("Starting program...")
    for _ in range(10):
        fast_task()
    
    medium_task()
    
    print("Running the slow part...")
    slow_task()
    
    print("Program finished.")

# --- How to Profile ---

if __name__ == "__main__":
    # Option 1: Profile via code
    # cProfile.run('main()')
    
    # Option 2 (Recommended): Run from terminal
    # python -m cProfile -s cumtime examples.py
    main()
