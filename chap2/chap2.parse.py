from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl

params = {
    "name": "Nick",
    "age": "22"
}
base_url = "https://baidu.com?"
url = base_url + urlencode(params)
print(url)

query = "name=germey&age=22"
print(parse_qs(query))
print(parse_qsl(query))

