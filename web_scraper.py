import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Set the MongoDB connection string
MONGO_DB_URL = 'mongodb://admin:Pacman111!@localhost:27017/web_scraper_db'

# Set the URL to scrape
URL = 'https://books.toscrape.com/'
response = requests.get(URL)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the book data
books = soup.find_all('article', class_='product_pod')
book_list = []
for book in books:
    title = book.h3.a.attrs['title']
    link = book.h3.a.attrs['href']
    price = book.select_one('p.price_color').get_text()
    book_list.append({'title': title, 'link': link, 'price': price})

# Connect to the MongoDB database
client = MongoClient(MONGO_DB_URL)
db = client['web_scraper_db']
collection = db['web_scraper_collection']

# Insert the book data into the collection
collection.insert_many(book_list)

# Print the number of books in the collection
num_books = collection.count_documents({})
print(f"Total number of books in the collection: {num_books}")
