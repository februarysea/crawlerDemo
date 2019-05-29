from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
baseUrl = "https://m.weibo.cn/comments/hotflow?"

headers = {
    'Host': "m.weibo.cn",
    'Referer': "https://www.baidu.com/",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
}


def get_page(max_id):
    params = {
        'id': '4365090332076737',
        'mid': '4365090332076737',
        'max_id': str(max_id),
        'max_id_type': '0'
    }
    url = baseUrl + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json = response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

    max_number = json.get('data').get('max_id')
    datas = json.get('data').get('data')
    for data in datas:
        big = []
        comment = {}
        user = data.get('user')
        pic = data.get('pic')
        comment['usr'] = user.get('screen_name')
        try:
            comment['pic'] = pic.get('url')
        except:
            continue
        print(comment)
        r = requests.get(comment['pic'], stream=True)
        with open(comment['usr']+"'.jpg'", 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)

    return max_number


max = get_page(0)
for i in range(0, 7):
    max = get_page(max)


