"""
PROJECT: The Book Collection API (Flask Edition)

Goal: Build a REST API using Flask to manage a library of books.

Requirements:

1. Data Setup:
   - Create a list of dictionaries: 'books = [{"id": 1, "title": "The Alchemist", "author": "Paulo Coelho"}]'

2. The Routes:
   - 'GET /books': Returns the list of all books.
   - 'POST /books': Receives a JSON object with 'title' and 'author', assigns an ID, and adds it to the list.
   - 'GET /books/<int:book_id>': Returns a single book or a 404 error if not found.
   - 'DELETE /books/<int:book_id>': Removes the book from the list.

3. Testing:
   - Run the script: python project.py
   - Use a tool like Postman or 'curl' (or just your browser for GET requests).
   - Add a new book, then delete the original one.

Real-World Logic:
- While FastAPI is the "new kid on the block," Flask is the foundation of millions of websites. Understanding both gives you the flexibility to work on any Python codebase in the world!
"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# TODO: Implement the Book Collection API


books = [
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho"
    }
]



@app.get("/books")
def get_books():

    return jsonify(books)



@app.post("/books")
def create_book():

    data = request.json

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(new_book)

    return jsonify(new_book), 201



@app.get("/books/<int:book_id>")
def get_book(book_id):

    for book in books:

        if book["id"] == book_id:
            return jsonify(book)

    abort(404)



@app.delete("/books/<int:book_id>")
def delete_book(book_id):

    for book in books:

        if book["id"] == book_id:

            books.remove(book)

            return jsonify({
                "message": "Book deleted"
            })

    abort(404)


if __name__ == "__main__":
    app.run(debug=True)