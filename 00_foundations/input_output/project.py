"""
Mini-Project: ID Card Generator

This project will take user information and output a formatted "ID Card" in the terminal.
"""

# 1_ Gather User Information
name = "Hamza Developer" # In a real script, use input()
job_title = "Python Wizard"
company = "Python Mastery Inc."
employee_id = 404

# 2_ Format the Card
print("\n" + "*" * 40)
print(f"*{' ' * 38}*")
print(f"*   NAME:    {name:<25}*")
print(f"*   JOB:     {job_title:<25}*")
print(f"*   COMPANY: {company:<25}*")
print(f"*   ID:      #{employee_id:<24}*")
print(f"*{' ' * 38}*")
print("*" * 40)

# Note: The :<25 syntax inside f-strings aligns the text to the left 
# with a width of 25 characters.
