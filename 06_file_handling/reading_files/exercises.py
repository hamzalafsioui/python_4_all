"""
EXERCISES: The Word Counter

Task:
1. Create a file named 'data.txt' with a few sentences about Python.
2. Read the file.
3. Calculate and print:
   - The total number of characters in the file.
   - The total number of words in the file.
   - The number of times the word 'Python' appears (case-insensitive).
"""

# TODO: Implement the word counter
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data.txt")

with open(FILE_PATH, "r") as f:
    content = f.read()
    print(content)

    # total number of characters
    print("total number of characters: ",len(content))

    # total number of words
    print("total number of words: ",len(content.split()))

    # number of times 'Python' appears (case-insensitive)
    print(content.lower().count('python'))