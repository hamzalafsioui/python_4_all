# utils.py
def greet(name):
    return f"Hello, {name}!"

def power(base, exp):
    return base ** exp

# This is a module-level constant
VERSION = "1.0.0"

if __name__ == "__main__":
    print("--- Running Utils Module Standalone ---")
    print(f"Test Greet: {greet('User')}")
    print(f"Test Power: {power(2, 3)}")
