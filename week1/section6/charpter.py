def task1():
    xl = [89, 98, 00, 75, 68, 37, 58, 90]
    print(xl)
    for index, item in enumerate(xl):
        if xl[index] > 20:
            xl[index] += 1900
        else:
            xl[index] += 2000
    xl.sort()
    print(xl)


def task4():
    xl = ["89", "98", "00", "75", "68", "37", "58", "90"]
    print(xl)
    for index, item in enumerate(xl):
        if xl[index] != "00":
            xl[index] = "19" + xl[index]
        else:
            xl[index] = "20" + xl[index]
    xl.sort()
    print(xl)


def task2():
    lastWeek = [4235, 5612, 8447, 11250, 9211, 9985, 3783]
    thisWeek = [4235, 10111, 8447, 9566, 9788, 8951, 9808]
    week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]
    he = []
    for i in range(7):
        he.append(lastWeek[i] + thisWeek[i])
    print(he)
    # he1=he
    he.sort()
    print("升序输出：", he)
    he.sort(reverse=True)
    print("降序输出：", he)
    tweek = []
    tweek = thisWeek[:]
    thisWeek.sort()
    print(thisWeek)

    min = week.insert(tweek.index(thisWeek[0]) + 1, thisWeek[0])
    max = week.insert(tweek.index(thisWeek[6]) + 2, thisWeek[6])
    print(week)

    ls = [x for x in lastWeek if x > 8000]

    ts = [x for x in thisWeek if x > 8000]
    print("上周大于8000步", ls)
    print("本周大于8000布", ts)
    print("上周求和", sum(lastWeek))
    print("本周求和", sum(thisWeek))


def task3():
    products = [[], [], [], [], []]
    print("请输出产品")
    for i in range(5):
        products[i].append(input("输入编号"))
        products[i].append(input("输入产品名"))
    print(products)
    cp = []
    cp1 = []
    while True:
        print("请输入你要使用的功能")
        print("1.添加产品")
        print("2.购买产品")
        print("3.查看购物车")
        gn = int(input())

        if gn == 1:
            cp.append(input("输入编号"))
            cp.append(input("输入产品名"))
            products.append(cp)
            print(products)
        if gn == 2:
            print("请输入你要购买的产品编号")
            cpbh = input()
            for index, item in enumerate(products):
                # print(item)
                # print(item[0])
                if item[0] == cpbh:
                    cp.append(item)

        if gn == 3:
            print(cp)


if __name__ == '__main__':
    task2()
