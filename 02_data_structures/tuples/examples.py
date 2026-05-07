"""
Examples: Data Structures - Tuples
This script demonstrates how to define, access, and unpack tuples.
"""

# ================== (1) Defining Tuples =======================
# Tuples use round brackets ()
colors = ("Red", "Green", "Blue")
empty_tuple = ()
single_tuple = ("Only one",) # Note the trailing comma!

print(f"Colors: {colors}")
print(f"Type: {type(colors)}")

print("-" * 20)

# ================== (2) Indexing and Slicing =======================
# Exactly the same as lists
print(f"First color: {colors[0]}")
print(f"Last color:  {colors[-1]}")
print(f"Slice (0:2): {colors[0:2]}")

print("-" * 20)

# ================== (3) Tuple Unpacking =======================
# Assigning tuple items to variables in one line
point = (100, 200, 300)
x, y, z = point

print(f"Unpacked -> x: {x}, y: {y}, z: {z}")

print("-" * 20)

# ================== (4) Returning multiple values from functions =======================
# Tuples are often used to return multiple pieces of data
def get_user_info():
    return "Hamza", 25, "Developer" # Returns a tuple

name, age, profession = get_user_info()
print(f"{name} is a {age} year old {profession}.")

print("-" * 20)

# ================== (5) Tuple Methods =======================
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Count of 2s: {numbers.count(2)}")
print(f"Index of 4:  {numbers.index(4)}")
