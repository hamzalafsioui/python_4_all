"""
PROJECT: The Fast Web Crawler (Simulator)

Goal: Prove the power of Threading for I/O-bound tasks by simulating a web crawler.

Requirements:

1. Setup:
   - Imagine we have 20 URLs to scrape.
   - urls = [f"http://example.com/page/{i}" for i in range(20)]

2. The Task:
   - Create a function 'scrape_page(url)':
     - Simulate network latency: time.sleep(1)
     - Return the string: f"Scraped {url}"

3. Execution 1: Serial
   - Scrape all 20 pages using a standard 'for' loop.
   - Time the operation (It should take ~20 seconds).

4. Execution 2: Threaded
   - Scrape all 20 pages using 'concurrent.futures.ThreadPoolExecutor(max_workers=10)'.
   - Time the operation (It should take ~2 seconds).

Real-World Logic:
- This is how all modern web scrapers and API clients work. If you need to make 1,000 API requests, doing it one by one would take hours. Using threads, you can make 50 requests at a time, finishing in minutes.
"""

import time
import concurrent.futures

# TODO: Implement the Web Crawler Simulator


def scrape_page(url):
    """
    Simulate network latency.
    """

    time.sleep(1)

    return f"Scraped {url}"



def run_serial(urls):

    print("=" * 50)
    print("SERIAL WEB SCRAPER")
    print("=" * 50)

    start = time.time()

    results = []

    for url in urls:
        results.append(scrape_page(url))

    end = time.time()

    for result in results:
        print(result)

    print(f"\nSerial Time: {end - start:.2f} seconds")



def run_threaded(urls):

    print("\n" + "=" * 50)
    print("THREADED WEB SCRAPER")
    print("=" * 50)

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=10
    ) as executor:

        # Start all scraping tasks concurrently
        results = executor.map(scrape_page, urls)

        # Convert iterator to list
        results = list(results)

    end = time.time()

    for result in results:
        print(result)

    print(f"\nThreaded Time: {end - start:.2f} seconds")


if __name__ == "__main__":

    # Simulated URLs
    urls = [
        f"http://example.com/page/{i}"
        for i in range(20)
    ]

    # Serial execution
    run_serial(urls)

    # Threaded execution
    run_threaded(urls)
