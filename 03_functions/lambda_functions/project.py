"""
Mini-Project: Smart Price Processor

A simple utility that applies dynamic transformations to a list of prices 
using lambda functions.
"""

# 1_ Raw Prices
prices = [100.0, 250.0, 50.0, 10.0, 500.0]

print("=" * 40)
print("       PRICE PROCESSOR PRO")
print("=" * 40)
print(f"Original: {prices}")

# 2_ Transformation Logic (using map + lambdas)
# Apply 10% discount to all items
discounted = list(map(lambda p: p * 0.9, prices))
print(f"Discount: {discounted}")

# Add 20% tax to all discounted items
final_prices = list(map(lambda p: p * 1.2, discounted))
print(f"Final:    {[round(p, 2) for p in final_prices]}")

print("-" * 40)

# 3_ Filtering Logic (using filter + lambdas)
# Find only items that are still "Luxury" (> 200 after processing)
luxury_items = list(filter(lambda p: p > 200, final_prices))
print(f"Luxury Items (> $200): {luxury_items}")

# 4_ Summary
total_revenue = sum(final_prices)
print(f"\nPotential Revenue: ${total_revenue:,.2f}")
print("=" * 40)
