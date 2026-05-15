"""
PROJECT: The E-Commerce Catalog (Simulator)

Goal: Build a terminal application that browses a live product catalog using a REST API.

Requirements:

1. API Source: 
   - Use the 'FakeStoreAPI': "https://fakestoreapi.com"

2. Features:
   - 'get_categories()': 
     - Fetches and prints all available product categories from "/products/categories".
   - 'get_products_in_category(category_name)': 
     - Fetches and prints all products in that category from "/products/category/[name]".
   - 'get_product_details(product_id)': 
     - Fetches details for a single product from "/products/[id]".

3. The Interaction:
   - First, show the user the list of categories.
   - Let the user type a category name.
   - Show all products in that category with their prices.
   - Let the user type a product ID to see the full description and rating.

Real-World Logic:
- This is how every e-commerce site works. The "Frontend" (the website you see) makes these exact same REST API calls to the "Backend" (the server with the database) to display products to you!
"""

import requests

# TODO: Implement the E-Commerce Catalog

API = 'https://fakestoreapi.com'

def get_categories():

    response = requests.get(
        API + "/products/categories"
    )

    return response.json()

def get_products_in_category(category_name):

    url = API + "/products/category/" + category_name

    response = requests.get(url)

    return response.json()

def get_product_details(product_id):

    url = API + "/products/" + str(product_id)

    response = requests.get(url)

    return response.json()

if __name__ == "__main__":

    print("=" * 50)
    print("WELCOME TO THE E-COMMERCE CATALOG")
    print("=" * 50)

    categories = get_categories()

    print("\nAvailable Categories:\n")

    for category in categories:
        print("-", category)

    
    chosen_category = input("\nEnter a category name: ")

    try:
        products = get_products_in_category(chosen_category)

        print("\nProducts:\n")

        
        for product in products:

            print(f"ID: {product['id']}")
            print(f"Title: {product['title']}")
            print(f"Price: ${product['price']}")
            print("-" * 40)
    except Exception as e:
        print("Error fetching products in category:", e)

    chosen_product_id = input("\nEnter a product ID: ")

    try:
        product = get_product_details(chosen_product_id)

        print("\nPRODUCT DETAILS")
        print("=" * 50)

        print("Title:", product["title"])
        print("Price:", "$" + str(product["price"]))
        print("Category:", product["category"])
        print("Description:", product["description"])

        print(
            "Rating:",
            product["rating"]["rate"],
            f"({product['rating']['count']} reviews)"
        )

    except Exception as e:
        print("Error fetching product details:", e)