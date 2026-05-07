"""
Mini-Project: Multiplication Table Generator

This project generates a formatted multiplication table for a specific number.
"""

# 1_ Configuration
number = 7 # The table to generate
limit = 12 # How far to go (e.g_, 7 x 12)

# 2_ Print Header
print("=" * 25)
print(f" Multiplication Table: {number}")
print("=" * 25)

# 3_ Generate Table
for i in range(1, limit + 1):
    result = number * i
    # Using alignment in f-strings for a clean table
    print(f"{number} x {i:>2} = {result:>3}")

print("=" * 25)

# Bonus: Nested Multiplication Table (1-5)
print("\nMulti-Table (1-5):")
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:3}", end=" ")
    print()
