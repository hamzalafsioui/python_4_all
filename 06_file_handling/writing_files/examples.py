# Examples: Writing and Appending

import os

# Get directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1_ Overwriting a file ("w")
file_w = os.path.join(BASE_DIR, "overwrite.txt")
print(f"--- Writing to {os.path.basename(file_w)} ---")
with open(file_w, "w") as f:
    f.write("This is the original text.\n")
    f.write("Wait... if I run this again, I'll disappear!")

# 2_ Appending to a file ("a")
file_a = os.path.join(BASE_DIR, "log.txt")
print(f"--- Appending to {os.path.basename(file_a)} ---")
with open(file_a, "a") as f:
    f.write("New entry added at this moment.\n")

# 3_ Writing multiple lines
file_lines = os.path.join(BASE_DIR, "list.txt")
lines = ["Item 1\n", "Item 2\n", "Item 3\n"]
with open(file_lines, "w") as f:
    f.writelines(lines)

print("\nFiles created/updated successfully. Check your folder!")
