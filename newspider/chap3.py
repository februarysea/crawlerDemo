import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.test
collection = db['movies']

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'Host': 'movie.douban.com'
}

num = 0
while num < 250:
    url = "https://movie.douban.com/top250" + "?start=" + str(num)
    num = num + 25
    response = requests.get(url=url, headers=headers)
    html = pq(response.text)
    items = html('.item').items()
    for item in items:
        movie = {
            'id': str(item.find('em').text()),
            'name': str(item('.title').text()) + str(item('.other').text()),
            'info': str(item.find('p').text()),
            'quote': str(item('.inq').text())
        }
        collection.insert_one(movie)


