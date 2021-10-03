import requests
from bs4 import BeautifulSoup


class beauty():
    def __init__(self):
        requests.adapters.DEFAULT_RETRIES = 5
        self.URL = 'https://www.buxiuse.com'
        self.startnum = []

        self.headers = {
            'Accept': "application/json, text/plain, */*",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }

        for i in range(1, 1):
            self.startnum.append(i)

    def beautypage(self):
        for i in self.startnum:
            requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
            s = requests.session()
            s.keep_alive = False  # 关闭多余连接
            beautyhtml = requests.get(url=self.URL, params={"cid": 3, "page": i}, timeout=300, headers=self.headers)

            print(beautyhtml.text)
            soup = BeautifulSoup(beautyhtml.text, "html.parser")
            print(soup)
            list = soup.find(class_="thumbnails").find_all("li")

    def start(self):
        page = requests.get(url="https://www.buxiuse.com/?cid=3&page=2")
        print(page.text)


if __name__ == '__main__':
    beauty = beauty()
    beauty.start()
