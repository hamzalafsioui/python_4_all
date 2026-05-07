"""
Examples: Data Structures - Dictionaries
This script demonstrates common dictionary operations and methods.
"""

# ================== (1) Basic Operations =======================
car = {
    "brand": "Tesla",
    "model": "Model 3",
    "year": 2023,
    "colors": ["White", "Black", "Red"]
}

print(f"Brand: {car['brand']}")
print(f"Year:  {car.get('year')}")

print("-" * 20)

# ================== (2) Modifying and Adding =======================
car["year"] = 2024
car["price"] = 45000
print(f"Updated Car: {car}")

print("-" * 20)

# ================== (3) Looping through items =======================
print("Car details:")
for key, value in car.items():
    if key == "colors":
        print(f"{key.capitalize()}: {', '.join(value)}")
    else:
        print(f"{key.capitalize()}: {value}")

print("-" * 20)

# ================== (4) Dictionary Methods =======================
# pop() returns the value of the removed key
removed_val = car.pop("price")
print(f"Removed price: {removed_val}")
print(f"Keys left: {list(car.keys())}")

print("-" * 20)

# ================== (5) Nested Dictionaries =======================
users = {
    "user1": {"name": "Hamza", "score": 90},
    "user2": {"name": "Ali", "score": 85}
}

print(f"User 1 Name: {users['user1']['name']}")
