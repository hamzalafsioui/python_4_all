"""
Examples: Functions - Lambda Functions
This script demonstrates the power of anonymous functions.
"""

# ================== (1) Basic Lambdas =======================
add = lambda a, b: a + b
print(f"Sum: {add(10, 20)}")

power = lambda base, exp: base ** exp
print(f"Power: {power(2, 3)}")

print("-" * 20)

# ================== (2) Sorting with Lambdas =======================
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200}
]

# Sort by price (Low to High)
by_price = sorted(products, key=lambda item: item["price"])
print("Products by price:")
for p in by_price:
    print(f"- {p['name']}: ${p['price']}")

print("-" * 20)

# ================== (3) Map and Filter =======================
nums = [1, 5, 8, 10, 15, 20]

# Filter: Keep numbers > 10
above_ten = list(filter(lambda x: x > 10, nums))
print(f"Greater than 10: {above_ten}")

# Map: Triple all numbers
tripled = list(map(lambda x: x * 3, nums))
print(f"Tripled: {tripled}")

print("-" * 20)

# ================== (4) Combined Usage =======================
# Get only the names of expensive products
expensive_names = list(map(
    lambda p: p["name"], 
    filter(lambda p: p["price"] > 100, products)
))
print(f"Expensive Product Names: {expensive_names}")


