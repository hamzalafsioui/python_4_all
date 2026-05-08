"""
Examples: Functions - Recursion
This script demonstrates the "stop and repeat" nature of recursion.
"""

# ================== (1) Basic Countdown =======================
def countdown(n):
    """Prints numbers down to 0 using recursion."""
    if n < 0:
        print("Blast off!")
        return # Base Case
    
    print(n)
    countdown(n - 1) # Recursive Case

print("Countdown Start:")
countdown(5)

print("-" * 20)

# ================== (2) Summing a List =======================
def recursive_sum(numbers):
    """Calculates the sum of a list recursively."""
    if not numbers:
        return 0 # Base Case (empty list)
    
    # Recursive Case: First item + sum of the rest
    return numbers[0] + recursive_sum(numbers[1:])

my_nums = [10, 20, 30, 40]
print(f"List Sum: {recursive_sum(my_nums)}")

print("-" * 20)

# ================== (3) Fibonacci Sequence =======================
# 0, 1, 1, 2, 3, 5, 8, 13...
def fibonacci(n):
    if n <= 1:
        return n # Base Case
    return fibonacci(n - 1) + fibonacci(n - 2) # Recursive Case

print(f"10th Fibonacci number: {fibonacci(10)}")
