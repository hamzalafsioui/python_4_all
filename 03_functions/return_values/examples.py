"""
Examples: Functions - Return Values
This script demonstrates how to capture and use data returned from functions.
"""

# ================== (1) Basic Return =======================
def get_full_name(first, last):
    """Combines names and returns the full string."""
    return f"{first.capitalize()} {last.capitalize()}"

user_name = get_full_name("hamza", "developer")
print(f"User: {user_name}")

print("-" * 20)

# ================== (2) Using Return in Calculations =======================
def calculate_tax(price, rate=0.2):
    return price * rate

price = 100
tax = calculate_tax(price)
total = price + tax
print(f"Total price including tax: ${total}")

print("-" * 20)

# ================== (3) Returning Multiple Values =======================
def get_stats(numbers):
    """Returns count, sum, and average of a list."""
    cnt = len(numbers)
    total = sum(numbers)
    avg = total / cnt
    return cnt, total, avg

c, s, a = get_stats([10, 20, 30, 40, 50])
print(f"Count: {c}, Sum: {s}, Average: {a}")

print("-" * 20)

# ================== (4) Conditional Return (Early Exit) =======================
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print(divide(10, 2))
print(divide(10, 0))
