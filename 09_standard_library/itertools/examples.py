# Examples: Efficient Looping with Itertools

import itertools

# 1_ Infinite and Repeating Iterators
def infinite_demo():
    print("--- Infinite Iterators ---")
    
    # Count: 10, 12, 14...
    counter = itertools.count(10, 2)
    print("First 3 counts:", [next(counter) for _ in range(3)])
    
    # Cycle: A, B, C, A, B, C...
    cycler = itertools.cycle(["A", "B", "C"])
    print("First 5 cycles:", [next(cycler) for _ in range(5)])

# 2_ Combinatorics (The Math of Combinations)
def combinatorics_demo():
    print("\n--- Combinatorics Demo ---")
    
    # Product (Cartesian Product)
    colors = ["Red", "Blue"]
    sizes = ["S", "M"]
    combinations = list(itertools.product(colors, sizes))
    print(f"Product (Colors x Sizes): {combinations}")
    
    # Combinations (Unique groups of 2)
    names = ["Hamza", "Osama", "Ali"]
    teams = list(itertools.combinations(names, 2))
    print(f"Possible teams of 2: {teams}")

# 3_ Chaining and Accumulating
def chain_demo():
    print("\n--- Chain and Accumulate ---")
    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    
    # Chain: Treats two lists as one
    combined = list(itertools.chain(list1, list2))
    print(f"Combined lists: {combined}")
    
    # Accumulate: Running totals
    numbers = [1, 2, 3, 4, 5]
    running_total = list(itertools.accumulate(numbers))
    print(f"Running totals: {running_total}")

# --- Usage ---

if __name__ == "__main__":
    infinite_demo()
    combinatorics_demo()
    chain_demo()
