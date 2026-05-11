# Examples: Closures and State Management

# 1_ The Multiplier Factory
def make_multiplier(n):
    """Returns a function that multiplies its input by n."""
    def multiply(x):
        return x * n
    return multiply

# 2_ The Prefixed Logger
def make_logger(prefix):
    """Remembers a prefix for all logged messages."""
    def log(message):
        print(f"[{prefix.upper()}] {message}")
    return log

# 3_ Managing State (The Counter)
def make_counter(start_at=0):
    """A counter that remembers its current state."""
    count = start_at
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# --- Usage ---

if __name__ == "__main__":
    # Test Multiplier
    times5 = make_multiplier(5)
    times10 = make_multiplier(10)
    print(f"5 * 5 = {times5(5)}")
    print(f"10 * 5 = {times10(5)}")

    # Test Logger
    info_log = make_logger("info")
    error_log = make_logger("error")
    info_log("System started")
    error_log("Connection failed")

    # Test Counter
    my_counter = make_counter(10)
    print(f"Counter: {my_counter()}")
    print(f"Counter: {my_counter()}")
    print(f"Counter: {my_counter()}")
