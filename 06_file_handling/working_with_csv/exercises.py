"""
EXERCISES: The Grade Calculator

Task:
1. Create a file named 'students.csv' with the following content:
   Name,Math,Science,English
   Hamza,85,90,88
   Omar,70,80,75
   Brahim,60,65,70

2. Read the file using csv.DictReader.
3. For each student, calculate their average grade.
4. Print a report like:
   Hamza: 87.67
   Omar: 75.00
   Brahim: 65.00
"""

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENTS_PATH = os.path.join(BASE_DIR, "students.csv")


def create_csv_file():
    # Create the CSV file with sample data
    with open(STUDENTS_PATH, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Name", "Math", "Science", "English"])
        writer.writerow(["Hamza", 85, 90, 88])
        writer.writerow(["Omar", 70, 80, 75])
        writer.writerow(["Brahim", 60, 65, 70])


def calculate_averages():
    # Read the CSV file
    with open(STUDENTS_PATH, "r") as f:
        reader = csv.DictReader(f)

        # Calculate and print averages
        for row in reader:
            math = int(row["Math"])
            science = int(row["Science"])
            english = int(row["English"])

            average = (math + science + english) / 3

            print(f"{row['Name']}: {average:.2f}")


if __name__ == "__main__":
    create_csv_file()
    calculate_averages()

