"""
Examples: Control Flow - For Loops
"""

# ================== (1) Looping through a List =======================
colors = ["Red", "Green", "Blue"]
for color in colors:
    print(f"I like {color}")

print("-" * 20)

# ================== (2) Using range() =======================
# Sum of first 5 numbers
total = 0
for i in range(1, 6):
    total += i
print(f"Sum of 1-5: {total}")

print("-" * 20)

# ================== (3) Using enumerate() =======================
tasks = ["Laundry", "Coding", "Cooking"]
for i, task in enumerate(tasks, start=1):
    print(f"Task {i}: {task}")

print("-" * 20)

# ================== (4) Nested Loops =======================
# Create a 3x3 grid coordinate list
for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end=" ")
    print() # Newline after each row

print("-" * 20)

# ================== (5) Iterating over Dictionaries =======================
user = {"name": "Hamza", "role": "Dev", "level": 10}
for key, value in user.items():
    print(f"{key.capitalize()}: {value}")
