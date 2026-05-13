# Examples: Concurrent Network Requests

import time
import concurrent.futures

# --- An I/O-Bound Task ---
def fetch_data(api_endpoint):
    """Simulates requesting data from an API over the internet."""
    print(f"Requesting data from {api_endpoint}...")
    
    # We use sleep to simulate network latency. 
    # During a sleep, the thread releases the GIL!
    time.sleep(2) 
    
    return f"Data from {api_endpoint}"

# --- Serial vs Threaded ---

def run_serial(endpoints):
    print("--- Running Serial ---")
    start = time.time()
    
    for endpoint in endpoints:
        result = fetch_data(endpoint)
        print(result)
        
    end = time.time()
    print(f"Serial Time: {end - start:.2f} seconds\n")

def run_threaded(endpoints):
    print("--- Running Threaded ---")
    start = time.time()
    
    # We can create a pool of threads.
    # max_workers decides how many threads run concurrently.
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # map() automatically assigns endpoints to available threads
        results = executor.map(fetch_data, endpoints)
        
        # Results are yielded in the same order they were given
        for result in results:
            print(result)
            
    end = time.time()
    print(f"Threaded Time: {end - start:.2f} seconds\n")

# --- Usage ---

if __name__ == "__main__":
    # We have 5 fake API endpoints
    api_urls = [f"api.server.com/data/{i}" for i in range(1, 6)]
    
    # Serial should take ~10 seconds (5 urls * 2 seconds)
    run_serial(api_urls)
    
    # Threaded should take ~2 seconds (All 5 run at the same time!)
    run_threaded(api_urls)
