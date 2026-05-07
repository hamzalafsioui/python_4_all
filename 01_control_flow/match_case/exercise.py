"""
Exercises: Control Flow - Match Case
"""

# Exercise 1: File Extension Checker
# Write a match statement that takes a file extension (string) 
# and prints the file type:
# - .jpg, .jpeg, .png -> "Image file"
# - .mp4, .mkv -> "Video file"
# - .py -> "Python script"
# - anything else -> "Unknown format"

extension = ".py"

# Your code here:

match extension:
    case ".jpg" | ".jpeg" | ".png":
        print("Image file")
    case ".mp4" | ".mkv":
        print("Video file")
    case ".py":
        print("Python script")
    case _:
        print("Unknown format")


# ----------------------------------------------------------------

# Exercise 2: Grade Converter
# Use a match statement with guards to print:
# - 90-100: "Excellent"
# - 70-89: "Good"
# - 50-69: "Pass"
# - < 50: "Fail"

score = 85

# Your code here:

match score:
    case value if 90 <= value <= 100:
        print("Excellent")
    case value if 70 < value <= 89:
        print("Good")
    case value if 50 < value <= 69:
        print("Pass")
    case value if value < 50:
        print("Fail")
    case _:
        print("Invalid score")


# ----------------------------------------------------------------

# Exercise 3: User Role Access
# match a tuple (role, is_authenticated)
# - ("admin", True) -> "Full access"
# - ("user", True) -> "Limited access"
# - (_, False) -> "Please log in"

user_data = ("admin", False)

# Your code here:

match user_data:
    case ("admin", True):
        print("Full access")
    case ("user", True):
        print("Limited access")
    case (_, False):
        print("Please log in")
    case _:
        print("Unknown user")