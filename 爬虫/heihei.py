import requests
from bs4 import BeautifulSoup


def test():
    response = requests.get('http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1')
    # print(response.text)  # 打印状态码
    # print(response.text)
    soup = BeautifulSoup(response.text, 'lxml')

    print(soup.body.div)


if __name__ == '__main__':
    test()
