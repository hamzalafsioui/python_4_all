"""
Mini-Project: Inventory Management System

A simple system to track product stock and prices using dictionaries.
"""

# 1_ Initialize Inventory
# Format: product_id: {"name": str, "price": float, "stock": int}
inventory = {
    101: {"name": "Laptop", "price": 1200.0, "stock": 5},
    102: {"name": "Mouse", "price": 25.0, "stock": 50},
    103: {"name": "Monitor", "price": 200.0, "stock": 10}
}

def display_inventory():
    print("\n" + "=" * 40)
    print(f"{'ID':<5} {'Product':<15} {'Price':<10} {'Stock':<5}")
    print("-" * 40)
    for pid, info in inventory.items():
        print(f"{pid:<5} {info['name']:<15} ${info['price']:<9} {info['stock']:<5}")
    print("=" * 40)

# 2_ Update Stock
def update_stock(pid, quantity):
    if pid in inventory:
        inventory[pid]["stock"] += quantity
        print(f"\n[OK] Updated {inventory[pid]['name']} stock by {quantity}.")
    else:
        print("\n[ERR] Product ID not found.")

# 3_ Calculate Total Value
def calculate_total_value():
    total = 0
    for info in inventory.values():
        total += info["price"] * info["stock"]
    return total

# --- Simulation ---
display_inventory()

update_stock(102, -5) # 5 mice sold
update_stock(103, 2)  # 2 monitors restocked

display_inventory()

total_val = calculate_total_value()
print(f"Total Warehouse Value: ${total_val:,}")
