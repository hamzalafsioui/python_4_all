"""
Exercises: Data Structures - Sets
"""

# Exercise 1: Unique Values
# Given the list of emails below, create a set to find all 
# unique email providers. (e.g., "gmail.com")
emails = ["ali@gmail.com", "hamza@yahoo.com", "ali@gmail.com", "lil@outlook.com", "hussain@gmail.com"]
providers = set()

# Hint: You can use a loop and .split("@")[1]
# Your code here:

for email in emails:
    providers.add(email.split("@")[1])

print(providers)



# ----------------------------------------------------------------

# Exercise 2: Group Intersection
# You have two groups of students attending different workshops.
# 1. Find students who attended BOTH workshops.
# 2. Find students who attended ONLY the Python workshop.
# 3. Find all students who attended at least one workshop.

python_workshop = {"Hamza", "Ali", "Aya", "Omar"}
ai_workshop = {"Aya", "Naim", "Hamza", "Zakaria"}

# Your code here:

attended_both = python_workshop.intersection(ai_workshop) # or python_workshop & ai_workshop
attended_only_python = python_workshop.difference(ai_workshop) # or python_workshop - ai_workshop
attended_at_least_one = python_workshop.union(ai_workshop) # or python_workshop | ai_workshop

print(f"Students who attended both workshops: {attended_both}")
print(f"Students who attended only the Python workshop: {attended_only_python}")
print(f"All students who attended at least one workshop: {attended_at_least_one}")

print("-"*20)
# ----------------------------------------------------------------

# Exercise 3: Set Modification
# 1. Create a set 'my_fruits' with "apple", "banana".
# 2. Add "cherry" and "mango" to the set.
# 3. Remove "banana" using .discard().
# 4. Check if "apple" is in the set and print the result.

# Your code here:

my_fruits = {"apple","banana"}
my_fruits.update(["cherry","mango"])
my_fruits.discard("banana")

if "apple" in my_fruits:
    print("apple is found")

print("-"*20)
print(my_fruits)


# ----------------------------------------------------------------

# Exercise 4: Symmetric Difference
# Use the '^' operator to find items that are in either 'set_x' 
# or 'set_y', but not in both.
set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}

# Your code here:
print("-"*20)

either_set_x_y=set_x.symmetric_difference(set_y) # or use ^ operator (set_x ^ set_y)
print(either_set_x_y)

print("-"*20)

