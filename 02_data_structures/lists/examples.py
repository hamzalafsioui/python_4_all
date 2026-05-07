"""
Examples: Data Structures - Lists
This script demonstrates common list operations and methods.
"""

# ================== (1) Basic Operations =======================
languages = ["Python", "JavaScript", "C++", "Java"]

print(f"First language: {languages[0]}")
print(f"Last language: {languages[-1]}")
print(f"Slice (1 to 3): {languages[1:3]}")

print("-" * 20)

# ================== (2) Modifying Lists =======================
# Adding items
languages.append("Rust")
languages.insert(1, "Go")
print(f"After adding: {languages}")

# Removing items
removed = languages.pop() # Removes "Rust"
languages.remove("Java")
print(f"Removed: {removed}")
print(f"After removing: {languages}")

print("-" * 20)

# ================== (3) Sorting and Reversing =======================
nums = [42, 10, 5, 100, 7]
nums.sort()
print(f"Sorted: {nums}")

nums.reverse()
print(f"Reversed: {nums}")

print("-" * 20)

# ================== (4) List Concatenation and Repetition =======================
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Combined: {combined}")

repeated = [0] * 5
print(f"Repeated: {repeated}")

print("-" * 20)

# ================== (5) Useful Built-in Functions =======================
prices = [10.99, 5.50, 20.00, 15.75]
print(f"Number of items: {len(prices)}")
print(f"Highest price: {max(prices)}")
print(f"Lowest price: {min(prices)}")
print(f"Total sum: {sum(prices)}")
