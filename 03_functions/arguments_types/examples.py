"""
Examples: Functions - Argument Types
This script demonstrates the flexibility of Python arguments.
"""

# ================== (1) Positional vs Keyword =======================
def create_profile(name, age, city):
    print(f"Profile: {name}, {age} years old, from {city}")

# Positional (order must match)
create_profile("Hamza", 25, "Casablanca")

# Keyword (order doesn't matter)
create_profile(city="Rabat", name="Ali", age=30)

print("-" * 20)

# ================== (2) Default Parameters =======================
def send_email(to, subject="No Subject", body="--- empty ---"):
    print(f"To:      {to}")
    print(f"Subject: {subject}")
    print(f"Body:    {body}")
    print("Email Sent!")

send_email("dev@python.com") # Uses defaults
send_email("hamza@test.com", "Hello!", "This is a test.")

print("-" * 20)

# ================== (3) *args (Multiple Positional) =======================
def list_skills(name, *skills):
    print(f"{name}'s skills:")
    for skill in skills:
        print(f"- {skill}")

list_skills("Hamza", "Python", "JavaScript", "SQL", "Docker")

print("-" * 20)

# ================== (4) **kwargs (Multiple Keywords) =======================
def print_data(**data):
    # data is a dictionary
    for key, value in data.items():
        print(f"{key}: {value}")

print_data(brand="Apple", model="M2", year=2023, color="Silver")
