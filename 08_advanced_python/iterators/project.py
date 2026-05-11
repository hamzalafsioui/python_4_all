"""
PROJECT: Remote Log Fetcher (Simulated)

Goal: Build an iterator that simulates fetching logs from a remote server one by one.

Requirements:

1. Class 'LogFetcher':
   - Attribute 'max_logs': How many logs to fetch before stopping.
   - Attribute 'fetched_count': Tracks progress.
   - Method '__iter__': Standard return self.
   - Method '__next__':
     - If fetched_count < max_logs:
       - Simulate a "network delay" of 0.5s.
       - Return a string like "[LOG] Entry #{fetched_count} - Status 200 OK".
     - Else:
       - Raise StopIteration.

Real-World Logic:
- This pattern is used in "Pagination" (e.g., loading the next page of search results). 
- The user of the iterator doesn't need to know the logs are coming from a remote server; they just loop over it!
"""

# TODO: Implement the Log Fetcher
import time

class LogFetcher:
    def __init__(self, max_logs):
        self.max_logs = max_logs
        self.fetched_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.fetched_count < self.max_logs:
            time.sleep(0.5)
            self.fetched_count += 1
            return f"[LOG] Entry #{self.fetched_count} - Status 200 OK"
        else:
            raise StopIteration

if __name__ == "__main__":
    log_fetcher = LogFetcher(5)
    for log in log_fetcher:
        print(log)
        
