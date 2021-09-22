import datetime
import time

for i in range(10):
    day = 10 - datetime.datetime.now().day
    hour = 24 - datetime.datetime.now().hour
    minute = 60 - datetime.datetime.now().minute
    second = 60 - datetime.datetime.now().second
    print("距离结束" + str(day) + "天" + str(hour) + "时" + str(minute) + "分" + str(second) + "秒")
    time.sleep(1)
