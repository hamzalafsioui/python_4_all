import time
from functools import wraps

# 0_ The "How it Works" Trace
def trace(func):
    """A decorator that explicitly shows the execution flow."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"   [Step 1] wrapper: Before calling '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"   [Step 3] wrapper: After calling '{func.__name__}'")
        return result
    return wrapper

@trace
def hello():
    print("   [Step 2] hello: I am running now!")

# ---------------------------------------------------------
def timer(func):
    """Measures the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"[{func.__name__}] Finished in {duration:.4f}s")
        return result
    return wrapper

def debug(func):
    """Prints the arguments and the return value of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"--- Calling {func.__name__}({signature}) ---")
        result = func(*args, **kwargs)
        print(f"--- {func.__name__} returned {result!r} ---")
        return result
    return wrapper

# 3_ Decorator with Arguments (The Triple-Layer)
def repeat(times):
    """A decorator factory that repeats a function call N times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"--- Starting {times} repetitions of {func.__name__} ---")
            last_result = None
            for i in range(times):
                print(f"   Repetition {i+1}...")
                last_result = func(*args, **kwargs)
            return last_result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("      Hi there!")

# --- Specialized Functions ---

@timer
def heavy_computation():
    """Simulates a slow process."""
    print("Starting a 1-second task...")
    time.sleep(1)
    return "Complete"

@debug
@timer
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# --- Usage ---

if __name__ == "__main__":
    print(">>> PART 0: THE TRACE")
    hello()
    
    print("\n>>> PART 1: THE REPEAT FACTORY")
    say_hi()

    print("\n>>> PART 2: COMPUTATION & DEBUG")
    heavy_computation()
    print("\n" + "-"*30 + "\n")
    print(greet("Hamza", message="Welcome"))
