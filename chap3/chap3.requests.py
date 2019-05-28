import requests
from requests import exceptions

cookies = '_zap=66015167-c1f3-4d82-88cc-8256535a8524; d_c0="ALDiqvTFgQ6PTned3qJOoptlZpC_FCwjwKw=|1542007104"; tst=r; __gads=ID=3b9e7ddc5fa5e3bb:T=1543198760:S=ALNI_MbTeR4B34uQfksHhfhg0rO3obk0nw; __utmz=51854390.1554010421.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); q_c1=fda92040d2cb42819b4eecdf03083fbf|1556977501000|1542007106000; _xsrf=2757136a-d67f-46a4-80ba-b3c43abb6c45; __utma=51854390.1483761936.1554010421.1554010421.1559011258.2; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20140810=1^3=entry_date=20140810=1; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330; capsion_ticket="2|1:0|10:1559015573|14:capsion_ticket|44:NmVkZTJkNDM0YTU3NGUzZmJhYjIyNDA4YTlhYjAwNzU=|10bff46b8bfd4abfab6e94a52bb230e1e9a57119846d4daaa74ac8c56683e1c4"; z_c0="2|1:0|10:1559015601|4:z_c0|92:Mi4xdnZCeEFBQUFBQUFBc09LcTlNV0JEaWNBQUFDRUFsVk5zVDBVWFFBenRZR2NVb2ppcGhFbUsxdGVFNkNjeWI2cjh3|1d3c1fc92ad3b326e48c1c98e719ffa9f5d03caae8ea581edcfb57e27327d0cc"'
cookies.strip('\"')

headers = {
    "Cookie": cookies,
    "Host": "www.zhihu.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
}

r = requests.get(url="https://www.zhihu.com", headers=headers)
print(r.text)

