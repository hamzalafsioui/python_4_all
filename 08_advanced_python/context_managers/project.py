"""
PROJECT: Safe File Backup Editor

Goal: Build a context manager that protects a file while it is being edited.

Requirements:

1. Class 'SafeEditor(file_path)':
   - In '__enter__':
     - Create a backup copy of the original file (e.g., 'original.txt.bak').
     - Return the file path for editing.
   - In '__exit__':
     - If an error occurred inside the 'with' block:
       - Restore the original file from the backup.
       - Print "ERROR: Changes discarded. Backup restored."
     - If NO error occurred:
       - Delete the backup file.
       - Print "SUCCESS: Changes saved."

Real-World Logic:
- This simulates how professional database systems or installers work: they perform a "Rollback" if something fails and a "Commit" if it succeeds.
"""

# TODO: Implement the Safe Editor

import os
import shutil


class SafeEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.backup_path = file_path + ".bak"

    def __enter__(self):
        # Create backup before editing
        shutil.copy2(self.file_path, self.backup_path)

        return self.file_path

    def __exit__(self, exc_type, exc_val, exc_tb):

        # If an exception occurred
        if exc_type is not None:

            # Restore original file
            shutil.move(self.backup_path, self.file_path)

            print("ERROR: Changes discarded. Backup restored.")

            # False = re-raise exception
            return False

        # No exception occurred
        else:
            # Delete backup
            os.remove(self.backup_path)

            print("SUCCESS: Changes saved.")

            return False


if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_FILE = os.path.join(BASE_DIR, "server.log")

    # Create original file
    with open(LOG_FILE, "w") as f:
        f.write("Original Content")

    try:
        with SafeEditor(LOG_FILE) as file_path:

            with open(file_path, "w") as f:
                f.write("New Content")

                # Simulate failure
                # raise ValueError("Something went wrong")

    except Exception as e:
        print("Caught Exception:", e)

    # Verify final file contents
    with open(LOG_FILE, "r") as f:
        print("\nFinal File Content:")
        print(f.read())