"""
Examples: Data Structures - Sets
This script demonstrates set creation, modification, and mathematical operations.
"""

# ================== (1) Set Creation & Uniqueness =======================
# Duplicate items are automatically removed
skills = {"Python", "JavaScript", "Python", "SQL", "C++"}
print(f"Unique skills: {skills}")

print("-" * 20)

# ================== (2) Modifying Sets =======================
tools = {"Git", "Docker"}
tools.add("Jenkins")
tools.update(["VS Code", "Postman"]) # Add multiple items

print(f"Tools after update: {tools}")

tools.discard("Jenkins")
print(f"Tools after discard: {tools}")

print("-" * 20)

# ================== (3) Mathematical Operations =======================
group_a = {"Hamza", "Hasan", "Hadi", "Ali"}
group_b = {"Ali", "Hasan", "Hussain", "Qais"}

# Union (All unique members)
print(f"Union: {group_a | group_b}")

# Intersection (Common members)
print(f"Intersection: {group_a & group_b}")

# Difference (In A but not in B)
print(f"Difference (A-B): {group_a - group_b}")

# Symmetric Difference (Only in one group)
print(f"Symmetric Diff: {group_a ^ group_b}")

print("-" * 20)

# ================== (4) Fast Membership Testing =======================
# Extremely efficient way to check existence
if "Ali" in group_a:
    print("Ali is in Group A!")

print("-" * 20)

# ================== (5) Removing Duplicates from a List =======================
raw_data = [1, 2, 2, 3, 4, 4, 5, 1, 6]
clean_data = list(set(raw_data)) # List -> Set -> List
print(f"Original list: {raw_data}")
print(f"Cleaned list:  {clean_data}")
