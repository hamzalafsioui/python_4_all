"""
PROJECT: Advanced Stock Analyzer

Goal: Build an inventory system that tracks sales and categories efficiently.

Requirements:

1. Transaction History (Deque):
   - Maintain a 'deque' with 'maxlen=5' to store the 5 most recent transactions.

2. Stock Tracking (Counter):
   - Use a 'Counter' to track the total quantity of every item in stock.
   - Initial stock: {"Laptop": 10, "Mouse": 50, "Keyboard": 30}.

3. Category Mapping (DefaultDict):
   - Use a 'defaultdict(set)' to store which items belong to which category.
   - Example: {"Electronics": {"Laptop", "Mouse", "Keyboard"}}.

4. Simulation:
   - Create a function 'process_sale(item, qty)':
     - Decrements the 'Counter'.
     - Adds the sale to the 'recent_transactions' deque.
   - Create a function 'show_report()':
     - Prints the current stock levels.
     - Prints the recent transaction history.

Real-World Logic:
- This uses the right tool for the right job: Counter for math, Deque for a sliding window of logs, and DefaultDict for grouping.
"""

# TODO: Implement the Stock Analyzer
from collections import Counter, deque, defaultdict

if __name__ == "__main__":
    stock = Counter({"Laptop": 10, "Mouse": 50, "Keyboard": 30})
    recent_transactions = deque(maxlen=5)
    category_mapping = defaultdict(set)

    def process_sale(item, qty):
        stock[item] -= qty
        recent_transactions.append((item, qty))

    def show_report():
        print("Stock Levels:", stock)
        print("Recent Transactions:", recent_transactions)

    def update_stock(item, qty, category):
        stock[item] += qty
        category_mapping[category].add(item)

    update_stock("Laptop", 2, "Electronics")
    update_stock("Mouse", 5, "Electronics")
    update_stock("Keyboard", 3, "Electronics")
    update_stock("Monitor", 4, "Electronics")
    update_stock("Phone", 6, "Electronics")
    show_report()
