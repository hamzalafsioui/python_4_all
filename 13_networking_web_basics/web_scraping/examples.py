# Examples: Parsing HTML and Scraping a Live Site

import requests
from bs4 import BeautifulSoup

# --- 1. Parsing a Local String ---
def parse_string_demo():
    print("--- Local HTML Parsing ---")
    html_doc = """
    <html>
        <body>
            <h1 id="title">My Blog</h1>
            <p class="content">First paragraph of interesting stuff.</p>
            <p class="content">Second paragraph with a <a href="https://google.com">link</a>.</p>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, "html.parser")
    
    # Find by Tag
    print(f"Title Tag: {soup.h1.string}")
    
    # Find by ID
    title = soup.find(id="title")
    print(f"Title by ID: {title.get_text()}")
    
    # Find All by Class
    paragraphs = soup.find_all("p", class_="content")
    for p in paragraphs:
        print(f"Paragraph: {p.get_text().strip()}")

# --- 2. Scraping a Live Site ---
def scrape_live_demo():
    print("\n--- Live Web Scraping ---")
    # We use a site specifically built for scraping practice
    url = "https://quotes.toscrape.com/"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Check for errors
        
        soup = BeautifulSoup(response.text, "lxml")
        
        # Find all quotes on the page
        # In this site, each quote is inside a div with class "quote"
        quotes = soup.find_all("div", class_="quote")
        
        for i, quote in enumerate(quotes[:5], 1): # Just show first 5 
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            print(f"{i}. \"{text}\" - {author}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Note: pip install beautifulsoup4 lxml requests
    parse_string_demo()
    scrape_live_demo()
