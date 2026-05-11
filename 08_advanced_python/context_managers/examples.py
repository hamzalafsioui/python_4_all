# Examples: Class vs Function-Based Context Managers

import time
from contextlib import contextmanager

# 1_ Class-Based: A Custom Timer
class TimerContext:
    """Measures the time spent inside the 'with' block."""
    def __enter__(self):
        self.start = time.perf_counter()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f"--- Block finished in {self.end - self.start:.4f}s ---")

# 2_ Function-Based: A Directory Manager
import os

@contextmanager
def temp_dir_change(new_path):
    """Changes the current directory and returns back safely."""
    old_path = os.getcwd()
    print(f"Moving to: {new_path}")
    os.chdir(new_path)
    try:
        yield
    finally:
        print(f"Returning to: {old_path}")
        os.chdir(old_path)

# --- Usage ---

if __name__ == "__main__":
    # Test Class-Based
    print(">>> PART 1: CLASS-BASED TIMER")
    with TimerContext():
        print("Doing some heavy work...")
        time.sleep(1)
        
    # Test Function-Based
    print("\n>>> PART 2: FUNCTION-BASED DIR CHANGER")
    # Using a relative path for the demo
    target = os.path.dirname(os.path.abspath(__file__))
    with temp_dir_change(target):
        print(f"Current working directory: {os.getcwd()}")
