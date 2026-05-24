# Web Scraping: Extracting Data from the Wild

What happens if you want to get data from a website that doesn't have an API? You use **Web Scraping**. This is the process of using Python to "read" the HTML code of a webpage and extract exactly the information you need.

---

## 1. How it Works
1. **Request**: Use the `requests` library to download the HTML source code of a page.
2. **Parse**: Use **BeautifulSoup** to turn that messy code into a searchable Python object.
3. **Extract**: Use specific tags, classes, or IDs to find the data.

---

## 2. HTML Refresher
To be a good scraper, you need to understand HTML:
- **`<div>`**: A container.
- **`<h1>`, `<h2>`**: Headlines.
- **`<p>`**: Paragraphs.
- **`<a>`**: Links (the `href` attribute is the URL).
- **`class` and `id`**: Labels used to style elements (and used by us to find them!).

---

## 3. Installation
```bash
pip install beautifulsoup4 lxml
```

---

## 4. Key BeautifulSoup Methods

### `find()`
Returns the **first** element that matches.
```python
soup.find("h1")
```

### `find_all()`
Returns a **list** of all elements that match.
```python
soup.find_all("p")
```

### `get_text()`
Extracts only the visible text inside a tag, removing the HTML.
```python
title = soup.find("h1").get_text()
```

### `get('attribute')`
Extracts the value of an attribute (like a link).
```python
link = soup.find("a").get("href")
```

---

## 5. Ethics and Legality
**Important**: Not all websites want to be scraped.
1. **Check `robots.txt`**: Visit `website.com/robots.txt` to see what parts are off-limits.
2. **Don't be a Bully**: Don't make 1,000 requests per second. You might crash the site or get your IP banned.
3. **Check the Terms**: Some sites explicitly forbid scraping in their Terms of Service.

---

## 6. Best Practices
1. **Use CSS Selectors**: `soup.select(".my-class")` is often more powerful than `find_all`.
2. **Handle NoneTypes**: If a tag doesn't exist, `find()` returns `None`. Always check before calling `.get_text()`.
3. **Inspect First**: Always use your browser's "Inspect Element" (F12) to find the classes and IDs before writing any code.

## Resources
- **Beautiful Soup Documentation** – https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **Real Python – Web Scraping with Beautiful Soup** – https://realpython.com/beautiful-soup-web-scraper-python/
- **Automate the Boring Stuff – Chapter 12 (Web Scraping)** – https://automatetheboringstuff.com/2e/chapter12/
- **YouTube – Web Scraping Tutorial (Corey Schafer)** – https://www.youtube.com/watch?v=ng2o98k983k
- **Ethics of Web Scraping – MIT Lecture** – https://ocw.mit.edu/18-720-web-scraping-ethics/
