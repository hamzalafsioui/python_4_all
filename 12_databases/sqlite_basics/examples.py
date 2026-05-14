# Examples: Creating and Querying a Database

import sqlite3
import os

# Get current directory to save the database file next to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "demo.db")

def setup_database():
    # 1. Connect (creates the file if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 2. Create a Table
    print("Creating 'students' table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade INTEGER
        )
    """)
    conn.commit()
    return conn

def insert_data(conn):
    cursor = conn.cursor()
    # 3. Insert Data (using placeholders for safety)
    print("Inserting students...")
    students = [("Hamza", 95), ("Ali", 88), ("Sara", 92)]
    cursor.executemany("INSERT INTO students (name, grade) VALUES (?, ?)", students)
    conn.commit()

def query_data(conn):
    cursor = conn.cursor()
    # 4. Read Data
    print("\nReading students from database:")
    cursor.execute("SELECT * FROM students")
    
    # fetchall() returns a list of tuples
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Grade: {row[2]}")

def cleanup(conn):
    # Always close the connection
    conn.close()
    print("\nDatabase connection closed.")

# --- Execution ---
if __name__ == "__main__":
    connection = setup_database()
    insert_data(connection)
    query_data(connection)
    cleanup(connection)
