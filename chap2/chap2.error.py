import urllib.request
import urllib.error
import socket

try:
    response = urllib.request.urlopen("https://www.baidu.com", timeout=0.1)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")