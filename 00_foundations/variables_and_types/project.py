"""
Mini-Project: User Profile Generator

In this project, you will create a script that stores user information 
and prints a formatted profile.
"""

# =================== (1) Define user data =============================
# Use appropriate data types for each field.
first_name = "Hamza"
last_name = "Developer"
age = 28
height_meters = 1.75
is_student = False
hobbies = "Coding, Reading, Gaming"

# =================== (2) Perform some simple calculations or conversions =============================
# Convert age to string for concatenated messages if needed (though f-strings handle this).
# Calculate age in 10 years.
age_in_10_years = age + 10

# =================== (3) Print the profile in a beautiful way =============================
print("=" * 30)
print("       USER PROFILE")
print("=" * 30)
print(f"Full Name:  {first_name} {last_name}")
print(f"Age:        {age} years old")
print(f"Height:     {height_meters}m")
print(f"Student:    {'Yes' if is_student else 'No'}")
print(f"Hobbies:    {hobbies}")
print("-" * 30)
print(f"In 10 years, {first_name} will be {age_in_10_years} years old.")
print("=" * 30)
