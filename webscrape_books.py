import requests
from bs4 import BeautifulSoup

# Set the URL you want to scrape
url = "http://books.toscrape.com/"

# Make a request to the website and store the response
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the book elements
books = soup.find_all("article", class_="product_pod")

# Iterate through the books and print the title and price
for book in books:
    # Find the title element
    title_element = book.find("h3").find("a")
    # Get the text of the title element
    title = title_element["title"]
    # Find the price element
    price_element = book.find("p", class_="price_color")
    # Get the text of the price element
    price = price_element.text
    # Print the title and price
    print(f"{title}: {price}")

# Save the results to a file
with open("books.txt", "w") as f:
    for book in books:
        title_element = book.find("h3").find("a")
        title = title_element["title"]
        price_element = book.find("p", class_="price_color")
        price = price_element.text
        f.write(f"{title}: {price}\n")
