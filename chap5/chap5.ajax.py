from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
base_url = "https://m.weibo.cn/api/container/getIndex?"

headers = {
    'Host': "m.weibo.cn",
    'Referer': "https://www.baidu.com/",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
}

r = requests.get(url="https://m.weibo.cn/detail/4365090332076737", headers=headers)
print(r)