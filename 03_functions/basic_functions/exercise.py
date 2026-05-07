"""
Exercises: Functions - Basic Functions
"""

# Exercise 1: Simple Greeting
# Create a function named 'greet_user' that takes one parameter 'name' 
# and prints "Hello, [name]! Hope you're having a great day."

# Your code here:

def greet_user(name):
    print(f"Hello, {name}! Hope you're having a great day.")

greet_user("Hamza")


# ----------------------------------------------------------------

# Exercise 2: Square Calculator
# Write a function named 'calculate_square' that takes a number 
# and prints the square of that number.

# Your code here:

def calculate_square(number):
    print(number * number)

calculate_square(5)


# ----------------------------------------------------------------

# Exercise 3: Area of a Rectangle
# Create a function named 'print_area' that takes 'length' and 'width' 
# as parameters and prints the area of the rectangle.

# Your code here:

def print_area(length, width):
    print(length * width)

print_area(5, 10)


# ----------------------------------------------------------------

# Exercise 4: Docstring Check
# 1. Define a function named 'say_goodbye'.
# 2. Add a docstring that says "Prints a goodbye message."
# 3. Print the docstring of the function using 'say_goodbye.__doc__'.

# Your code here:

def say_goodbye():
    """Prints a goodbye message."""
    print("Goodbye!")

print(say_goodbye.__doc__)

