"""
Examples: Input and Output
This script demonstrates how to interact with the user via the terminal.
"""

# ================== (1) Basic Input =======================
name = input("What is your name? ")
print(f"Hello, {name}!")

# Note: We comment out input calls in examples so they don't block execution
# if you run them without a terminal, but feel free to uncomment and test!

print("-" * 20)

# ================== (2) Input Type Conversion =======================
year_born = input("What year were you born? ")
age = 2026 - int(year_born)
print(f"You are approximately {age} years old.")

print("-" * 20)

# ================== (3) Print Customization =======================
print("Apple", "Banana", "Cherry", sep=" | ")
print("This stays on", end=" ")
print("the same line.")

print("-" * 20)

# ================== (4) Advanced F-Strings =======================
pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

score = 0.85
print(f"Percentage: {score:.2%}") # 85.00%
