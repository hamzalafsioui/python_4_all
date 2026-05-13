"""
EXERCISES: The Bottleneck Hunter

EXERCISE 1: Profile the Fibonacci
1. The code below calculates the 30th Fibonacci number using recursion.
2. Run it with 'python -m cProfile -s ncalls exercises.py'.
3. Look at 'ncalls'. How many times was 'fib' called? (Hint: It's over 1 million!).

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

EXERCISE 2: Finding the culprit
1. You have a pipeline of 3 functions: 'fetch', 'process', 'save'.
2. One is slow. Use 'cProfile' to find out which one.

def fetch():
    time.sleep(0.1)

def process():
    # Intentional bottleneck
    total = 0
    for i in range(5_000_000):
        total += i
    return total

def save():
    time.sleep(0.1)

def run_pipeline():
    fetch()
    process()
    save()
"""

import time
import cProfile

# TODO: Implement and profile the exercises below
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fetch():
    time.sleep(0.1)

def process():
    # Intentional bottleneck
    total = 0
    for i in range(5_000_000):
        total += i
    return total

def save():
    time.sleep(0.1)

def run_pipeline():
    fetch()
    process()
    save()

if __name__ == "__main__":
    fib(30)
    run_pipeline()




