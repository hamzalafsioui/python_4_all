# Examples: Reading and Writing CSVs

import csv
import os

# Get directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "employees.csv")

# 1_ Writing to CSV using DictWriter
data = [
    {"ID": "101", "Name": "Hamza", "Dept": "Engineering"},
    {"ID": "102", "Name": "Ali", "Dept": "Marketing"},
    {"ID": "103", "Name": "Ahmed", "Dept": "Design"}
]

print(f"--- Creating {os.path.basename(CSV_FILE)} ---")
with open(CSV_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Dept"])
    writer.writeheader()
    writer.writerows(data)

# 2_ Reading CSV using DictReader
print("\n--- Reading Employees ---")
with open(CSV_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"[{row['ID']}] {row['Name']} works in {row['Dept']}")

# 3_ Appending a single row
print("\n--- Appending New Employee ---")
with open(CSV_FILE, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Dept"])
    writer.writerow({"ID": "104", "Name": "Aliii", "Dept": "HR"})

print("Done! Open employees.csv to see the results.")
