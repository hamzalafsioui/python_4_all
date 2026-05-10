# Examples: Operator Overloading & Representation

class Vector:
    """A simple 2D vector class."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        """User friendly print."""
        return f"Vector({self.x}, {self.y})"
        
    def __repr__(self):
        """Developer friendly representation."""
        return f"Vector(x={self.x}, y={self.y})"
        
    def __add__(self, other):
        """Allows: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
        
    def __eq__(self, other):
        """Allows: v1 == v2"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    def __len__(self):
        """Allows: len(my_book)"""
        return self.pages

# --- Usage ---
v1 = Vector(2, 4)
v2 = Vector(5, -2)

# Test Representation
print(f"v1: {v1}") # Calls __str__

# Test Addition
v3 = v1 + v2 # Calls __add__
print(f"v1 + v2 = {v3}")

# Test Equality
print(f"Is v1 == v2? {v1 == v2}")
print(f"Is v1 == Vector(2, 4)? {v1 == Vector(2, 4)}")

# Test Length
my_book = Book("Python Mastery", 450)
print(f"The book '{my_book.title}' is {len(my_book)} pages long.")
