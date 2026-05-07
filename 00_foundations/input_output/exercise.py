"""
Exercises: Input and Output

Practice gathering data and formatting it correctly.
"""

# Exercise 1: Personal Greeter
# Write a program that asks for the user's name and favorite color, 
# then prints a message like: "Hi Alice! Blue is a great color!"

# Your code here:

user_name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(f"Hi {user_name}! {favorite_color} is a great color!")

# ----------------------------------------------------------------

# Exercise 2: Tip Calculator
# 1_ Ask the user for the total bill amount (float).
# 2_ Ask the user for the tip percentage they want to leave (e.g., 15).
# 3_ Calculate the total tip amount and the final bill.
# 4_ Print the result formatted to 2 decimal places.

# Your code here:

total_bill = float(input("What is the total bill amount? "))
tip_percentage = int(input("What is the tip percentage? "))

total_tip = total_bill * (tip_percentage / 100)
final_bill = total_bill + total_tip

print(f"Total Bill: ${total_bill:.2f}")
print(f"Tip Percentage: {tip_percentage:.1f}%")
print(f"Total Tip: ${total_tip:.2f}")
print(f"Final Bill: ${final_bill:.2f}")

# ----------------------------------------------------------------

# Exercise 3: Character Counter
# Ask the user for a sentence and print the total number of characters in it.
# Hint: Use len()

# Your code here:

sentence = input("enter your sentence: ")
print(f"the total number of characters in this sentence is {len(sentence)}")
