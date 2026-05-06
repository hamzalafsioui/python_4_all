"""
Examples: Control Flow - If/Else

"""

# ================== (1) Basic If/Else =======================
temperature = 25

if temperature > 30:
    print("It's a hot day!")
else:
    print("It's a pleasant day.")

print("-" * 20)

# ================== (2) Elif Chain =======================
# Grading system
marks = 72

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks}, Grade: {grade}")

print("-" * 20)

# ================== (3) Logical Operators =======================
has_ticket = True
has_id = False

# Using 'and'
if has_ticket and has_id:
    print("Welcome to the event!")
else:
    print("Access denied. You need both a ticket and an ID.")

# Using 'or'
is_admin = True
is_moderator = False

if is_admin or is_moderator:
    print("You have access to the dashboard.")

print("-" * 20)

# ================== (4) Nested If Statements =======================
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Negative or Zero")

print("-" * 20)

# ================== (5) Ternary Operator =======================
# result = value_if_true if condition else value_if_false
age = 16
can_vote = "Yes" if age >= 18 else "No"
print(f"Can vote? {can_vote}")
