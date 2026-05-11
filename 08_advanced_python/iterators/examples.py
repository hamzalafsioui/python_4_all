# Examples: Manual Iteration and Custom Iterators

# 1_ Manual Iteration using iter() and next()
def manual_demo():
    fruits = ["Apple", "Banana", "Cherry"]
    
    # Get the iterator
    fruit_engine = iter(fruits)
    
    print("--- Manual Iteration ---")
    print(next(fruit_engine)) # Apple
    print(next(fruit_engine)) # Banana
    print(next(fruit_engine)) # Cherry
    
    # This would raise StopIteration:
    # print(next(fruit_engine)) 

# 2_ A Custom Counter Iterator
class Counter:
    """An iterator that counts from low to high."""
    
    def __init__(self, low, high):
        self.current = low
        self.high = high
        
    def __iter__(self):
        """Standard protocol: return self."""
        return self
        
    def __next__(self):
        """Standard protocol: return value or raise StopIteration."""
        if self.current > self.high:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            return value

# 3_ Infinite Iterator Example
class InfiniteCounter:
    def __init__(self):
        self.num = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.num += 1
        return self.num

# --- Usage ---

if __name__ == "__main__":
    manual_demo()
    
    print("\n--- Custom Counter (1 to 5) ---")
    c = Counter(1, 5)
    for num in c:
        print(num)
        
    print("\n--- Infinite Iterator (First 3) ---")
    inf = InfiniteCounter()
    print(next(inf))
    print(next(inf))
    print(next(inf))
