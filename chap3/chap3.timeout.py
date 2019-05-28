import requests

r = requests.get(url="https://www.taobao.com", timeout=1)

print(r.status_code)