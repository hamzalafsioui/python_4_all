"""
EXERCISES: The System Investigator

EXERCISE 1: Folder Creator
1. Use 'os' to create a new directory named 'sandbox'.
2. Inside 'sandbox', create an empty file named 'test.log'.
3. Use 'os.path.exists' to verify both were created.
4. Finally, delete both the file and the folder using 'os.remove' and 'os.rmdir'.

EXERCISE 2: CLI Calculator
1. Write a script that takes two numbers as command-line arguments (sys.argv).
2. Add them together and print the result.
3. Handle the error if the user doesn't provide enough arguments or if the arguments aren't numbers.

EXERCISE 3: Path Splitter
1. Take a long file path string.
2. Use 'os.path.split' to separate the folder path from the filename.
3. Use 'os.path.splitext' to separate the filename from the extension.
"""

# TODO: Implement the exercises below
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SANDBOX_DIR = os.path.join(BASE_DIR, "sandbox")
TEST_FILE = os.path.join(SANDBOX_DIR, "test.log")

if __name__ == "__main__":

    # Exercise 1
    os.makedirs(SANDBOX_DIR, exist_ok=True)
    with open(TEST_FILE, "w") as f:
        f.write("Test log")
    print(os.path.exists(SANDBOX_DIR))
    print(os.path.exists(TEST_FILE))
    os.remove(TEST_FILE)
    os.rmdir(SANDBOX_DIR)

    # Exercise 2
    if len(sys.argv) != 3:
        print("Usage: python exercises.py <num1> <num2>")
    else:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            print(f"Result: {num1 + num2}")
        except ValueError:
            print("Invalid numbers provided.")

    # Exercise 3
    path = r"C:\Users\hamza\Desktop\repos\python_4_all\09_standard_library\os_sys\exercises.py"
    folder, filename = os.path.split(path)
    print("Folder:", folder)
    print("Filename:", filename)
    filename, extension = os.path.splitext(filename)
    print("Filename:", filename)
    print("Extension:", extension)
    
