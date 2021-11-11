import pymysql

db = pymysql.connect(host="139.155.68.220", user="root", password='123456', database='mrsoft',port=3306)
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("database version: %s" % data)
db.close()
