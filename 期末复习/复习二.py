

import pymysql
db=pymysql.connect(host='139.155.68.220',user='root',password='123456',port=3306,database='mydb')
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS students")
sql='''
CREATE TABLE students(
id int(8) not null auto_increment primary key,
name varchar(50) not null,
sex varchar(2) not null,
age int(3) DEFAULT NULL,
class varchar(10) default null
) ENGINE=MyISAM auto_increment=1 default charset=utf8
'''

cursor.execute(sql)

cursor.execute("insert into students values (1,'limie','nv',18,'1ban')");
cursor.execute("insert into students values (2,'liuda','an',20,'3ban')");
cursor.execute("insert into students values (3,'hmm','nv',19,'5ban')");
cursor.execute("insert into students values (4,'zhangpi','an',18,'7ban')");
result=cursor.fetchall()
cursor.close()
db.close()