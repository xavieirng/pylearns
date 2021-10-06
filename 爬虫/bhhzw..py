import requests
from bs4 import BeautifulSoup


class bhh():
    def __init__(self):
        self.URL = "https://www.bhhzw.com/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

    def get_url(self):
        htmlurl = requests.get(self.URL, verify=False)

        soup = BeautifulSoup(htmlurl, "lxml")
        print(soup)
        # html = etree.HTML(htmlurl)
        # html_data = html.find('/html/body/div[1]/div[2]')
        # print(html_data)
        # # /html/body/div[1]/div[2]/div[1]/div/a

        # for item in html_data:


if __name__ == '__main__':
    bhh = bhh()
    bhh.get_url()
