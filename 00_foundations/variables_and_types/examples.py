"""
Examples: Variables and Data Types
This script demonstrates how to define variables and use basic data types in Python.
"""

# ================== (1) Variable Assignment =======================
# Python is dynamically typed, so we don't need to specify the type.
name = "Python 4 All"
version = 3.12
is_fun = True
max_score = 100

print(f"Name: {name}")
print(f"Version: {version}")
print(f"Is Fun? {is_fun}")
print(f"Max Score: {max_score}")

print("-" * 20)

# ================== (2) Checking Data Types =======================
# Use type() to inspect the type of a variable.
print(f"Type of name: {type(name)}")
print(f"Type of version: {type(version)}")
print(f"Type of is_fun: {type(is_fun)}")
print(f"Type of max_score: {type(max_score)}")

print("-" * 20)

# ================== (3) Type Casting =======================
# Converting between types.
raw_input = "50"
score = int(raw_input)  # String to Int
average = float(score)  # Int to Float
status = str(is_fun)    # Bool to String

print(f"Score (as int): {score}")
print(f"Average (as float): {average}")
print(f"Status (as string): {status}")

print("-" * 20)

# ================== (4) Multiple Assignment =======================
x, y, z = 1, 2, 3
print(f"x: {x}, y: {y}, z: {z}")

# Swapping variables (The Pythonic way!)
x, y = y, x
print(f"Swapped x: {x}, Swapped y: {y}")
