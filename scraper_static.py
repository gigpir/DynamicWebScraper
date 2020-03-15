import requests
import bs4 as bs
import urllib.request
URL = 'https://www.vivino.com/explore?e=eJwFwb0KgCAYBdC3uWMUEk13bGiNmiLiy0yE1DDp5-07xyeqooZ3gQ28vFQl9MdugGY79jhZwe68JTmT5UBcmSS7YK9FbpPEGkRu5tJ48jSz-gEIaBrF'

source = urllib.request.urlopen(URL)
soup = bs.BeautifulSoup(source,'xml')
js_test = soup.findAll('span', class_='vintageTitle__wine--U7t9G')

print(js_test)

