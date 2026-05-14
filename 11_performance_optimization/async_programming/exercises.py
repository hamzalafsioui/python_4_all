"""
EXERCISES: The Async Adventurer

EXERCISE 1: The Basic Coroutine
1. Write an async function 'greet(name)' that:
   - Prints "Hello [name]"
   - Awaits 'asyncio.sleep(1)'
   - Prints "Goodbye [name]"
2. Run it using 'asyncio.run()'.

EXERCISE 2: Concurrent Timers
1. Write an async function 'timer(label, seconds)'.
2. In a main function, use 'asyncio.gather' to run:
   - timer("Short", 1)
   - timer("Medium", 2)
   - timer("Long", 3)
3. Total time should be 3 seconds, not 6.

EXERCISE 3: The Async Loop
1. Create a list of 5 names.
2. Use a list comprehension to create a list of 'greet' coroutines.
3. Use 'asyncio.gather' to run all of them at once.
"""

import asyncio
import time

# TODO: Implement the exercises below


async def greet(name):

    print(f"Hello {name}")

    await asyncio.sleep(1)

    print(f"Goodbye {name}")

async def timer(label, seconds):

    print(f"Starting timer {label} ({seconds}s)...")

    await asyncio.sleep(seconds)

    print(f"Timer {label} finished.")


async def run_timers():

    await asyncio.gather(
        timer("Short", 1),
        timer("Medium", 2),
        timer("Long", 3)
    )



async def run_greetings():

    names = ["Hamza", "Ali", "Omar", "Sara", "Hiba"]

    tasks = [greet(name) for name in names]

    await asyncio.gather(*tasks)



async def main():

    print("=" * 40)
    print("Exercise 1")
    print("=" * 40)

    await greet("Hamza")

    print("\n" + "=" * 40)
    print("Exercise 2")
    print("=" * 40)

    await run_timers()

    print("\n" + "=" * 40)
    print("Exercise 3")
    print("=" * 40)

    await run_greetings()


if __name__ == "__main__":

    asyncio.run(main())