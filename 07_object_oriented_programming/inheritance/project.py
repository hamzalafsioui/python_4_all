"""
PROJECT: E-commerce Product System

Goal: Create a system to manage different types of products with shared and unique attributes.

Requirements:

1. Base Class 'Product':
   - Attributes: 'name', 'price'.
   - Method 'get_details()': Returns a string like "Name: [name], Price: $[price]".

2. Subclass 'Electronics':
   - Additional Attribute: 'warranty_months'.
   - Override 'get_details()': Include warranty info.

3. Subclass 'Clothing':
   - Additional Attributes: 'size', 'material'.
   - Override 'get_details()': Include size and material info.

4. Function 'display_catalog(products)':
   - Takes a list of products and prints the details of each.

Real-World Challenge:
- Create a list of different products (some electronic, some clothing).
- Use a loop to show the full catalog.
- Notice how 'display_catalog' doesn't care WHAT kind of product it is—it just calls 'get_details()'. This is a preview of Polymorphism!
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_details(self):
        return f"Name: {self.name}, Price: ${self.price}"

class Electronics(Product):
    def __init__(self, name, price, warranty_months):
        super().__init__(name, price)
        self.warranty_months = warranty_months
    
    def get_details(self):
        return f"Name: {self.name}, Price: ${self.price}, Warranty: {self.warranty_months} months"

class Clothing(Product):
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material
    
    def get_details(self):
        return f"Name: {self.name}, Price: ${self.price}, Size: {self.size}, Material: {self.material}"

def display_catalog(products):
    for product in products:
        print(product.get_details())

# TODO: Implement the Product Hierarchy
if __name__ == "__main__":
    products = [
        Electronics("Laptop", 1000, 12),
        Clothing("T-Shirt", 25, "L", "Cotton"),
        Electronics("Phone", 800, 12),
        Clothing("Jeans", 50, "M", "Denim")
    ]
    display_catalog(products)
