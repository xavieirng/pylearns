

import pymysql
db = pymysql.connect(host="139.155.68.220", user="root", password="123456",database= "mydb",port=3306)
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS books")
sql = """
CREATE TABLE books (
  id int(8) NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  category varchar(50) NOT NULL,
  price decimal(10,2) DEFAULT NULL,
  publisher varchar(50) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;    
"""
cursor.execute(sql)
cursor.execute("insert into books values(1,'数据结构','计算机类',58,'人民邮电出版社')")
cursor.execute("insert into books values(2,'计算机基础','计算机类',26,'电子工业出版社')")
cursor.execute("insert into books values(3,'软件工程','计算机类',26,'人民邮电出版社')")
cursor.execute("update books set publisher='清华大学出版社' where id=2")
cursor.execute("select * from books where publisher='清华大学出版社'")
result=cursor.fetchall()
print(result)
cursor.execute("delete from books where publisher='清华大学出版社'")
cursor.close()
db.close()
