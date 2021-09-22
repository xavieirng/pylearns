import random
from array import array
from random import random, randint


def tesk1():
    print("报道日期 00010 00000 00010 00000 00001 01010")
    times = ["00010", "00000", "00010", "00000", "00001", "01010"]
    print("您破解的报名日期" + str(int(times[0], 10)) + str(int(times[1], 10)) + str(int(times[2], 10)) + str(
        int(times[3], 10)) + "年" + str(int(times[4], 10)) + "月" + str(int(times[5], 10)) + "日")


def tesk2():
    str1 = "我爱你一生一世"
    str2 = 520.1314
    str3 = 5201314
    print(str1)
    print(str(str2))
    print(str(str3))


def tesk3():
    print("请输入一个数")
    number = int(input())
    print(str(number) + "的二进制数为:" + bin(number) + ",八进制为：" + oct(number) + "，十六进制为：" + hex(number))


def tesk4():
    gamestr = ["攻击", "防御", "武力", "统率", "速度", "智力"]
    game = array("i")

    game.append(int(input("请输入攻击值")))
    game.append(int(input("请输入防御值")))
    game.append(int(input("请输入武力值")))
    game.append(int(input("请输入统率值")))
    game.append(int(input("请输入速度值")))
    game.append(int(input("请输入智力值")))

    for i in range(len(game)):
        print(gamestr[i] + "  " + str(game[i]) + "          " + printstart(game[i]))


def printstart(start, starts=""):
    for i in range(int(start / 10)):
        starts += "*"
    return starts


def tesk5():
    computer = randint(1, 3)
    print("请玩家输入")
    print("1.石头")
    print("2.剪刀")
    print("3.布")
    gamer = int(input())
    if computer == 1:
        print("电脑出了 1.石头")
        if gamer == 1:
            print("您出了 1.石头")
            print("平局")
        if gamer == 2:
            print("您出了 2.剪刀")
            print("您输了")
        if gamer == 3:
            print("您出了 3.布")
            print("您赢了")

    if computer == 2:
        print("电脑出了 2.剪刀")
        if gamer == 2:
            print("您出了 2.剪刀")
            print("平局")
        if gamer == 3:
            print("您出了 3.布")
            print("您输了")
        if gamer == 1:
            print("您出了 1.石头")
            print("您赢了")

    if computer == 3:
        print("电脑出了 3.布")
        if gamer == 3:
            print("您出了 3.布")
            print("平局")
        if gamer == 1:
            print("您出了 1.石头")
            print("您输了")
        if gamer == 2:
            print("您出了 2.剪刀")
            print("您赢了")


def tesk6():
    print("尤文图shi                                曼联")
    print("■" * 5 + "控球率" + "■" * 5)
    print("■" * 5 + "任意球" + "■" * 5)
    print("■" * 5 + "射正" + "■" * 5)
    print("■" * 8 + "射偏" + "■" * 2)
    print("■" * 6 + "角球" + "■" * 4)
    print("■" * 5 + "犯规" + "■" * 5)
    print("■" * 5 + "界外球" + "■" * 4)
    print("■" * 4 + "球门球" + "■" * 6)
    print("■" * 0 + "越位" + "■" * 0)
    print("■" * 0 + "扑救" + "■" * 0)


def tesk7():
    yyy = input("请输入摇一摇")
    if yyy == "摇一摇":
        md = random.choice(('免单', '$0.25'))
        print(md)
    else:
        print("错误")


def directory():
    print("欢迎")
    while 1:
        print("请输入你要调用的功能")
        print("1.破译爬虫项目实践活动的日期密码")
        print("2.用不同的数据类型完成表白")
        print("3.将十进制转换成二进制，八进制，十六进制")
        print("4.输出游戏玩家的功力值")
        print("5.模拟石头，剪刀，布")
        print("6.输出球赛结果对比图")
        print("7.模拟输出摇一摇免单结果")
        taskFunction = int(input())

        if taskFunction == 1:
            tesk1()
        elif taskFunction == 2:
            tesk2()
        elif taskFunction == 3:
            tesk3()
        elif taskFunction == 4:
            tesk4()
        elif taskFunction == 5:
            tesk5()
        elif taskFunction == 6:
            tesk6()
        elif taskFunction == 7:
            tesk7()
        else:
            break


if __name__ == '__main__':
    directory()
