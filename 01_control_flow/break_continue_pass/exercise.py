"""
Exercises: Control Flow - Break, Continue, Pass
"""

# Exercise 1: Early Exit
# Write a for loop that iterates through numbers 1 to 100.
# The loop should stop (break) if the number is divisible by 7 and 11.
# Print the number that caused the break.

# Your code here:

for num in range(1, 101):
    if num % 7 == 0 and num % 11 == 0:
        print(f"Found {num} divisible by 7 and 11")
        break
    # else:
    #     print(f"{num} is not divisible by 7 and 11")




# ----------------------------------------------------------------

# Exercise 2: Skipping Items
# Given a list of ages, use 'continue' to skip any age that is less than 18.
# Print the "Access Granted" message only for adults.
ages = [12, 25, 17, 30, 45, 10]

# Your code here:

for age in ages:
    if age < 18:
        continue
    print("Access Granted")

# ----------------------------------------------------------------

# Exercise 3: Placeholders
# Create an if-elif-else block for a "System Menu".
# Use 'pass' for the 'Settings' and 'Profile' options.
# Only implement the 'Logout' option (print "Logging out").
choice = "Settings"

# Your code here:

if choice == "Settings":
    pass
elif choice == "Profile":
    pass
elif choice == "Logout":
    print("Logging out")
else:
    print("Invalid choice")
