sdate = (20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 21)
sstar = ("摩羯座", "水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座", "射手座", "摩羯座")
indate = input("请输入您的生日(格式：2018:10:12)：")
instr = indate.split(":")
year = int(instr[0])
month = int(instr[1])
date = int(instr[2])
if date >= sdate[month - 1]:
    print("您的星座是：" + sstar[month])
else:
    print("您的星座是：" + sstar[month - 1])
