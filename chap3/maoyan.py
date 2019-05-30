import requests


def getOnePage(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = "http://maoyan.com/board/4?offset=0"
    html = getOnePage(url)


main()
