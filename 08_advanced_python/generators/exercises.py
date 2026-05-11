"""
EXERCISES: The Lazy Programmer

EXERCISE 1: The Even Generator
1. Write a generator function 'evens(limit)' that yields even numbers up to the limit.
2. Test it using a for loop.

EXERCISE 2: Custom Range
1. Write a generator function 'my_range(start, stop, step)' that mimics the built-in range().
2. Ensure it handles the step correctly.

EXERCISE 3: Reading Large Lists
1. Imagine you have a massive list of strings.
2. Use a Generator Expression to create a generator that filters out strings shorter than 5 characters.
"""

# TODO: Implement the exercises below

def evens(limit: int):
    for i in range(limit):
        if i % 2 == 0:
            yield i

def my_range(start: int, stop: int, step: int = 1):
    while start < stop:
        yield start
        start += step

def filter_strings(strings: list[str]):
    return (s for s in strings if len(s) >= 5)


if __name__ == "__main__":
    # Test your generators here
    for i in evens(10):
        print(i)

    for i in my_range(1, 10, 2):
        print(i)

    strings = ["apple", "banana", "cat", "dog", "elephant"]
    for s in filter_strings(strings):
        print(s)
