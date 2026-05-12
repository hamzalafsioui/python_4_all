"""
PROJECT: The Robust Web Scraper (Simulator)

Goal: Build a simulator for a web scraper that uses professional logging.

Requirements:

1. Setup:
   - Configure logging to save 'INFO' and above to 'scraper.log'.
   - Configure a second handler to print 'WARNING' and above to the console.

2. Simulation Logic:
   - Create a list of URLs (e.g., ["google.com", "broken-site.org", "slow-api.net"]).
   - Create a function 'scrape_site(url)':
     - Log 'INFO': "Attempting to reach [url]..."
     - If the site is "slow-api.net", log 'WARNING': "Connection to [url] is slow (latency: 5s)."
     - If the site is "broken-site.org", log 'ERROR': "404 Not Found: [url]".
     - Otherwise, log 'INFO': "Successfully scraped [url]."

3. Execution:
   - Run the scraper through your list of URLs.
   - Open 'scraper.log' and verify that all events were recorded correctly.

Real-World Logic:
- Scrapers often run for hours or days. Logging is the ONLY way to know which sites failed and why without staring at the screen the whole time.
"""

import logging
import time
import os

# TODO: Implement the Robust Scraper Simulator

def scrape_site(url):
    logging.info(f"Attempting to reach {url}...")
    if url == "slow-api.net":
        logging.warning(f"Connection to {url} is slow (latency: 5s).")
    elif url == "broken-site.org":
        logging.error(f"404 Not Found: {url}")
    else:
        logging.info(f"Successfully scraped {url}.")

if __name__ == "__main__":

    BASE_DIR = os.path.join(os.path.dirname(__file__), "")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s: [%(levelname)s] -> %(message)s",
        filename= BASE_DIR + "scraper.log"
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    
    url_list = ["google.com", "broken-site.org", "slow-api.net"]
    for url in url_list:
        scrape_site(url)
