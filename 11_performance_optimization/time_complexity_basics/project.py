"""
PROJECT: The High-Speed Search Engine (Simulator)

Goal: Prove why Time Complexity matters by building a search tool for a massive database.

Requirements:

1. Data Setup:
   - Create a list of 100,000 dictionaries representing "Products":
     [{"id": 0, "name": "Product 0"}, {"id": 1, "name": "Product 1"}, ...]

2. Task 1: Naive Search (O(n))
   - Write a function 'find_product_list(product_id)':
     - Loops through the list until it finds the dictionary with that ID.

3. Task 2: Optimized Search (O(1))
   - Create a dictionary where the keys are IDs and values are the Product objects.
   - Write a function 'find_product_dict(product_id)':
     - Look up the ID directly in the dictionary.

4. The Comparison:
   - Run both functions for the ID 99,999.
   - Use 'time.time()' to measure and print the results for both.
   - You should see the dictionary search is almost 1,000x faster!

Real-World Logic:
- This is exactly why databases use "Indexes." An index is essentially a dictionary (hash map) that lets the database find data in O(1) time instead of scanning the whole hard drive in O(n) time.
"""

import time

# TODO: Implement the High-Speed Search Engine

products = []
for i in range(100_000):
    products.append({"id": i, "name": f"Product {i}"})

def find_product_list(product_id):
    start = time.time()
    for product in products:
        if product["id"] == product_id:
            end = time.time()
            return product, round(end - start, 6)
    return None, None

product_dict = {product["id"]: product for product in products}

def find_product_dict(product_id):
    start = time.time()
    end = time.time()
    return product_dict[product_id], round(end - start, 6)

if __name__ == "__main__":
    print("Task 1: Naive Search")
    product, time_taken = find_product_list(99_999)
    print(product, "Time taken: ", time_taken)
    
    print("\nTask 2: Optimized Search")
    product, time_taken = find_product_dict(99_999)
    print(product, "Time taken: ", time_taken)

