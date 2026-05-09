"""
PROJECT: The Library Management System (Mini)

Goal: Build a system that manages books using objects.

Requirements:

1. Class 'Book':
   - Attributes: 'title', 'author', 'is_borrowed' (default False).
   - Method 'mark_as_borrowed()': Sets is_borrowed to True.
   - Method 'mark_as_returned()': Sets is_borrowed to False.

2. Class 'Library':
   - Attribute 'books': A list that will hold 'Book' objects.
   - Method 'add_book(book_obj)': Adds a Book instance to the list.
   - Method 'show_available_books()': Prints all books that are NOT borrowed.
   - Method 'borrow_book(title)': Finds a book by title and marks it as borrowed.

Best Practice:
- Use a loop in the main block to allow the user to interact with your library.
- Store your Book objects inside the Library's list attribute.
"""

# TODO: Implement the Library System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True
        print(f'"{self.title}" has been borrowed.')

    def mark_as_returned(self):
        self.is_borrowed = False
        print(f'"{self.title}" has been returned.')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added to the library.')

    def show_available_books(self):
        print("\nAvailable Books:")
        found = False

        for book in self.books:
            if not book.is_borrowed:
                print(f'- {book.title} by {book.author}')
                found = True

        if not found:
            print("No available books.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():

                if book.is_borrowed:
                    print("Book is already borrowed.")
                else:
                    book.mark_as_borrowed()

                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():

                if not book.is_borrowed:
                    print("Book was not borrowed.")
                else:
                    book.mark_as_returned()

                return

        print("Book not found.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'"{title}" removed from the library.')
                return

        print("Book not found.")


if __name__ == "__main__":

    library = Library()

    while True:
        print("\n" + "=" * 40)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Book")
        print("2. Show Available Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Remove Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")

            book = Book(title, author)
            library.add_book(book)

        elif choice == "2":
            library.show_available_books()

        elif choice == "3":
            title = input("Enter title to borrow: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("Enter title to return: ")
            library.return_book(title)

        elif choice == "5":
            title = input("Enter title to remove: ")
            library.remove_book(title)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")