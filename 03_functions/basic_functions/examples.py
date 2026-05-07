"""
Examples: Functions - Basic Functions
This script demonstrates how to define and call simple functions.
"""

# ================== (1) No-Argument Function =======================
def show_welcome():
    """Prints a standard welcome message."""
    print("*" * 30)
    print("Welcome to Python Mastery!")
    print("*" * 30)

show_welcome()

print("-" * 20)

# ================== (2) Single Parameter Function =======================
def celebrate_birthday(name):
    """Prints a birthday message for a specific person."""
    print(f"Happy Birthday, {name}! (from hamza)")

celebrate_birthday("Hamza")
celebrate_birthday("Ali")

print("-" * 20)

# ================== (3) Multiple Parameter Function =======================
def print_sum(a, b):
    """Calculates and prints the sum of two numbers."""
    total = a + b
    print(f"The sum of {a} and {b} is: {total}")

print_sum(10, 5)
print_sum(100, 250)

print("-" * 20)

# ================== (4) Functions calling Functions =======================
def morning_routine(name):
    print(f"Good morning, {name}!")
    show_welcome() # Calling another function

morning_routine("Developer")
