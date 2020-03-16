import requests
from bs4 import BeautifulSoup

import requests
URL = 'https://www.tripadvisor.it/Airline_Review-d8729018-Reviews-Alitalia'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())



