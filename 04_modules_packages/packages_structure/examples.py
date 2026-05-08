import os
import sys

# Add the current working directory to the search path so we can import the package we're about to create
sys.path.append(os.getcwd())

# Let's create a package on the fly for this example
os.makedirs("ecommerce/inventory", exist_ok=True)

# Create __init__.py files
with open("ecommerce/__init__.py", "w") as f:
    f.write("# Ecommerce Package\n")

with open("ecommerce/inventory/__init__.py", "w") as f:
    f.write("from .stock import get_stock_count\n")

# Create a module in the sub-package
with open("ecommerce/inventory/stock.py", "w") as f:
    f.write("def get_stock_count(item):\n    return 42 # Placeholder\n")

# Now we can import it!
print("--- Importing from Package ---")
from ecommerce.inventory import stock
print(f"Stock for Laptop: {stock.get_stock_count('laptop')}")

# Using the shortcut we set up in ecommerce/inventory/__init__.py
import ecommerce.inventory
print(f"Stock for Phone (via shortcut): {ecommerce.inventory.get_stock_count('phone')}")

