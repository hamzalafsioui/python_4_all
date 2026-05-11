"""
EXERCISES: The Guardian of Resources

EXERCISE 1: The Database Simulator
1. Create a class-based context manager 'DatabaseConnection'.
2. '__enter__' should print "Connecting to DB..." and return a dummy connection object (a string).
3. '__exit__' should print "Committing changes and Closing connection...".
4. Test it using a 'with' statement.

EXERCISE 2: The HTML Tagger
1. Create a function-based context manager using @contextmanager called 'html_tag(tag)'.
2. It should print the opening tag (e.g., "<html>").
3. Yield.
4. Print the closing tag (e.g., "</html>").
5. Test it:
   with html_tag("body"):
       print("Hello World")

EXERCISE 3: Exception Handler
1. Create a context manager 'IgnoreError(error_type)'.
2. In '__exit__', if the exception matches 'error_type', return True to suppress it.
"""

# TODO: Implement the exercises below
from contextlib import contextmanager

class DatabaseConnection:
    def __init__(self):
        self.connection = None
    
    def __enter__(self):
        print("Connecting to DB...")
        self.connection = "Database Connection"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Committing changes and Closing connection...")
        self.connection = None

@contextmanager
def html_tag(tag):
    print(f"<{tag}>")
    yield
    print(f"</{tag}>")

class IgnoreError:
    def __init__(self, error_type):
        self.error_type = error_type
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.error_type:
            print(f"Suppressed {exc_type}")
            return True

if __name__ == "__main__":
    db = DatabaseConnection()
    with db:
        print("Doing some database operations...")
        
    with html_tag("body"):
        print("Hello World")
    
    with IgnoreError(ZeroDivisionError):
        result = 10 / 0

