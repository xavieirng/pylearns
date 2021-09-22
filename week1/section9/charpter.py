def task1():
    asciistring = input("请输入")
    if (ord(asciistring) <= 90 and ord(asciistring) >= 65) or (ord(asciistring) >= 97 and ord(asciistring) <= 122) or (
            ord(asciistring) >= 48 and ord(asciistring) <= 57):
        print(asciistring + "   ascii   is   " + str(ord(asciistring)))
    else:
        print("输入非法字符")


def task2():
    for i in range(20):
        print("*" * i)


def task3():
    plutocrat = [
        [1, "杰夫·贝索斯", 1284, 54, "科技", "美国"],
        [2, "比尔·盖茨", 915, 62, "科技", "美国"],
        [3, "沃伦·巴菲特", 879, 87, "投资", "美国"],
        [4, "伯纳德·阿诺特及家族", 764, 69, "商业", "法国"],
        [5, "马克·扎克伯格", 735, 33, "科技", "美国"],
        [6, "卡洛斯·斯利姆·埃卢及家族", 695, 78, "科技", "墨西哥"],
        [7, "阿曼西奥·奥特加", 660, 81, "商业", "西班牙"],
        [8, "拉里·埃里森", 632, 73, "科技", "美国"],
        [9, "大卫·科赫", 608, 77, "能源", "美国"],
        [10, "查尔斯·科赫", 608, 82, "能源", "美国"],

        [11, "拉里·佩奇", 522, 44, "科技", "美国"],
        [12, "迈克尔·布隆伯格", 508, 76, "科技", "美国"],
        [13, "谢尔盖·布林", 508, 44, "科技", "美国"],
        [14, "马化腾", 491, 46, "科技", "中国"],
        [15, "梅耶尔·贝当古", 446, 64, "商业", "法国"],
        [16, "吉姆·沃尔顿", 419, 69, "商业", "美国"],
        [17, "S·罗伯森·沃尔顿", 418, 73, "商业", "美国"],
        [18, "爱丽森·沃尔顿", 416, 68, "商业", "法国"],
        [19, "谢尔登·安德尔森", 411, 84, "娱乐", "美国"],
        [20, "马云", 406, 53, "科技", "中国"],
    ]
    newplutocrat = []
    newplutocrats = ""
    for item in plutocrat:
        if item[4] == "科技":
            newplutocrat.append(item)
            newplutocrats = newplutocrats + ",".join(str(i) for i in item) + "\n"
    # print(newplutocrat)
    file = open("NEW.txt", 'w')
    file.write(newplutocrats)
    file.close()


if __name__ == '__main__':
    task3()
