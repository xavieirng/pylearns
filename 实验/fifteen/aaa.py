import pymysql
from beautifultable import BeautifulTable
import sys
def get_input(message=None, integer=False, digit=False, character=False, decimal=False, string=False):
    """获取用户输入信息"""
    if message:
        print(message)
    while True:
        try:
            str_input = input()
            if str_input == 'esc':
            #结束运行的程序
                print('程序已退出')
                sys.exit()
            elif str_input == 'home' or str_input == '':
                    break# 返回首页
            elif string:
                 return str_input
            elif character and str_input.isalnum():
                # 判断所有字符都是数字或者字母
                 return str_input
            elif digit and str_input.isdigit():# 判断所有字符都是数字
                 return int(str_input)
            elif decimal and float(str_input):# 判断所有字符都是十进制数字
                 return float(str_input)
            elif integer and 1 <= int(str_input) <= 16:# 判断是否为1-16间的整数
                 return int(str_input)
            else:
                 print('您输入的指令有误,请重新输入!')
        except ValueError:print('您输入的指令有误,请重新输入!')

def init_print():
    """初始化打印信息"""
    print("=======会员管理系统==========")
    print("1、建立数据库,2、建立数据表，3、添加管理员，4、修改管理员，5、删除管理员，6,添加会员卡,7.删除会员卡,8.查 找 会 员 卡,9.添加会员,13.会员充值,15.会员卡挂失 ,10.修改会员,14.充值查询,16.会员卡挂失查询,11.删除会员 ,12.查 询 会 员")
    return get_input(integer=True)
def change_data(db, cursor, sql):
    """操作数据"""
    try:# 执行sql语句
         cursor.execute(sql)# 提交到数据库执行
         db.commit()
    except:# 发生错误时回滚
        db.rollback()

def select_data(cursor, sql):
    """查询数据"""
    cursor.execute(sql)# 获取数据
    data = cursor.fetchall()# 遍历打印数据
    table = BeautifulTable()
    for row in data:
        table.append_row(row)
    print(table)
    if len(data) == 0:
        print('未查询到任何数据!')

def execute_sql(sql, database='membermanagement'):
     try:
        db = pymysql.connect(host='139.155.68.220', user='root', password='123456', database='mrsofts', charset='utf8')
        cursor = db.cursor()
        for one_sql in sql.split(';')[:-1]:
            if one_sql.startswith('INSERT') or one_sql.startswith('UPDATE') or one_sql.startswith('DELETE'):
                change_data(db, cursor, one_sql)
            else:
                select_data(cursor, one_sql)
        cursor.close()
        db.close()
        print('SQL已执行完成,按回车继续操作!')
        get_input()
     except pymysql.err.InternalError as e:
         print(e)
