import time

import wx


# 任务一


def printstr():
    asciistring = input("请输入")
    for i in range(len(asciistring)):
        print(asciistring[i] + "   ascii   is   " + str(ord(asciistring[i])))


# 任务二
def task2():
    print("请输入消费金额")
    money = float(input())
    if money <= 0:
        print("支付失败")
    else:
        print("付款金额为:" + str(money))
        print("支付成功，对方已收款")


# 任务三
def task3():
    print("枯藤老树昏鸦，")
    print("小桥流水人家。")
    print("空调Wifi西瓜")
    print("啤酒烧烤小龙虾")


# 任务四
def task4():
    nowtime = int(time.time())
    strtime = '2021-11-11 00:00:00'
    after = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
    after = int(time.mktime(after))
    secounds = (after - nowtime)
    day = int(secounds / 60 / 60 / 24)
    hour = int((secounds % (60 * 60 * 24)) / 3600)
    minutes = int((secounds % (60 * 60 * 24)) % 3600 / 60)
    secound = int((secounds % (60 * 60 * 24)) % 3600 % 60)
    print(str(day) + "天" + str(hour) + "时" + str(minutes) + "分" + str(secound) + "秒")


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="成语接龙", size=(1000, 600))
        panel = wx.Panel(self)
        height = 100
        weight = 100
        self.bt_liang = wx.Button(panel, label="两", pos=(height, weight), size=(50, 50))
        self.bt_quan = wx.Button(panel, label="全", pos=(height + 50 + 20, weight), size=(50, 50))
        self.tc_qi = wx.TextCtrl(panel, pos=(height + 50 * 2 + 20 * 2, weight), size=(50, 50))
        self.bt_mei = wx.Button(panel, label="美", pos=(height + 50 * 3 + 20 * 3, weight), size=(50, 50))
        self.bt_le = wx.Button(panel, label="乐", pos=(height + 50 * 2 + 20 * 2, weight + 50 + 20), size=(50, 50))
        self.bt_wu = wx.Button(panel, label="无", pos=(height + 50 * 2 + 20 * 2, weight + 50 * 2 + 20 * 2),
                               size=(50, 50))
        self.bt_qiong = wx.Button(panel, label="穷", pos=(height + 50 * 2 + 20 * 2, weight + 50 * 3 + 20 * 3),
                                  size=(50, 50))

        self.bt_sr = wx.Button(panel, label="输入", pos=(600, 300), size=(200, 100))
        self.bt_sr.Bind(wx.EVT_BUTTON, self.OncickSubmit)

    def OncickSubmit(self, event):
        qi = self.tc_qi.GetValue()
        if qi == "其":
            message = "输入正确"
        else:
            message = "输入错误"
        wx.MessageBox(message)


'''
目录
'''


def directory():
    print("欢迎")
    while 1:
        print("请输入你要调用的功能")
        print("1.输出字母，数字或符号的ascii状态码")
        print("2.模拟微信支付实现付款功能")
        print("3.输出向往的生活场景")
        print("4.模拟特价商品销售倒数计时提醒")
        print("5.模拟成语填空游戏")
        taskFunction = int(input())

        if taskFunction == 1:
            printstr()
        elif taskFunction == 2:
            task2()
        elif taskFunction == 3:
            task3()
        elif taskFunction == 4:
            task4()
        elif taskFunction == 5:
            app = wx.App()
            frame = MyFrame(parent=None, id=-1)
            frame.Show()
            app.MainLoop()
        else:
            break


if __name__ == '__main__':
    directory()
