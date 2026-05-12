"""
EXERCISES: The Loop Master

EXERCISE 1: The Infinite Counter
1. Use 'itertools.count' to generate multiples of 5.
2. Use 'itertools.islice' to print only the first 10 multiples.

EXERCISE 2: The Multi-List Flattener
1. You have three lists of numbers: [1, 2], [3, 4], [5, 6].
2. Use 'itertools.chain' to print all numbers in a single loop without merging the lists.

EXERCISE 3: The Outfit Generator
1. You have a list of 'tops' = ["Shirt", "Hoodie"].
2. You have a list of 'bottoms' = ["Jeans", "Shorts"].
3. You have a list of 'shoes' = ["Sneakers", "Boots"].
4. Use 'itertools.product' to print every possible outfit combination.

EXERCISE 4: The Grouping Challenge
1. Take a list of numbers: [1, 2, 3, 4].
2. Use 'itertools.permutations' to print all possible orderings of these numbers.
"""

# TODO: Implement the exercises below
import itertools

# Exercise 1
def demo_ex1():
    for i in itertools.count(1, 2):
        if i > 10:
            break
        print(i)

# Exercise 2
def demo_ex2():
    for i in itertools.chain([1, 2], [3, 4], [5, 6]):
        print(i)

# Exercise 3
def demo_ex3():
    for i in itertools.product(["Shirt", "Hoodie"], ["Jeans", "Shorts"], ["Sneakers", "Boots"]):
        print(i)

# Exercise 4
def demo_ex4():
    for i in itertools.permutations([1, 2, 3, 4]):
        print(i)

if __name__ == "__main__":
    demo_ex1()
    demo_ex2()
    demo_ex3()
    demo_ex4()
