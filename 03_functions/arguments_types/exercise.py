"""
Exercises: Functions - Argument Types
"""

# Exercise 1: Default Message
# Create a function 'power' that takes two arguments: 'base' and 'exponent'.
# Set the default value of 'exponent' to 2. 
# The function should print the result of base^exponent.

# Your code here:

def power(base, exponent=2):
    print(base ** exponent)

power(5)


# ----------------------------------------------------------------

# Exercise 2: Keyword Order
# Define a function 'show_info' with parameters: 'name', 'job', and 'salary'.
# Call it using keyword arguments in a completely different order than defined.

# Your code here:

def show_info(name, job, salary):
    print(f"Name: {name}, Job: {job}, Salary: {salary}")

show_info(job="Developer", name="Hamza", salary=50000)


# ----------------------------------------------------------------

# Exercise 3: Variable Arguments (*args)
# Write a function 'multiply_all' that takes any number of arguments 
# and prints their product (all of them multiplied together).

# Your code here:

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    print(result)

multiply_all(1, 2, 3, 4)


# ----------------------------------------------------------------

# Exercise 4: Settings Dictionary (**kwargs)
# Create a function 'apply_settings' that takes any number of keyword 
# arguments representing system settings and prints them as:
# "Setting [Key] applied with value [Value]"

# Your code here:

def apply_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"Setting {key} applied with value {value}")

# apply_settings(**{"theme":"dark", "language":"python", "notifications":True})
apply_settings(theme="dark", language="python", notifications=True)

# ----------------------------------------------------------------
