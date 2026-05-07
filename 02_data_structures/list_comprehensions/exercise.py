"""
Exercises: Data Structures - List Comprehensions
"""

# Exercise 1: Basic Squares
# Use a list comprehension to create a list of squares for 
# numbers from 1 to 10.

# Your code here:

numbers = [n*n for n in range(1,11)]
print(numbers)

print("-" * 40)

# ----------------------------------------------------------------

# Exercise 2: Filtering Strings
# Given the list below, use a list comprehension to create a new 
# list containing only the names that start with the letter 'A'.
names = ["Ali", "Hamza", "Ahmed", "Zakaria", "Adam"]

# Your code here:

names_starting_with_A = [name for name in names if name.startswith("A")]

print(names_starting_with_A)
print("-" * 40)


# ----------------------------------------------------------------

# Exercise 3: Celsius to Fahrenheit
# Given a list of temperatures in Celsius, convert them to Fahrenheit.
# Formula: F = (C * 9/5) + 32
celsius = [0, 10, 20, 30, 40]

# Your code here:

fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)
print("-" * 40)

# ----------------------------------------------------------------

# Exercise 4: Conditional Logic
# Create a list that contains "Positive" if a number is >= 0 
# and "Negative" otherwise.
data = [10, -5, 3, -1, 0, 7]

# Your code here:

positive_negative_numbers = ["Positive" if i>=0 else "Negative" for i in data]
print(positive_negative_numbers)
print("-" * 40)