"""
EXERCISES: The Data Harvester

EXERCISE 1: Tag Finder
1. Create a variable 'html' with a string containing an <h1>, three <li> items, and one <a> link.
2. Use BeautifulSoup to:
   - Print the text inside the <h1>.
   - Print the number of items in the list (len of <li>).
   - Print the URL of the link.

EXERCISE 2: Class Search
1. Use the URL: "https://quotes.toscrape.com/".
2. Fetch the page and find all "tag" links (they have a class of "tag").
3. Print a list of all unique tags found on the first page.

EXERCISE 3: The Author Explorer
1. Using the same quotes site, find all <small> tags with the class "author".
2. Create a set of all author names so that there are no duplicates.
3. Print the sorted list of authors.
"""

from bs4 import BeautifulSoup
import requests

# TODO: Implement the exercises below


html_doc = """
<html>
    <body>

        <h1 id="title">My Blog</h1>

        <ul class="items">
            <li class="item">Item 1</li>
            <li class="item">Item 2</li>
            <li class="item">Item 3</li>
        </ul>

        <a href="https://google.com">Google</a>

    </body>
</html>
"""



def tag_finder():

    soup = BeautifulSoup(html_doc, "html.parser")

    # H1 text
    print(soup.find("h1").get_text())

    # Number of list items
    items = soup.find_all("li", class_="item")
    print(len(items))

    # Link URL
    print(soup.find("a").get("href"))



def class_search():

    url = "https://quotes.toscrape.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    tags = set()

    for tag in soup.find_all("a", class_="tag"):

        tags.add(tag.get_text())

    print(sorted(tags))




def author_explorer():

    url = "https://quotes.toscrape.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    authors = set()

    for author in soup.find_all("small", class_="author"):

        authors.add(author.get_text())

    print(sorted(authors))



if __name__ == "__main__":

    tag_finder()

    print("\n--- TAGS ---")
    class_search()

    print("\n--- AUTHORS ---")
    author_explorer()