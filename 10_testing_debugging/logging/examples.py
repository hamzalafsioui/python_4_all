# Examples: Master the Art of Logging

import logging
import os

# --- Basic Configuration ---
# This setup logs to both a file AND the console
def setup_logging():
    # Get current directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(base_dir, "example.log")

    logging.basicConfig(
        level=logging.DEBUG, # Capture everything!
        format="[%(levelname)s] %(asctime)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),   # Write to file
            logging.StreamHandler()         # Also print to screen
        ]
    )

def logging_demo():
    print("--- Starting Logging Demo ---")
    
    logging.debug("This is a developer secret: variable x = 10")
    logging.info("User 'Hamza' has logged in.")
    logging.warning("System temperature is rising (60C).")
    logging.error("Could not find image 'profile.jpg'.")
    logging.critical("CPU OVERHEATING. SHUTTING DOWN.")

def exception_logging():
    print("\n--- Exception Logging Demo ---")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        # 'exception' level automatically includes the traceback!
        logging.exception("An error occurred during math operation:")

# --- Usage ---

if __name__ == "__main__":
    setup_logging()
    logging_demo()
    exception_logging()
    print("\nCheck 'example.log' in this folder to see the persisted logs!")
