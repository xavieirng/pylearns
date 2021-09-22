import urllib
from urllib import request

if __name__ == '__main__':
    response = urllib.request.urlopen(
        'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E5%88%BA%E5%AE%A2567')
    print(response.read().decode('utf-8'))
