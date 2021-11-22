import  pymysql
class sqllearn():
    def __init__(self):
        self.db = pymysql.connect(host="139.155.68.220", user="root", password='123456', database='mrsoft', port=3306)
        self.cursor = self.db.cursor()
    def createtable(self):
        create_sql='''
                create table manaager(
                    id int not null ,
                    name varchar(20)  not null ,
                    password varchar(20) not null ,
                    post varchar (20) null ,
                    primary key (id)
                )
        '''
        self.cursor.execute(create_sql)
    def insert_sql(self):
        sql = "insert into manager(id,name,password,post) value (2,'其志恒','123456','组长')"
        sql1 = "insert into manager(id,name,password,post) value (3,'zhangjiahao','666666','打工人  ')"
        self.cursor.execute(sql)
        self.cursor.execute(sql1)
        self.db.commit()
        print("ok")
    def delete_sql(self):
        sql = "delete from manager where name='admin'"
        self.cursor.execute(sql)
        self.db.commit()
        print("ok")
    def update_sql(self):
        sql = "update manager set name='qi志恒' where name='其志恒'"
        self.cursor.execute(sql)
        self.db.commit()
        print("ok")
    def exit_sql(self):
        self.cursor.close()
        self.db.close()
    def select_sql(self):
        res=self.cursor.fetchone()
        self.db.commit()
        print(res)
        print("ok")
if __name__ == '__main__':
    sqllearn=sqllearn()
    sqllearn.insert_sql()
