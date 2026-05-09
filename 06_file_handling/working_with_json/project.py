"""
PROJECT: JSON Contact Book

Goal: Create a contact manager that saves data to a JSON file.

Requirements:
1. The script should maintain a list of contacts. Each contact is a dictionary:
   {"name": "Hamza", "phone": "123-456", "email": "hamza@example.com"}
2. Menu:
   1. Show all contacts
   2. Add new contact
   3. Search for contact by name
   q. Quit
3. On startup, the script should load existing contacts from 'contacts.json'.
4. Every time a contact is added, the 'contacts.json' file should be updated.
5. Handle the case where 'contacts.json' doesn't exist yet (start with an empty list).
"""

# TODO: Implement the Contact Book
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACTS_PATH = os.path.join(BASE_DIR, "contacts.json")

def main():
    while True:
        print("\n--- Simple Contact Book ---")
        print("1. Show all contacts")
        print("2. Add new contact")
        print("3. Search for contact by name")
        print("q. Quit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            view_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "q":
            print("Exiting the application...")
            break

def view_contacts():
    try:
        with open(CONTACTS_PATH, "r") as f:
            contacts = json.load(f)
            print("\n--- All Contacts ---")
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    except FileNotFoundError:
        print("No contacts found.")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    contact = {"name": name, "phone": phone, "email": email}
    
    try:
        with open(CONTACTS_PATH, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []
    
    contacts.append(contact)
    with open(CONTACTS_PATH, "w") as f:
        json.dump(contacts, f, indent=4)
    
    print("Contact added successfully!")

def search_contact():
    name = input("Enter contact name to search: ")
    
    try:
        with open(CONTACTS_PATH, "r") as f:
            contacts = json.load(f)
            found_contacts = [contact for contact in contacts if contact['name'].lower() == name.lower()]
            
            if found_contacts:
                print("\n--- Search Results ---")
                for contact in found_contacts:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("No contact found with that name.")
    except FileNotFoundError:
        print("No contacts found.") 

if __name__ == "__main__":
    main()
