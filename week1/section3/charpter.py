from numpy import double


def tesk1():
    number1 = 0o267
    number2 = 0b10110001
    number3 = 0Xe3a5
    print("0o267的8进制数转化十进制:")
    print(int(number1))
    print("0b10110001的2进制数转化十进制数")
    print(int(number2))
    print("0Xe3a5的16进制数转化十进制数")
    print(int(number3))


def tesk2():
    num1 = double(input("请输入底数："))
    num2 = double(input("请输入幂："))
    print(str(num1 ** num2))


def tesk3():
    money = float(input("请输入加油的钱数"))
    mileage = float(input("请输入运行的公里数"))
    fuel = money / 8
    fuel = fuel / mileage * 100

    print("您车辆的油耗为：" + str(fuel) + "/100.每公里花费为:" + str(money / mileage) + "元")
    total = int(input("请输入车辆一年运行的总的公里数："))
    print("您的车辆一年的油费为：" + str(money / mileage * total) + "元")


def tesk4():
    Fahrenheit = float(input("请输入华氏摄氏度："))
    print("转化后的摄氏度为：" + str((Fahrenheit - 32) * 5 / 9))


def directory():
    print("欢迎")
    while 1:
        print("请输入你要调用的功能")
        print("1.爱国者导弹总数量")
        print("2.奋斗的青春最美丽")
        print("3.计算汽车平均油耗")
        print("4.华氏温度转换成摄氏度")
        taskFunction = int(input())

        if taskFunction == 1:
            tesk1()
        elif taskFunction == 2:
            tesk2()
        elif taskFunction == 3:
            tesk3()
        elif taskFunction == 4:
            tesk4()
        else:
            break


if __name__ == '__main__':
    directory()