def find_sql(index):
 sql_data = {2: lambda x: "DROP TABLE IF EXISTS `manager`;CREATE TABLE `manager` ( `id` int(8) unsigned "
 "zerofill NOT NULL AUTO_INCREMENT, `name` varchar(255) NOT NULL, "
 "`phone` varchar(20) NOT NULL, `update_date` datetime DEFAULT NULL, "
 "`create_date` datetime NOT NULL, `is_delete` int(1) NOT NULL DEFAULT '0', "
 "PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;DROP TABLE IF EXISTS "
 "`member`;CREATE TABLE `member` ( `id` int(8) unsigned zerofill NOT NULL "
 "AUTO_INCREMENT, `name` varchar(255) NOT NULL, `phone` varchar(20) NOT NULL, "
 "`update_date` datetime DEFAULT NULL, `create_date` datetime NOT NULL, "
 "`is_delete` int(1) NOT NULL DEFAULT '0', PRIMARY KEY (`id`)) ENGINE=InnoDB"
  "DEFAULT CHARSET=utf8;DROP TABLE IF EXISTS `membercard`;CREATE TABLE `membercard` "
  "( `id` int(8) unsigned zerofill NOT NULL AUTO_INCREMENT, `member_id` int(8) "
  "NOT NULL, `balance` decimal(12,2) DEFAULT '0.00', `create_date` datetime "
  "NOT NULL, `is_delete` int(1) NOT NULL DEFAULT '0', PRIMARY KEY "
  " (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;DROP TABLE IF EXISTS "
  "`recharge`;CREATE TABLE `recharge` ( `id` int(16) unsigned zerofill NOT "
  "NULL AUTO_INCREMENT, `membercard_id` int(8) NOT NULL, `money` decimal(12,"
  "2) NOT NULL, `create_date` datetime NOT NULL, PRIMARY KEY (`id`)) "
  "ENGINE=InnoDB DEFAULT CHARSET=utf8;DROP TABLE IF EXISTS `report`;CREATE TABLE "
  "`report` ( `id` int(8) unsigned zerofill NOT NULL AUTO_INCREMENT, `membercard_id` "
  "int(8) NOT NULL, `create_date` datetime NOT NULL, PRIMARY KEY ("
  "`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;SHOW TABLES;",
3: lambda x: "INSERT "
                          " INTO "
                          "manager("
                          "`name`,phone,"
                          "update_date,"
                          "create_date) "
                          " VALUES "
                          "('%s',%d,"
                          "NOW(),"
                          "NOW());SELECT "
                          " * FROM "
                          "manager;" %
                          (get_input(
                              message='请输入管理员姓名,按回车结束！', string=True),
                           get_input(message='请输入电话号码,按回车结束！', digit=True)),
             5: lambda x: "DELETE FROM manager WHERE id='%d';SELECT * FROM manager;" % get_input(
                 message='请输入将要删除的管理员id,按回车结束！', digit=True), 6: lambda
         x: "INSERT INTO membercard(member_id, create_date) VALUES ('%d', NOW());SELECT * FROM membercard ;" % get_input(
         message='请输入会员id(若无请直接回车,再添加会员),按回车结束！', digit=True),
             7: lambda x: "DELETE FROM membercard WHERE id='%d';SELECT * FROM membercard ;" % get_input(
                 message='请输入会员卡id,按回车结束！', digit=True), 9: lambda
         x: "INSERT INTO member(`name`,phone,update_date,create_date) VALUES ('%s',%d,NOW(),NOW());SELECT * FROM member;" % (
         get_input(message='请输入会员名称,按回车结束！', string=True), get_input(message='请输入电话号码,按回车结束！', digit=True)),
             11: lambda x: "DELETE FROM member WHERE id='%d';SELECT * FROM member;" % get_input(
                 message='请输入将要删除的会员id,按回车结束！', digit=True),
             14: lambda x: "SELECT * FROM recharge WHERE membercard_id='%d';" % get_input(message='请输入会员卡id,按回车结束！',
                                                                                          digit=True),
             16: lambda x: "SELECT * FROM report WHERE id='%d';" % get_input(message='请输入会员卡id,按回车结束！', digit=True)}
 try:
    sql = sql_data[index](1)
 except KeyError as ke:
    sql = ""
 except TypeError as te:
    sql = ""
 return sql

def generate_sql(number):
    sql = ""
    if number == 1:
        sql_create_database = "DROP database IF EXISTS `mrsofts`;CREATE database `mrsofts`;SHOW DATABASES; "
        execute_sql(sql_create_database, database='mysql')
    elif number == 4 or number == 10:
        person_id = get_input(message='请输入将要修改的人员id,按回车结束！', digit=True)
        filed_name_num = get_input(message='请输入将要修改的内容序号,1-姓名,2-电话,按回车结束！', digit=True)
        if filed_name_num == 1:
            filed_name = 'name'
        elif filed_name_num == 2:
            filed_name = 'phone'
        else:
            filed_name = ''
        filed_value = get_input(message='请输入修改后字段的值,按回车结束！', string=True)
        people_table = ('manager' if (number == 4) else 'member')
        sql = "UPDATE %s SET `%s`='%s',update_date=NOW() WHERE id='%s';SELECT * FROM %s;" % (people_table, filed_name, filed_value, person_id, people_table)
    elif number == 8 or number == 12:
        relve_id = get_input(message='请输入相关id,按回车结束,输入all将会查找所有会员卡信息！',string=True)
        table_name = ('membercard' if (number == 8) else 'member')
        if relve_id == 'all':
            sql = "SELECT * FROM %s;"%table_name
        elif relve_id.isdigit():
            sql = "SELECT * FROM %s WHERE id='%d';" % (table_name, int(relve_id))
    elif number == 13:
        membercard_id = get_input(message='请输入会员卡id,按回车结束！',digit=True)
        money = get_input(message='请输入充值金额,按回车结束！', decimal=True)
        sql = "INSERT INTO recharge(membercard_id,money,create_date) VALUES ('%d',%f,NOW());UPDATE membercard SET balance=balance+%f WHERE id=%d;SELECT * FROM membercard WHERE id=%d;" % (membercard_id, money, money, membercard_id, membercard_id)
    elif number == 15:
        membercard_id = get_input(message='请输入会员卡id,按回车结束！', digit=True)
        sql = "INSERT INTO report(membercard_id,create_date) VALUES ('%d',NOW());INSERT INTO membercard(member_id, balance, create_date) VALUES ((selecb.member_id from(SELECT member_id FROM membercard WHERE id=%d)b), (select a.balance from (SELECT balance FROM membercard WHERE id=%d)a), NOW());SELECT * FROM membercard ORDER BY create_date DESC LIMIT 1;" % (membercard_id, membercard_id, membercard_id)
    else:
        sql = find_sql(number)
    execute_sql(sql)
if __name__ == '__main__':
    while True:
        number = init_print()
        generate_sql(number)
