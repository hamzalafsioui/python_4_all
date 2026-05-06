"""
Exercises: Control Flow - If/Else

"""

# Exercise 1: Odd or Even
# Write a program that takes a number and prints whether it is "Even" or "Odd".
number = 7

# Your code here:
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ----------------------------------------------------------------

# Exercise 2: Age Categories
# Write a program that prints a message based on the age:
# - age < 13: "Child"
# - 13 <= age < 20: "Teenager"
# - 20 <= age < 65: "Adult"
# - age >= 65: "Senior"
age = 25

# Your code here:
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# ----------------------------------------------------------------

# Exercise 3: Leap Year (Bonus)
# A year is a leap year if:
# - It is divisible by 4
# - EXCEPT if it is divisible by 100, unless it is also divisible by 400.
# Hint: Use the modulo operator (%) to check divisibility.
year = 2024

# Your code here:
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")


# ----------------------------------------------------------------

# Exercise 4: Simple Calculator
# Create variables for two numbers and an operator (+, -, *, /).
# Use if/elif/else to perform the calculation and print the result.
num1 = 10
num2 = 5
operator = "/"

# Your code here:
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else: 
        print(num1 / num2)
else:
    print("Invalid operator")