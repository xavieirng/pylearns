import random


def task1():
    print("支付宝支付密码")
    password = input()
    num1 = 0
    for i in password:
        if int(ord(i)) <= 57 and int(ord(i)) >= 48:
            num1 += 1

    if num1 == 6:
        print("支付数字合法")
    else:
        print("支付不合法")


def task2():
    commoditys = [["SanDisk 闪迪 u盘 128G", 149], ["苹果鼠标 Magic Mouse2", 550], ["罗技MK2335 无线鼠标键盘套装", 120],
                  ["小米 米家扫地机器人", 1400]]

    commodity = random.choice(commoditys)
    print("竞猜商品为：", commodity[0], ",请输入您的竞猜价格：")
    for i in range(20):
        price = int(input())
        if commodity[1] == price:
            print("恭喜你，你猜对了该商品的价格，你是大赢家！")
            return 0
        if commodity[1] < price:
            print("价格高了，请继续竞猜：")
        else:
            print("价格低了，请继续竞猜：")


if __name__ == '__main__':
    task2()
