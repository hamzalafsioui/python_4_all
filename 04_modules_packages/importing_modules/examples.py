# Examples: Mastering Imports

# 1_ Simple Import
import math
print(f"Standard Pi: {math.pi}")

# 2_ Specific Imports
from os import getcwd, listdir
print(f"Current Directory: {getcwd()}")
print(f"Files here: {listdir('.')[:3]}") # Show first 3 files

# 3_ Aliasing (Common for long names or conflicts)
import random as rnd
print(f"Random Choice [A, B, C]: {rnd.choice(['A', 'B', 'C'])}")

# 4_ Combining them
from datetime import datetime as dt
print(f"Current Year: {dt.now().year}")

# 5_ Importing multiple items
from math import floor, ceil
val = 4.7
print(f"Floor of {val}: {floor(val)}")
print(f"Ceil of {val}: {ceil(val)}")
