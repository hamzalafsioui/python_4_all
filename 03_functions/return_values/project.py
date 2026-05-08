"""
Mini-Project: Grade Management System

In this project, we create functions that process scores and return 
meaningful data (letter grades and status).
"""

def get_letter_grade(score):
    """Converts a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def check_status(grade):
    """Returns 'Passed' or 'Failed' based on the letter grade."""
    if grade == "F":
        return "Failed"
    return "Passed"

def process_student(name, score):
    """Processes a student's data and returns a formatted string."""
    grade = get_letter_grade(score)
    status = check_status(grade)
    return f"Student: {name} | Grade: {grade} | Status: {status}"

# --- Simulation ---
students = [
    ("Hamza", 95),
    ("Ali", 72),
    ("Zakaria", 55)
]

print("=" * 45)
print("       STUDENT GRADE REPORT")
print("=" * 45)

for name, score in students:
    report = process_student(name, score) # Capturing the return value
    print(report)

print("=" * 45)
