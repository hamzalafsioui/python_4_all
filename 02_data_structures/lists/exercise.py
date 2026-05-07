"""
Exercises: Data Structures - Lists

Complete the following exercises to practice list manipulation.
"""

# Exercise 1: Basic Operations
# Create a list named 'colors' with 5 different color names.
# Print the third color in the list.
# Change the second color to "Black".

# Your code here:

colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
print(colors[2])
colors[1] = "Black"
print(colors)


# ----------------------------------------------------------------

# Exercise 2: List Methods
# Start with an empty list named 'shopping_list'.
# 1. Add "Milk", "Eggs", and "Bread" using .append().
# 2. Add "Butter" at the beginning of the list using .insert().
# 3. Sort the list alphabetically.
# 4. Remove "Eggs" from the list.
# 5. Print the final list and its length.

# Your code here:

shopping_list = []
shopping_list.append("Milk")
shopping_list.append("Eggs")
shopping_list.append("Bread")
shopping_list.insert(0, "Butter")
shopping_list.sort()
shopping_list.remove("Eggs")
print(shopping_list)
print(len(shopping_list))


# ----------------------------------------------------------------

# Exercise 3: Slicing
# Given the list below, extract:
# 1. The first three elements.
# 2. The last two elements.
# 3. The list in reverse order using slicing.
numbers = [10, 20, 30, 40, 50, 60, 70]

# Your code here:

first_three = numbers[:3]
last_two = numbers[-2:]
reversed_numbers = numbers[::-1]
print(first_three)
print(last_two)
print(reversed_numbers)

# ----------------------------------------------------------------

# Exercise 4: Nested Lists
# Create a 2x2 matrix (a list of 2 lists, each containing 2 numbers).
# Access and print the element in the second row and first column.

# Your code here:

matrix = [[1, 2], [3, 4]]
print(matrix[1][0])