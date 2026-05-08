"""
Exercises: Functions - Return Values
"""

# Exercise 1: Multiplier
# Create a function 'multiply' that returns the product of two numbers.
# Store the result in a variable 'total' and print it.

# Your code here:

def multiply(a, b):
    return a * b

total = multiply(5, 10)
print(total)


# ----------------------------------------------------------------

# Exercise 2: List Processor
# Write a function 'get_first_and_last' that takes a list 
# and returns both the first and the last element.

# Your code here:

def get_first_and_last(lst):
    return lst[0], lst[-1]

print(get_first_and_last([1, 2, 3, 4, 5]))


# ----------------------------------------------------------------

# Exercise 3: User Validator
# Create a function 'is_valid_username' that returns True if 
# a username is longer than 5 characters, and False otherwise.

# Your code here:

def is_valid_username(username):
    return len(username) > 5

print(is_valid_username("hamza"))


# ----------------------------------------------------------------

# Exercise 4: Discount Calculator
# Write a function 'apply_discount' that returns the final price 
# after applying a percentage discount.
# If the discount is more than 100 or less than 0, return "Invalid".

# Your code here:

def apply_discount(price, discount):
    if discount > 100 or discount < 0:
        return "Invalid"
    return price - (price * discount / 100)

print(apply_discount(100, 50))
