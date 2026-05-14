# Examples: Modern Concurrency with Asyncio

import asyncio
import time

# --- A Coroutine ---
async def fetch_data(id, delay):
    print(f"Task {id}: Starting (will take {delay}s)...")
    
    # Non-blocking sleep: This allows other tasks to run!
    await asyncio.sleep(delay)
    
    print(f"Task {id}: Finished.")
    return f"Result {id}"

# --- Running Concurrently ---
async def main():
    print("--- Starting Async Demo ---")
    start_time = time.perf_counter()

    # We create a list of tasks (coroutines)
    # Note: Calling the function returns the coroutine, but doesn't run it yet.
    task1 = fetch_data(1, 3)
    task2 = fetch_data(2, 1)
    task3 = fetch_data(3, 2)

    # asyncio.gather runs them all at once
    # The total time will be the time of the longest task (3s)
    results = await asyncio.gather(task1, task2, task3)

    end_time = time.perf_counter()
    print(f"\nAll results: {results}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

# --- Entry Point ---
if __name__ == "__main__":
    # In Python 3.7+, this is the standard way to run the top-level entry point
    asyncio.run(main())
