"""
EXERCISES: The Pandas Pioneer

EXERCISE 1: DataFrame from scratch
1. Create a dictionary containing data for 5 products:
   - 'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
   - 'Price': [999.99, 699.99, 399.99, 149.99, 249.99]
   - 'Quantity': [15, 30, 20, 50, 25]
2. Convert this dictionary into a Pandas DataFrame named 'inventory_df'.
3. Inspect it using '.head()', '.info()', and '.describe()'.

EXERCISE 2: Filtering Inventory
1. Write a query to filter and display products with a price less than $500.
2. Write a compound filter to display products where Price > 200 AND Quantity > 20.

EXERCISE 3: Total Asset Value
1. Add a new column to 'inventory_df' named 'TotalValue'. 
   (TotalValue should be Price * Quantity for each product).
2. Calculate the grand total value of the entire inventory (Hint: use .sum() on the new column).
3. Update the quantity of 'Tablet' to 25 and recalculate.
"""

import pandas as pd

    

# TODO: Implement the exercises above

# EXERCISE 1: DataFrame from scratch
inventory_data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'],
    'Price': [999.99, 699.99, 399.99, 149.99, 249.99],
    'Quantity': [15, 30, 20, 50, 25]
}

# 2. Convert dictionary into a DataFrame
inventory_df = pd.DataFrame(inventory_data)

# 3. Inspect the DataFrame
print("=== HEAD ===")
print(inventory_df.head())

print("\n=== INFO ===")
print(inventory_df.info())

print("\n=== DESCRIBE ===")
print(inventory_df.describe())

# EXERCISE 2: Filtering Inventory

# 1. Products with price less than $500
print("\n=== PRODUCTS WITH PRICE < 500 ===")
cheap_products = inventory_df[inventory_df['Price'] < 500]
print(cheap_products)

# 2. Products where Price > 200 AND Quantity > 20
print("\n=== PRICE > 200 AND QUANTITY > 20 ===")
filtered_products = inventory_df[
    (inventory_df['Price'] > 200) &
    (inventory_df['Quantity'] > 20)
]
print(filtered_products)

# EXERCISE 3: Total Asset Value

# 1. Add TotalValue column
inventory_df['TotalValue'] = (
    inventory_df['Price'] * inventory_df['Quantity']
)

print("\n=== DATAFRAME WITH TOTAL VALUE ===")
print(inventory_df)


# 2. Calculate grand total inventory value
grand_total = inventory_df['TotalValue'].sum()

print("\n=== GRAND TOTAL INVENTORY VALUE ===")
print(f"${grand_total:.2f}")

# 3. Update Tablet quantity to 25 and recalculate
inventory_df.loc[
    inventory_df['Product'] == 'Tablet',
    'Quantity'
] = 25

# Recalculate TotalValue after update
inventory_df['TotalValue'] = (
    inventory_df['Price'] * inventory_df['Quantity']
)

updated_total = inventory_df['TotalValue'].sum()

print("\n=== UPDATED INVENTORY ===")
print(inventory_df)

print("\n=== UPDATED GRAND TOTAL ===")
print(f"${updated_total:.2f}")

if __name__ == "__main__":
    pass
