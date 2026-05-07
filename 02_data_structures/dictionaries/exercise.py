"""
Exercises: Data Structures - Dictionaries
"""

# Exercise 1: Create and Access
# 1. Create a dictionary named 'student' with: name, age, grade, and subjects (a list).
# 2. Print the student's name.
# 3. Print the number of subjects the student is taking.

# Your code here:

student = {"name": "Ali", "age": 20, "grade": "A", "subjects": ["Math", "Science", "History"]}
print(student["name"])
print(len(student["subjects"]))

print("-"*20)

# ----------------------------------------------------------------

# Exercise 2: Updates & Safety
# 1. Add a new key 'is_enrolled' and set it to True.
# 2. Use .get() to print the student's 'phone_number'. 
#    If it doesn't exist, print "Unknown".
# 3. Update the 'grade' to "A+".

# Your code here:

student["is_enrolled"] = True
print(student.get("phone_number", "Unknown"))
student["grade"] = "A+"
print(student)

print("-"*20)

# ----------------------------------------------------------------

# Exercise 3: Looping
# Use a for loop to print all keys and values in the following dictionary 
# in the format: "The capital of [Country] is [City]".
capitals = {
    "France": "Paris",
    "Morocco": "Rabat",
    "Japan": "Tokyo",
    "Canada": "Ottawa"
}

# Your code here:

for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")

print("-"*20)

# ----------------------------------------------------------------

# Exercise 4: Dictionary from Lists (Bonus)
# Combine the two lists below into a dictionary named 'fruit_prices'.
# Hint: Use the zip() function or a loop.
fruits = ["apple", "banana", "orange"]
prices = [0.5, 0.25, 0.75]

# Your code here:

print(dict(zip(fruits, prices))) 


fruit_prices = {}
for fruit, price in zip(fruits, prices):
    fruit_prices[fruit] = price
print(fruit_prices)

print("-"*20)

# zip is a function that combines two iterables into pairs. but we need dict() to convert the pairs into a dictionary. 

# ----------------------------------------------------------------


