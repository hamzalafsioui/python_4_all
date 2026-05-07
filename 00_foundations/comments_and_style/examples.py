"""
Examples: Comments and PEP 8 Style
This file demonstrates clean vs. messy code.

"""

# ================== (1) Messy Code (Avoid this!) =======================
x=10 # set x to 10
y=20 # set y to 20
z=x+y # add them
print(z)

# Why is this bad?
# 1. No spaces around operators.
# 2. Meaningless variable names.
# 3. "What" comments that state the obvious.

print("-" * 20)

# ================== (2) Clean Code (Pythonic) =======================
# Initialize score variables
player_score = 10
bonus_points = 20

# Calculate total by adding base score and bonuses
total_score = player_score + bonus_points

print(f"Total: {total_score}")

# Why is this better?
# 1. Descriptive names (player_score).
# 2. Proper spacing.
# 3. Comments explain the intent.

print("-" * 20)

# ================== (3) Docstrings =======================
def calculate_tax(price):
    """
    Calculates a 15% tax on a given price.
    Returns the total price including tax.
    """
    return price * 1.15
