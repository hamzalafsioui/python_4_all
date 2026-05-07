"""
Exercises: Data Structures - Tuples
"""

# Exercise 1: Tuple Creation & Access
# 1. Create a tuple named 'dimensions' with three numbers (width, height, depth).
# 2. Print the second number in the tuple.
# 3. Try to change the first number to 100. (Note: This should cause an error!)

# Your code here:

dimensions = (100, 200, 300)
print(dimensions[1])
# dimensions[0] = 100 # error because tuples are immutable
print(dimensions)

# ----------------------------------------------------------------

# Exercise 2: Unpacking
# Given the following data, unpack it into 'city', 'country', and 'year'.
location_data = ("Tokyo", "Japan", 2024)

# Your code here:

city, country, year = location_data
print(city)
print(country)
print(year)

# ----------------------------------------------------------------

# Exercise 3: Swapping Variables
# Use tuple unpacking to swap the values of 'a' and 'b' in one line.
a = 1
b = 99

# Your code here:

a, b = b, a
print(a)
print(b)

# ----------------------------------------------------------------

# Exercise 4: Tuple Methods
# Count how many times the number 7 appears in the tuple below.
# Find the index of the string "Python".
mixed_data = (7, "Java", 7, "Python", 7, "C++")

# Your code here:

print(mixed_data.count(7))
print(mixed_data.index("Python"))
