from urllib.request import HTTPPasswordMgrWithDefaultRealm
from urllib.request import HTTPBasicAuthHandler
from urllib.request import build_opener
from urllib.error import URLError

username = "username"
password = "password"
url = "http://localhost:5000"

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(realm=None, uri=url, user=username, passwd=password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)