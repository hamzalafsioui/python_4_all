"""
PROJECT: The Quote-to-CSV Exporter

Goal: Scrape multiple pages of quotes and save them into a clean CSV file.

Requirements:

1. Setup:
   - Base URL: "https://quotes.toscrape.com"
   - Target File: "quotes.csv"

2. Logic:
   - Loop through the first 3 pages of the site (URL pattern: /page/1/, /page/2/, etc.).
   - For each page:
     - Find all quote containers.
     - Extract the Quote Text, Author, and the Tags associated with that quote.
   - Store the data in a list of dictionaries.

3. Output:
   - Use the 'csv' module to write the list of dictionaries into 'quotes.csv'.
   - Headers should be: "Quote", "Author", "Tags".

4. Ethics Check:
   - Add a 'time.sleep(1)' between page requests so you don't overwhelm the server.

Real-World Logic:
- This is how data scientists collect training data for AI models. If there is no dataset available on Kaggle, they build a scraper like this to gather their own data from the web!
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
import os

# TODO: Implement the Quote Exporter

BASE_URL = 'https://quotes.toscrape.com/'
TARGET_FILE = os.path.join(os.path.dirname(__file__), 'quotes.csv')

def write_to_csv(data):
    with open(TARGET_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Quote", "Author", "Tags"])
        writer.writeheader()
        writer.writerows(data)

def quote_scraper():
    quotes_data = []
    
    for page_num in range(1, 4):  
        url = f"{BASE_URL}page/{page_num}/"
        print(f"Scraping page {page_num}: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            text = quote.find('span', class_='text').get_text(strip=True)
            author = quote.find('small', class_='author').get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]
            tags_str = ', '.join(tags)
            
            quotes_data.append({
                "Quote": text,
                "Author": author,
                "Tags": tags_str
            })
        
        # Ethics check: polite delay between requests
        if page_num < 3:
            time.sleep(1)
    
    write_to_csv(quotes_data)
    print(f"Done! Saved {len(quotes_data)} quotes to '{TARGET_FILE}'.")

if __name__ == "__main__":
    quote_scraper()