"""
EXERCISES: The Efficiency Expert

EXERCISE 1: Big O Identification
Identify the Time Complexity (Big O) of these functions:

1. def print_first(lst):
       print(lst[0])
   # Your Answer: 

2. def print_all(lst):
       for x in lst:
           print(x)
   # Your Answer: 

3. def find_pairs(lst):
       for x in lst:
           for y in lst:
               print(x, y)
   # Your Answer: 

EXERCISE 2: The Optimized Duplicate Finder
1. The function below is O(n^2) because of the nested loop.
2. Rewrite it to be O(n) using a SET.

def find_duplicates_slow(lst):
    dupes = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                dupes.append(lst[i])
    return dupes

def find_duplicates_fast(lst):
    # TODO: Implement using a set
    pass

EXERCISE 3: List vs Set Benchmark
1. Create a large list of 1,000,000 numbers.
2. Convert that list into a set.
3. Measure how long it takes to find the number 999,999 in the list.
4. Measure how long it takes to find the same number in the set.
"""

import time

# TODO: Implement the exercises above

# Exercise 1 Answer
# 1. O(1)
# 2. O(n)
# 3. O(n^2)

# Exercise 2

def find_duplicates_fast(lst):
    seen = set()
    dupes = []
    for x in lst:
        if x in seen:
            dupes.append(x)
        seen.add(x)
    return dupes

# Exercise 3 
def large_list_demo():
    large_list = list(range(1_000_000))
    target = 999_999

    # List search (O(n))
    start = time.time()
    target in large_list
    list_time = time.time() - start

    # Set search (O(1))
    large_set = set(large_list)
    start = time.time()
    target in large_set
    set_time = time.time() - start

    print(f"List search time: {list_time:.6f}s")
    print(f"Set search time:  {set_time:.6f}s")


if __name__ == "__main__":
    print("Exercise 1")
    print("1. O(1)")
    print("2. O(n)")
    print("3. O(n^2)")
    
    print("\nExercise 2")
    print("find_duplicates_fast: ", find_duplicates_fast([1, 2, 3, 2, 1]))
    
    print("\nExercise 3 ")
    large_list_demo()
