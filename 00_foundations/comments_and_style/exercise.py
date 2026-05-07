"""
Exercises: Comments and Style

Your task is to refactor (improve) the code below.
"""

# Exercise 1: Refactor this code
# 1. Change variable names to be more descriptive.
# 2. Add proper spacing.
# 3. Add a meaningful comment.

# Original:
# a=50
# b=0.2
# c=a*b
# print(c)

# Your Refactored Code:

length = 50
width = 0.2
area = length * width
print(area)

# ----------------------------------------------------------------

# Exercise 2: Docstring Task
# Create a function (or just a block of code) that calculates 
# the distance between two points. Add a triple-quote docstring 
# explaining what the code does.

# Your code here:

def distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points.
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(distance(0, 0, 3, 4))


# ----------------------------------------------------------------

# Exercise 3: PEP 8 Check
# Which of these variable names follow PEP 8? (Mark with True/False)
# userAge = 25       # False
# user_age = 25      # True
# USER_AGE = 25      # (Hint: This is used for constants!) True
# _userage = 25      # False
