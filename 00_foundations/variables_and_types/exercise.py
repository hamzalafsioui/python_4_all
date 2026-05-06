"""
Exercises: Variables and Data Types

"""

# Exercise 1: Create variables
# Create a variable named 'city' and assign it the name of your favorite city (string).
# Create a variable named 'population' and assign it a number (integer).
# Create a variable named 'is_capital' and assign it a boolean value.

# Your code here:
city = "Ouled Teima"
population = 30139
is_capital = False

# ----------------------------------------------------------------

# Exercise 2: Type Checking
# Print the type of each variable you created above.

# Your code here:
print(type(city))
print(type(population))
print(type(is_capital))

# ----------------------------------------------------------------

# Exercise 3: Type Conversion
# Convert the 'population' variable to a float and store it in 'population_float'.
# Convert the 'population' variable to a string and store it in 'population_str'.
# Print both new variables.

# Your code here:
population_float = float(population)
population_str = str(population)
print(population_float)
print(population_str)

# ----------------------------------------------------------------

# Exercise 4: Naming Conventions
# Fix the following variable names to follow PEP 8 (snake_case):
# UserAge = 30
# my_Favorite_Color = "Black"
# 1st_place = "Here haha"  # Hint: Variables cannot start with a number!

# Your code here:
user_age = 30
my_favorite_color = "Black"
first_place = "Here haha"

# ----------------------------------------------------------------

# Exercise 5: Multiple Assignment
# Assign the values 10, 20, and 30 to variables x, y, and z in a single line.
# Swap the values of x and y.
# Print the new values of x and y.

# Your code here:
x, y, z = 10, 20, 30
x, y = y, x
print(x)
print(y)

# ----------------------------------------------------------------
