"""
EXERCISES: Mastering the Protocol

EXERCISE 1: The Fibonacci Iterator
1. Write an iterator class 'Fibonacci' that takes 'n' (the number of Fibonacci numbers to generate).
2. The Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, 8...
3. Each number is the sum of the previous two.
4. Test it with a for loop to print the first 10 Fibonacci numbers.

EXERCISE 2: The Reverse Iterator
1. Write a class 'ReverseIterator' that takes a list and returns its elements in reverse order.
2. Note: Do NOT use list.reverse() or slicing like [::-1]. Use the iterator protocol manually!

EXERCISE 3: The Step Iterator
1. Create an iterator 'EvenRange' that mimics range(0, limit, 2).
"""

# TODO: Implement the exercises below

# EXERCISE 1: Fibonacci Iterator
class Fibonacci:
    def __init__(self, n):
        self.n = n                  # total numbers to generate
        self.count = 0              # how many generated so far
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1

        return value


# EXERCISE 2: Reverse Iterator
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.data[self.index]
        self.index -= 1

        return value


# EXERCISE 3: EvenRange Iterator
class EvenRange:
    def __init__(self, start, stop, step=2):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        value = self.current
        self.current += self.step

        return value


if __name__ == "__main__":

    print("--- Fibonacci Sequence ---")
    fib = Fibonacci(10)
    for num in fib:
        print(num)

    print("\n--- Reverse Iterator ---")
    rev = ReverseIterator([1, 2, 3, 4, 5])
    for num in rev:
        print(num)

    print("\n--- Even Range ---")
    even = EvenRange(0, 10, 2)
    for num in even:
        print(num)
