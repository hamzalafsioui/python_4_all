"""
Exercises: Functions - Lambda Functions
"""

# Exercise 1: One-Liner Math
# Convert the following function into a lambda function named 'multiply'.
# def multiply(a, b):
#     return a * b

# Your code here:

multiply = lambda n1,n2: n1*n2

print(multiply(4,5))

print('='*30)


# ----------------------------------------------------------------

# Exercise 2: String Formatter
# Write a lambda function named 'clean_string' that takes a string, 
# strips whitespace, and converts it to uppercase.

# Your code here:

clean_string = lambda s: s.strip().upper()

print(clean_string("  Hello World  "))

print('='*30)

# ----------------------------------------------------------------

# Exercise 3: Filter Even Numbers
# Use the 'filter()' function and a lambda to keep only even 
# numbers from the list below.
numbers = [12, 5, 8, 19, 20, 7, 3]

# Your code here:

even_numbers = list(filter(lambda x: x%2==0,numbers))
print(even_numbers)

print('='*30)

# ----------------------------------------------------------------

# Exercise 4: Custom Sort
# Sort the following list of strings by their LAST character 
# using a lambda as the key.
words = ["apple", "banana", "cherry", "date"]

# Your code here:

sorted_words = sorted(words,key = lambda s:s[-1])
print(sorted_words)

print('='*30)