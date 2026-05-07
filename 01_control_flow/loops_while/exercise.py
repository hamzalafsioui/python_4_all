"""
Exercises: Control Flow - While Loops
"""

# Exercise 1: Sum of Input
# Write a program that keeps asking the user for a number 
# and adds it to a total. The loop should stop if the user 
# enters 0.

# Your code here:

total = 0
number = int(input("Enter a number (0 to quit): "))
while number != 0:
    total += number
    number = int(input("Enter a number (0 to quit): "))
print(total)


# ----------------------------------------------------------------

# Exercise 2: Password Validator
# 1. Set a variable 'correct_password' to "python123".
# 2. Ask the user for a password.
# 3. While the input is incorrect, keep asking.
# 4. Once correct, print "Access Granted".

# Your code here:

correct_password = "python123"
password = input("Enter your password: ")
while password != correct_password:
    password = input("Enter your password: ")
print("Access Granted")


# ----------------------------------------------------------------

# Exercise 3: Power of 2
# Write a while loop that prints all powers of 2 (2, 4, 8, 16...) 
# that are less than 1000.

# Your code here:

powers = 2
while powers < 1000:
    print(powers)
    powers *= 2