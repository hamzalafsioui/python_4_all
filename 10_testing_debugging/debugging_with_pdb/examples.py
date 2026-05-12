# Examples: Hunting Bugs with PDB

# 1_ The Logic Error
# This function is supposed to sum all numbers from 1 to N,
# but it has a logical flaw.
def sum_to_n(n):
    total = 0
    for i in range(n): # Bug: range(n) goes from 0 to n-1
        total += i
    return total

# 2_ The "Hidden" Bug
# This function calculates a discount but sometimes returns an error.
def apply_discount(price, discount):
    print(f"Applying {discount}% discount to ${price}...")
    
    breakpoint() # <-- UNCOMMENT THIS to start debugging
    
    final_price = price - (price * (discount / 100))
    
    if final_price < 0:
        print("Warning: Final price is negative!")
        
    return final_price

# --- Usage ---

if __name__ == "__main__":
    # Test 1
    print(f"Sum to 5 (Should be 15): {sum_to_n(5)}")
    
    # Test 2
    # This will work
    print(f"New price: {apply_discount(100, 10)}")
    
    # This might feel "weird" - use pdb to inspect why
    print(f"New price: {apply_discount(100, 110)}")
