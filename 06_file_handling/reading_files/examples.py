# Examples: Different Ways to Read Files

import os

# Get the directory where this script is located !!!!!!!!!!!!!!!!!!!!!!!!
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "sample.txt")

# 1_ Reading the whole file at once
print("--- Method 1: read() ---")
with open(FILE_PATH, "r") as f:
    content = f.read()
    print(content)

# 2_ Reading line by line
print("\n--- Method 2: readline() ---")
with open(FILE_PATH, "r") as f:
    print(f"Line 1: {f.readline().strip()}")
    print(f"Line 2: {f.readline().strip()}")

# 3_ Reading into a list
print("\n--- Method 3: readlines() ---")
with open(FILE_PATH, "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    print(f"Last line: {lines[-1].strip()}")

# 4_ Looping (The most memory-efficient way)
print("\n--- Method 4: Iterating ---")
with open(FILE_PATH, "r") as f:

    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.strip()}")
