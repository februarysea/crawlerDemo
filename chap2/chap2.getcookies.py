import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
for item in cookie:
    print(item.name + "=" + item.value)

filename = "cookies"
cookies = http.cookiejar.LWPCookieJar(filename=filename)  # create cookie file
handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookies.save(ignore_discard=True, ignore_expires=True)
