"""
PROJECT: Automated File Organizer

Goal: Create a script that cleans up a "Downloads" folder by moving files into subfolders based on their extensions.

Requirements:

1. Setup:
   - Create a directory named 'downloads_mock'.
   - Create several dummy files inside: 'test.jpg', 'data.pdf', 'script.py', 'vacation.jpg', 'resume.pdf'.

2. The Organizer Logic:
   - Define a dictionary of categories:
     CATEGORIES = {
         "Images": [".jpg", ".png", ".jpeg"],
         "Documents": [".pdf", ".docx", ".txt"],
         "Code": [".py", ".js", ".html"]
     }
   - Loop through every file in 'downloads_mock'.
   - For each file, check its extension (using os.path.splitext).
   - Move the file into the corresponding category folder.
   - If the category folder doesn't exist, create it!

Real-World Logic:
- This is a very common automation task. You can schedule this script to run once a week to keep your computer clean.
- Use 'os.rename(src, dst)' to move files.
"""

# TODO: Implement the File Organizer
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads_mock")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

if __name__ == "__main__":
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)
    with open(os.path.join(DOWNLOADS_DIR, "test.jpg"), "w") as f:
        f.write("Test jpg")
    with open(os.path.join(DOWNLOADS_DIR, "data.pdf"), "w") as f:
        f.write("Test pdf")
    with open(os.path.join(DOWNLOADS_DIR, "script.py"), "w") as f:
        f.write("Test py")
    with open(os.path.join(DOWNLOADS_DIR, "vacation.jpg"), "w") as f:
        f.write("Test vacation")
    with open(os.path.join(DOWNLOADS_DIR, "resume.pdf"), "w") as f:
        f.write("Test resume")

    CATEGORIES = {
         "Images": [".jpg", ".png", ".jpeg"],
         "Documents": [".pdf", ".docx", ".txt"],
         "Code": [".py", ".js", ".html"]
     }
    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)
        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(filename)
            for category, extensions in CATEGORIES.items():
                if file_extension in extensions:
                    category_dir = os.path.join(DOWNLOADS_DIR, category)
                    os.makedirs(category_dir, exist_ok=True)
                    shutil.move(file_path, category_dir)
                    break

    
