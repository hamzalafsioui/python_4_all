# Examples: Polymorphism in Action

from abc import ABC, abstractmethod
import math

# 1_ The Abstract Contract
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Must be implemented by all shapes."""
        pass

# 2_ Different implementations of the same interface
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2

# 3_ The Polymorphic Function
def print_area(shape):
    """
    This function doesn't care if it gets a Circle or a Square.
    It only cares that the object has an .area() method.
    """
    print(f"The area is: {shape.area():.2f}")

# --- Usage ---
my_circle = Circle(5)
my_square = Square(4)

shapes = [my_circle, my_square]

print("--- Calculating Areas Polymorphically ---")
for s in shapes:
    print_area(s)

# 4_ Built-in Polymorphism (Duck Typing)
print("\n--- Built-in Polymorphism ---")
print(f"Length of 'Hello': {len('Hello')}")
print(f"Length of [1, 2, 3]: {len([1, 2, 3])}")
