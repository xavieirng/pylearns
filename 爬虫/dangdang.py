import requests
from bs4 import BeautifulSoup


class dangdang(object):
    def __init__(self):
        self.URL = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"
        self.starnum = []
        for start_page in range(25):
            self.starnum.append(start_page)

    def get_top50(self):
        for start in self.starnum:

            html = requests.get(self.URL + str(start))

            soup = BeautifulSoup(html.text, "html.parser")

            # name = soup.select('body > div.bang_wrapper > div.bang_content > div.bang_list_box > ul')

            names = soup.find_all('div', class_='name')
            for item in names:
                print(item.text)
                file = open("mulu.txt", "a", encoding="utf-8")
                file.write(item.text + '\n')
                file.close()


if __name__ == '__main__':
    cls = dangdang()
    cls.get_top50()
