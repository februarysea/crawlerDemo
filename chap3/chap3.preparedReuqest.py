from requests import Request
from requests import Session

url = "http://httpbin.org/post"
data = {
    "name": "nick"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
}

s = Session()
req = Request(method='POST', url=url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)