"""
EXERCISE: The Architect

1. Create a folder structure like this:
   shapes/
   ├── __init__.py
   ├── square.py (contains area(side))
   └── circle.py (contains area(radius))

2. In THIS file (exercise.py), import both area functions.
3. Calculate the area of a square (side=4) and a circle (radius=3).

Hint: You'll need to use 'os.makedirs' and 'open' if you want to create 
these files via code, or just create them manually in your editor.
"""

# TODO: Create the package structure and import it

import os
import sys

# Directory where this script exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Add this directory to Python path
sys.path.append(BASE_DIR)

# Create shapes folder inside current script directory
shapes_dir = os.path.join(BASE_DIR, "shapes")
os.makedirs(shapes_dir, exist_ok=True)

# Create __init__.py
with open(os.path.join(shapes_dir, "__init__.py"), "w") as f:
    f.write("# Shapes Package\n")

# square.py
with open(os.path.join(shapes_dir, "square.py"), "w") as f:
    f.write(
        "def area(side):\n"
        "    return side * side\n"
    )

# circle.py
with open(os.path.join(shapes_dir, "circle.py"), "w") as f:
    f.write(
        "from math import pi\n\n"
        "def area(radius):\n"
        "    return pi * radius * radius\n"
    )

# Import modules
from shapes import square
from shapes import circle

square_area = square.area(4)
circle_area = circle.area(3)

print(f"Square area: {square_area}")
print(f"Circle area: {circle_area}")