import requests
import json
import time
import random
from pymongo import MongoClient


headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'Host': 'm.weibo.cn',
    'Cookie': '_T_WM=71838482308; WEIBOCN_FROM=1110006030; SUB=_2A25wHFO4DeRhGeBM6FES8SnIyjmIHXVT_33wrDV6PUJbkdANLWblkW1NROJamJ-E3ulWvvC9Zugn2njYG6lydEW3; SUHB=0wnFVymvczh6EA; MLOGIN=1; XSRF-TOKEN=65557c; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253Dbiniscool%26oid%3D2310026597710454_-_MBLOGPAGE%26uicode%3D10000011%26fid%3D1076036597710454',
    'referer': 'https://m.weibo.cn/u/2397963837',
    'X-Requested-With': "XMLHttpRequest",
}

client = MongoClient('localhost', 27017)
db = client.test
collection = db['ray']


url = "https://m.weibo.cn/api"
for k in range(0, 200):
    try:
        response = requests.get(url=url, headers=headers)
    except requests.exceptions.Timeout as e:
        print('请求超时：'+str(e.message))
    except requests.exceptions.HTTPError as e:
        print('http请求错误:'+str(e.message))

    data = json.loads(response.text)
    since_id = "&since_id=" + str(data['data']['cardlistInfo']['since_id'])
    url = "https://m.weibo.cn/api/container/getIndex?type=uid&value=2397963837&containerid=1076032397963837" + since_id
    for card in data['data']['cards']:
        if card['card_type'] == 9:
            if card['mblog']['pic_types'] == '0,0' or card['mblog']['pic_types'] == '0':
                ray = {
                    'text': card['mblog']['text'],
                    'pic': card['mblog']['original_pic'],
                    'date': card['mblog']['created_at']
                }
            else:
                ray = {
                    'text': card['mblog']['text'],
                    'date': card['mblog']['created_at'],
                }
            collection.insert_one(ray)
            print(ray)
