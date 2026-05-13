"""
EXERCISES: The Waiting Game

EXERCISE 1: Manual Threads
1. Use the basic 'threading' module.
2. Create a function 'delayed_print(name, delay)' that sleeps for 'delay' seconds, then prints 'name'.
3. Create two 'threading.Thread' objects: one delays for 2 seconds, one for 1 second.
4. Start both. Use '.join()' to wait for them. Notice which one prints first!

EXERCISE 2: ThreadPool Downloader
1. Create a function 'download_file(filename)' that sleeps for 1 second and returns f"Saved {filename}".
2. Create a list of 10 filenames: ["file_1.txt", "file_2.txt", ... "file_10.txt"].
3. Use 'concurrent.futures.ThreadPoolExecutor' to download all 10 files.
4. Measure the time. It should take ~1-2 seconds, not 10.
"""

import time
import threading
import concurrent.futures

# TODO: Implement the exercises above

# Exercise 1

def delayed_print(name, delay):
    time.sleep(delay)
    print(name)



# Exercise 2
def download_file(filename):
    time.sleep(1)
    return f"Saved {filename}"





if __name__ == "__main__":

    print('='*40)
    print('Ex01')
    print('='*40)

    t1 = threading.Thread(target=delayed_print, args=("Hamza", 2))
    t2 = threading.Thread(target=delayed_print, args=("Abdullah", 1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("=" * 40)
    print("Ex02")
    print("=" * 40)

    files = [f"file_{i}.txt" for i in range(1, 11)]

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

        # Submit ALL tasks immediately
        futures = [
            executor.submit(download_file, file)
            for file in files
        ]

        # Collect results
        for future in futures:
            print(future.result())

    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")
        