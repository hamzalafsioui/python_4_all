"""
PROJECT: Large Log File Processor

Goal: Process a massive log file without loading it all into memory.

Requirements:

1. Generator 'read_logs(file_path)':
   - Opens the file.
   - Yields one line at a time.
   - Cleanly closes the file when done (use 'with' statement).

2. Generator 'filter_logs(log_stream, keyword)':
   - Takes a generator as input.
   - Yields only the lines that contain the keyword.

3. Main Logic:
   - Create a dummy 'server.log' file with many lines.
   - Chain the generators together: read -> filter.
   - Print the matching lines.

Real-World Logic:
- Chaining generators creates a 'pipeline'. Data flows through the pipeline one line at a time. 
- This uses almost ZERO memory regardless of whether the file is 1MB or 100GB.
"""

# TODO: Implement the Log Processor
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "server.log")

def create_dummy_logs():
    with open(LOG_FILE, "w") as f:
        f.write("INFO: System started\n")
        f.write("ERROR: Database connection failed\n")
        f.write("DEBUG: Cache cleared\n")
        f.write("ERROR: Unauthorized access attempt\n")
        f.write("INFO: User logged in\n")

def read_logs(file_path: str):
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()

def filter_logs(log_stream, keyword: str):
    for line in log_stream:
        if keyword in line:
            yield line

if __name__ == "__main__":
    create_dummy_logs()
    # Implement the generator pipeline here
    log_stream = read_logs(LOG_FILE)
    filtered_logs = filter_logs(log_stream, "ERROR")
    for log in filtered_logs:
        print(log)
    
