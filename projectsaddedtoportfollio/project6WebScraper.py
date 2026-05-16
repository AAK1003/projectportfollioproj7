import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
website_data = requests.get(url)
if website_data.status_code == 200:
    bsdata = BeautifulSoup(website_data.text, "html.parser")
    categories = bsdata.find_all(class_ = 'side_categories')
    for catagory in categories:
        print(f'Categories: \n{catagory.text.strip()}')
else:
    print(f'Sorry, data from {url} is not accessible at this time')