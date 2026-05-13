"""
EXERCISES: The Parallel Processor

EXERCISE 1: Manual Processes
1. Write a function 'countdown(name, n)' that counts down from 'n' to 0, with a 'time.sleep(0.5)' between numbers.
2. In the 'if __name__' block, create two 'multiprocessing.Process' objects.
3. Start both processes.
4. Use '.join()' to wait for both to finish.

EXERCISE 2: Pool Mapping
1. Write a function 'is_prime(n)' that returns True if a number is prime, and False otherwise.
2. Create a list of large numbers (e.g., [10000000, 10000001, 10000002, 10000003]).
3. Use 'multiprocessing.Pool().map()' to check all of them concurrently.

Note: Make sure all execution code is inside the 'if __name__ == "__main__":' block!
"""

import time
import multiprocessing

# TODO: Implement the exercises above

def countdown(name, n):
    for i in range(n, -1, -1):
        print(f"{name}: {i}")
        time.sleep(0.5)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Exercise 1
    p1 = multiprocessing.Process(target=countdown, args=("Process 1", 5))
    p2 = multiprocessing.Process(target=countdown, args=("Process 2", 5))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    # Exercise 2
    numbers = [10000000, 10000001, 10000002, 10000003]
    with multiprocessing.Pool() as pool:
        results = pool.map(is_prime, numbers)
    print(results)
