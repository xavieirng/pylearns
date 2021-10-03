import requests
from bs4 import BeautifulSoup


class douban():
    def __init__(self):
        self.URL = "https://movie.douban.com/top250"
        self.movienums = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        for movie in range(0, 251, 25):
            self.movienums.append(movie)

    def getmovies(self):
        for movie in self.movienums:
            moviepage = requests.get(self.URL, params={"start": movie, "filter": ''}, headers=self.headers)

            soup = BeautifulSoup(moviepage.text, "html.parser")

            list = soup.find(class_='grid_view').find_all('li')

            for item in list:
                item_name = item.find(class_='title').string
                item_img = item.find('a').find('img').get('src')
                item_index = item.find(class_='').string
                item_score = item.find(class_='rating_num').string
                item_author = item.find('p').text

                # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
                print('爬取电影：' + item_index + ' | ' + item_name + ' | ')

            moviepage.close()


if __name__ == '__main__':
    douban = douban()
    douban.getmovies()
