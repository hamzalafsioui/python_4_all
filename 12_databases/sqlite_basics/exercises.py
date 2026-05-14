"""
EXERCISES: The Database Architect

EXERCISE 1: Book Collection
1. Create a database 'library.db'.
2. Create a table 'books' with columns: 'id', 'title', 'author', 'year'.
3. Insert 3 books by different authors.
4. Commit your changes.

EXERCISE 2: Filtering Data
1. Write a query to select all books written after the year 2010.
2. Print the titles of those books.

EXERCISE 3: Updating Records
1. Change the 'year' of one of your books using an 'UPDATE' statement.
2. Delete one book from the table using its 'id'.
3. Print the final list of books to verify.
"""

import sqlite3
import os

# TODO: Implement the exercises below

# Get current directory to save the database file next to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "library.db")

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        print(f"Connected to {DB_PATH}")
    except sqlite3.Error as e:
        print(e)
    return conn

conn = create_connection()

def create_table(conn):
    """Create the books table."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER
            )
        """)
        conn.commit()
        print("Table 'books' created successfully.")
    except sqlite3.Error as e:
        print(e)

def insert_books(conn):
    """Insert sample books into the database."""
    try:
        cursor = conn.cursor()
        books = [
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
            ("To Kill a Mockingbird", "Harper Lee", 1960),
            ("1984", "George Orwell", 1949)
        ]
        cursor.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books)
        conn.commit()
        print(f"Inserted {len(books)} books.")
    except sqlite3.Error as e:
        print(e)

def query_books(conn):
    """Query books written after 1960."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM books WHERE year > 1960")
        rows = cursor.fetchall()
        print("\nBooks published after 1960:")
        for row in rows:
            print(row[0])
    except sqlite3.Error as e:
        print(e)

def update_book(conn, book_id, new_year):
    """Update the year of a specific book."""
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET year = ? WHERE id = ?", (new_year, book_id))
        conn.commit()
        print(f"Book with ID {book_id} updated to year {new_year}.")
    except sqlite3.Error as e:
        print(e)

def delete_book(conn, book_id):
    """Delete a book by its ID."""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        print(f"Book with ID {book_id} deleted.")
    except sqlite3.Error as e:
        print(e)

def select_all_books(conn):
    """Print all books in the table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        print("\nAll books in the database:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def close_connection(conn):
    """Close the database connection."""
    try:
        conn.close()
        print("Connection closed.")
    except sqlite3.Error as e:
        print(e)

        
if __name__ == "__main__":
    conn = create_connection()
    create_table(conn)
    insert_books(conn)
    query_books(conn)
    update_book(conn, 1, 1926)
    delete_book(conn, 2)
    select_all_books(conn)
    close_connection(conn)
