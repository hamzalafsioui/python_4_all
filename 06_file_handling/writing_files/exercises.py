"""
EXERCISES: The Personal Diary

Task:
1. Ask the user to input a note or a thought.
2. Get the current date and time using the 'datetime' module.
3. Append the note to a file named 'diary.txt' in the following format:
   [YYYY-MM-DD HH:MM:SS] - Your note here
4. Ensure the file is not overwritten—each new note should appear on a new line at the end.
"""

import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIARY_PATH = os.path.join(BASE_DIR, "diary.txt")

def add_entry():
    note = input("Enter your note/thought today: ")

    # Get current date and time
    current_date = datetime.now()

    # Format the entry
    entry = f"[{current_date.strftime('%Y-%m-%d %H:%M:%S')}] - {note}\n"

    # Append the entry to the diary file
    with open(DIARY_PATH, "a", encoding="utf-8") as diary_file:
        diary_file.write(entry)

    print("Your diary entry has been saved!")

if __name__ == "__main__":
    add_entry()