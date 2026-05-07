"""
Exercises: Data Structures - Nested Structures
"""

# Exercise 1: Matrix Math
# 1. Access the number 5 in the matrix below.
# 2. Change the number 9 to 99.
# 3. Print the first row.
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Your code here:
print(f"1. The number 5 is at index: {numbers[1][1]}")
numbers[2][2] = 99
print(f"2. The matrix after update: {numbers}")
print(f"3. The first row is: {numbers[0]}")


# ----------------------------------------------------------------

# Exercise 2: Deep Access
# Extract the 'city' name from the following employee record.
company_data = {
    "hr": {
        "employees": [
            {"name": "Ali", "location": {"city": "Tangier", "zip": "50000"}},
            {"name": "Hamza", "location": {"city": "Casablanca", "zip": "20000"}}
        ]
    }
}

# Your code here (Target: Casablanca):
print(f"2. The city is: {company_data['hr']['employees'][1]['location']['city']}")




# ----------------------------------------------------------------

# Exercise 3: Aggregation
# Calculate the average score for 'User1' from the data below.
scores_data = {
    "User1": [85, 90, 78, 92],
    "User2": [70, 80, 75, 85]
}

# Your code here:

# Get User1's scores
user1_scores = scores_data["User1"]

# Calculate the sum
sum_of_scores = sum(user1_scores)

# Calculate the average
# Using len() to get the number of scores (which is 4)
average_score = sum_of_scores / len(user1_scores)

print(f"3. The average score for User1 is: {average_score}")

# ----------------------------------------------------------------

# Exercise 4: List of Lists to Dictionary (Bonus)
# Convert the list below into a dictionary where the first item 
# is the key and the second item is the value.
pairs = [["ID1", "Value1"], ["ID2", "Value2"], ["ID3", "Value3"]]

# Your code here:

pairs_dict = {}
for pair in pairs:
    key = pair[0]
    value = pair[1]
    pairs_dict[key] = value
print(f"4. The dictionary is: {pairs_dict}")