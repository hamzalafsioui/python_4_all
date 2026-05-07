"""
Examples: Basic Operators
This script demonstrates arithmetic, assignment, and comparison operators.
"""

# ================== (1) Arithmetic Operators =======================
a = 15
b = 4

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}") # Removes decimal
print(f"Modulo: {a % b}")           # Remainder
print(f"Exponentiation: {a ** 2}")  # 15 squared

print("-" * 20)

# ================== (2) Assignment Operators =======================
x = 10
print(f"Initial x: {x}")

x += 5  # x = x + 5
print(f"After x += 5: {x}")

x *= 2  # x = x * 2
print(f"After x *= 2: {x}")

print("-" * 20)

# ================== (3) Comparison Operators =======================
print(f"Is 10 == 10? {10 == 10}")
print(f"Is 10 != 5?  {10 != 5}")
print(f"Is 10 > 20?  {10 > 20}")
print(f"Is 5 <= 5?   {5 <= 5}")

print("-" * 20)

# ================== (4) String Concatenation =======================
# The '+' operator also works for strings!
greeting = "Hello" + " " + "World"
print(greeting)

repeat_me = "Python! " * 3
print(repeat_me)
