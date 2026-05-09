"""
PROJECT: Inventory Management System

Goal: Manage a product inventory stored in a CSV file.

Requirements:
1. The CSV file 'inventory.csv' should have columns: 'ID', 'Name', 'Price', 'Quantity'.
2. Menu:
   1. View Inventory
   2. Add Product
   3. Update Quantity
   q. Quit
3. View Inventory: Display all products in a nice table-like format.
4. Add Product: Append a new row to the CSV.
5. Update Quantity:
   - Ask for a Product ID.
   - Read the whole CSV.
   - Update the quantity for that ID in the list of dictionaries.
   - Overwrite the CSV with the updated list.
"""

# TODO: Implement the Inventory System
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_PATH = os.path.join(BASE_DIR, "inventory.csv")

def main():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Update Quantity")
        print("q. Quit")
        choice = input("Enter your choice: ").strip().lower()
        match choice:
            case "1":
                view_inventory()
            case "2":
                add_product()
            case "3":
                update_quantity()
            case "q":
                print("Exiting the application...")
                break

def view_inventory():
    create_csv_file()
    with open(INVENTORY_PATH, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"ID: {row['ID']}\nName: {row['Name']}\nPrice: {row['Price']}\nQuantity: {row['Quantity']}\n")
            print("-"*20 + "\n")


def add_product():
    id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    quantity = input("Enter product quantity: ")
    with open(INVENTORY_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, name, price, quantity])


def update_quantity():
    id = input("Enter product ID: ")
    with open(INVENTORY_PATH, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    for row in rows:
        if row["ID"] == id:
            row["Quantity"] = input("Enter new quantity: ")
            break
    with open(INVENTORY_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Price", "Quantity"])
        writer.writeheader()
        writer.writerows(rows)

def create_csv_file():
   if os.path.exists(INVENTORY_PATH):
       return
   with open(INVENTORY_PATH, "w", newline="") as f:
       writer = csv.writer(f)
       writer.writerow(["ID", "Name", "Price", "Quantity"])
   

if __name__ == "__main__":
    main()
