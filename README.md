# Web Scraper APP

# Setting up MongoDB and Mongo Express using Docker and using it for Web Scraping with Python

In this blog, we have covered how to set up MongoDB and Mongo Express using Docker. This allows us to easily create and manage MongoDB databases and access a visual interface for managing our data. We then proceeded to write a python code to run a command to web scrape a website. With these tools, we can easily create web scrapers like the one we discussed earlier and store the data in our MongoDB databases.

# Prerequisites

To follow along with this tutorial, you will need:

 - Docker installed on your local machine
 - A basic understanding of Python programming language
 - Basic knowledge of web scraping

# Setting up MongoDB and Mongo Express using Docker

To set up MongoDB and Mongo Express using Docker, we need to follow these steps:

 First, we need to pull the MongoDB and Mongo Express images from Docker Hub. We can do this by running the following command in our terminal:
 
 ```
    docker pull mongo
    docker pull mongo-express
 ```
 
 Once the images are downloaded, we can start our MongoDB and Mongo Express containers using the following commands:
 
 ```
    docker network create mongo-network
    docker network ls
    docker run -d --name mongodb --network mongo-network -p 27017:27017 mongo
    docker run -d -p 8081:8081 \
    -e ME_CONFIG_MONGODB_SERVER=mongodb \
    -e ME_CONFIG_BASICAUTH_USERNAME=admin \
    -e ME_CONFIG_BASICAUTH_PASSWORD=Password123! \
    --name mongo-express mongo-express

 ```
 
 Here, we are running two containers - one for MongoDB and one for Mongo Express. The --name flag is used to specify the name of the container, and the -d flag is used to run the container in the background. The --link flag is used to link our Mongo Express container to our MongoDB container, so that it can access the database.

Once our containers are up and running, we can access our Mongo Express dashboard by visiting http://localhost:8081 in our web browser.


# Web Scraping with Python and storing data in MongoDB

Now that we have set up our MongoDB and Mongo Express containers, we can use them for web scraping with Python. Here's an example Python code to scrape a website and store the data in our MongoDB database:

```
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
    collection = db['webscraper']

    # Insert the book data into the collection
    collection.insert_many(book_list)

    # Print the number of books in the collection
    num_books = collection.count_documents({})
    print(f"Total number of books in the collection: {num_books}")

   
```


Conclusion

In this blog post, we have learned how to set up MongoDB and Mongo Express using Docker and use them for web scraping with Python. With these tools, we can easily create web scrapers and store the data in our MongoDB databases. This is a powerful combination that can be used for a variety of use cases.

You can get detailed explanation on my blog [Hasnode.dev](https://vicmode.hashnode.dev/webscrapping-using-beautifulsoup)

