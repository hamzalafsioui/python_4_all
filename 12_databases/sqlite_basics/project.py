"""
PROJECT: Personal Contact Manager

Goal: Build a terminal application that manages a list of contacts stored in a database.

Requirements:

1. Setup:
   - Create 'contacts.db'.
   - Table 'contacts': 'id', 'name', 'phone', 'email'.

2. Features (Functions):
   - 'add_contact(name, phone, email)': Inserts a new row.
   - 'list_contacts()': Selects all rows and prints them nicely.
   - 'search_contact(name)': Searches for a specific name and prints their info.
   - 'delete_contact(id)': Removes a contact by their ID.

3. Persistence Test:
   - Run the script and add 2 contacts.
   - Stop the script.
   - Run the script again and use 'list_contacts()'. The data should still be there!

Real-World Logic:
- This is the foundation of almost every app you use. Whether it's your phone's contact list or a giant CRM like Salesforce, it all boils down to these basic SQL operations.
"""

import sqlite3
import os

# TODO: Implement the Contact Manager

# Get current directory to save the database file next to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "contacts.db")

def create_connection():
    """Create a connection to the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        print("Connected to database.")
        return conn
    except sqlite3.Error as e:
        print(e)

def close_connection(conn):
    """Close the database connection."""
    try:
        conn.close()
        print("Connection closed.")
    except sqlite3.Error as e:
        print(e)

def create_table(conn):
    """Create the contacts table."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT
            )
        """)
        conn.commit()
        print("Table 'contacts' created successfully.")
    except sqlite3.Error as e:
        print(e)

def add_contact(conn, name, phone, email):
    """Add a new contact to the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        print(f"Contact '{name}' added successfully.")
    except sqlite3.Error as e:
        print(e)

def list_contacts(conn):
    """List all contacts in the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        print("\nAll contacts:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def search_contact(conn, name):
    """Search for a specific contact by name."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ("%" + name + "%",))
        rows = cursor.fetchall()
        print(f"\nSearch results for '{name}':")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def delete_contact(conn, id):
    """Delete a contact by their ID."""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (id,))
        conn.commit()
        print(f"Contact with ID {id} deleted successfully.")
    except sqlite3.Error as e:
        print(e)

if __name__ == "__main__":
   conn = create_connection()
   create_table(conn)
   while True:
      print("\n1. Add Contact")
      print("2. List Contacts")
      print("3. Search Contact")
      print("4. Delete Contact")
      print("5. Exit")
      choice = int(input("Enter your choice: "))
      if choice == 1:
         name = input("Enter contact name: ")
         phone = input("Enter contact phone: ")
         email = input("Enter contact email: ")
         add_contact(conn, name, phone, email)
      elif choice == 2:
         list_contacts(conn)
      elif choice == 3:
         name = input("Enter contact name: ")
         search_contact(conn, name)
      elif choice == 4:
         id = int(input("Enter contact ID: "))
         delete_contact(conn, id)
      elif choice == 5:
         close_connection(conn)
         break
      else:
         print("Invalid choice. Please try again.")
         
