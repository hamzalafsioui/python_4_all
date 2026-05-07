"""
Mini-Project: The Clean Code Template

This is a template you can use for all your future Python scripts.
It demonstrates the standard layout and documentation style.
"""

# --- IMPORTS ---
# (None for this basic template)

# --- CONSTANTS ---
TAX_RATE = 0.05
MAX_RETRY = 3

# --- FUNCTIONS ---
def main():
    """
    The main entry point of the script.
    """
    print("Welcome to the Clean Code Template!")
    
    # 1_ Input Section
    item_price = 100 # In real usage: float(input("Enter price: "))
    
    # 2_ Logic Section
    total = item_price * (1 + TAX_RATE)
    
    # 3_ Output Section
    print(f"Subtotal: ${item_price}")
    print(f"Tax Rate: {TAX_RATE:.0%}")
    print(f"Total:    ${total:.2f}")

# --- EXECUTION ---
if __name__ == "__main__":
    main()
