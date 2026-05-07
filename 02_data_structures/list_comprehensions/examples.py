"""
Examples: Data Structures - List Comprehensions
This script demonstrates various ways to create lists efficiently.
"""

# ================== (1) Basic Transformation =======================
names = ["ali", "hamza", "yassin"]
capital_names = [name.capitalize() for name in names]
print(f"Capitals: {capital_names}")

print("-" * 20)

# ================== (2) Filtering with 'if' =======================
prices = [10, 55, 20, 100, 5, 80]
# Keep only expensive items (> 50)
expensive_items = [p for p in prices if p > 50]
print(f"Expensive: {expensive_items}")

print("-" * 20)

# ================== (3) Transformation with 'if-else' =======================
scores = [45, 88, 72, 30, 95]
# Convert scores to "Pass" or "Fail"
results = ["Pass" if s >= 50 else "Fail" for s in scores]
print(f"Scores:  {scores}")
print(f"Results: {results}")

print("-" * 20)

# ================== (4) Nested Loops (Brief) =======================
# Create a coordinates list [(0,0), (0,1), (1,0), (1,1)]
coords = [(x, y) for x in range(2) for y in range(2)]
print(f"Coordinates: {coords}")

print("-" * 20)

# ================== (5) Dictionary Comprehension =======================
# Mapping words to their lengths
words = ["Python", "is", "awesome"]
lengths = {word: len(word) for word in words}
print(f"Word Lengths: {lengths}")

print("-" * 20)

# ================== (6) Set Comprehension =======================
# Create a set of squares from a list
numbers = [1, 2, 2, 3, 3, 4]
squares = {n * n for n in numbers}
print(f"Squares: {squares}")

