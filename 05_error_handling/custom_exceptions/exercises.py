"""
EXERCISES: The Geometry Guardian

Task:
1. Create a custom exception called `NegativeDimensionError`.
2. Write a function `calculate_area(width, height)`:
   - If either width or height is less than or equal to 0, raise `NegativeDimensionError` with a message.
   - Otherwise, return width * height.
3. Use a try-except block to call this function and handle the custom error.
"""

# TODO: Implement the custom exception and test function

class NegativeDimensionError(Exception):
    """Raised when a dimension is negative."""
    def __init__(self, dimension, value, message="Dimension cannot be negative."):
        self.dimension = dimension
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (Your dimension: {self.dimension}, Value: {self.value})"

def calculate_area(width, height):
    if width <= 0 or height <= 0:
        raise NegativeDimensionError("Width or height", width if width <= 0 else height)
    return width * height

try:
    print(f"Area: {calculate_area(10, 20)}")
    print(f"Area: {calculate_area(-10, 20)}")
except NegativeDimensionError as e:
    print(f"Caught Custom Error: {e}")

