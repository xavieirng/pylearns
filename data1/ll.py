try:  # 添加异常处理
    ##函数showall()显示当前已注册用户信息###################################
    def showall():
        try:
            import sqlite3
            cn = sqlite3.connect('E:/chapter8_do_db.db')
            cur = cn.execute('select * from users')
            users = cur.fetchall()
            if len(users) == 0:
                print('\t当前无注册用户')
            else:
                print('\t当前已注册用户信息如下：')
                n = 0
                for x in users:  # 遍历用户列表，打印用户信息
                    for a in x:
                        print('\t  ', a, end='\t')
                    print()
            cn.close()
            input('\n\t按Enter键继续......\n')  # 完成操作后，暂停
        except Exception as ex:
            print('\t数据库访问出错：', ex)
            raise ex


    ##函数showall()代码结束

    ##函数check_update()执行查找、修改或删除操作#############################
    def check_update():
        try:
            import sqlite3
            cn = sqlite3.connect('E:/chapter8_do_db.db')
            uname = input('\t请输入要查找的用户名:')
            if find(uname) == -1:
                print('\t%s 还未注册！' % uname)
            else:
                # 用户名已注册，执行修改或删除操作
                print('\t%s 已经注册！' % uname)
                print('\t请选择操作：')
                print('\t  1.修改用户')
                print('\t  2.删除用户')
                op = input('\t请输入序号选择对应操作：')
                if op == '2':
                    # 删除用户
                    cn.execute('delete from users where userid=?', (uname,))
                    cn.commit()
                    print('\n\t  已成功删除用户！')
                else:
                    # 修改用户信息
                    newname = input('\t请输入新的用户名:')
                    if newname == '':
                        print('\t用户名输入无效！')
                    else:
                        # 检查是否已存在同名的注册用户
                        if find(newname) == 1:
                            print('\t你输入的用户名已经使用！')
                        else:
                            pwd = input('\t请输入新用户登录密码:')
                            if pwd == '':
                                print('\t登录密码输入无效！')
                            else:
                                cn.execute('update users set userid=?,password=? where userid=?', (newname, pwd, uname))
                                cn.commit()
                                print('\n\t已成功修改用户！')
            cn.close()
            input('\n\t按Enter键继续......\n')
        except Exception as ex:
            print('\t数据库访问出错：', ex)
            raise ex
        ##函数check_update()代码结束


    ##函数adduser()添加新用户#############################################
    def adduser():
        try:
            import sqlite3
            cn = sqlite3.connect('E:/chapter8_do_db.db')
            uname = input('\t请输入新的用户名:')
            if uname == '':
                print('\t用户名输入无效！')
            else:
                # 检查是否已存在同名的注册用户
                if find(uname) == 1:
                    print('\t你输入的用户名已经使用，请重新添加用户！')
                else:
                    pwd = input('\t请输入新用户登录密码:')
                    if pwd == '':
                        print('\t登录密码输入无效！')
                    else:
                        cn.execute('insert into users values(?,?)', (uname, pwd))
                        cn.commit()
                        print('\t已成功添加用户！')
            cn.close()
            input('\n\t按Enter键继续......')
        except Exception as ex:
            print('\t数据库访问出错：', ex)
            raise ex
        ##函数adduser()代码结束


    ##函数find(namekey)查找是否存在用户名为namekey的注册用户#####################
    def find(namekey):
        try:
            import sqlite3
            cn = sqlite3.connect('E:/chapter8_do_db.db')
            cur = cn.execute('select * from users where userid=?', (namekey,))
            user = cur.fetchall()
            # 如果存在与namekey值同名的用户，返回1，否则返回-1
            if len(user) > 0:
                n = 1
            else:
                n = -1
            cn.close()
            return n
        except Exception as ex:
            print('\t数据库访问出错：', ex)
            raise ex
        ##函数find(namekey)代码结束


    ##函数resetdb()重置用户数据库（删除已注册用户数据）###################################
    def resetdb():
        try:
            import sqlite3
            cn = sqlite3.connect('E:/chapter8_do_db.db')
            cn.execute('drop table if exists users')
            cn.execute('create table users(userid text primary key,password text)')
            cn.close()  # 关闭文件
            print('\t已成功重置用户数据库')
            input('\n\t按Enter键继续......')
        except Exception as ex:
            print('\t数据库访问出错：', ex)
            raise ex
        ##函数save()代码结束


    # 以死循环显示系统操作菜单，直到选择退出系统###########################################
    while True:
        print('用户注册信息管理系统')
        print('\t1.显示全部已注册用户')
        print('\t2.查找/修改/删除用户信息')
        print('\t3.添加新用户')
        print('\t4.创建/重置用户数据库')
        print('\t5.退出系统')
        no = input('请输入序号选择对应菜单：')
        if no == '1':
            showall()  # 显示全部用户信息
        elif no == '2':
            check_update()  # 执行查找、修改或删除操作
        elif no == '3':
            adduser()  # 执行添加新用户操作
        elif no == '4':
            resetdb()  # 重置用户数据库
        elif no == '5':
            print('谢谢使用，系统已退出')
            break
except Exception as ex:  ###系统异常处理，写异常日志文件##############################################
    from traceback import print_tb  # 导入print_tb打印堆栈跟踪信息
    from datetime import datetime  # 导入日期时间类，为异常日志文件写入当前日期时间

    log = open('chapter6_do_log.txt', 'a')  # 打开异常日志文件
    x = datetime.today()  # 获得当前日期时间
    # 为用户显示异常日志信息
    print('\n出错了：')
    print('日期时间：', x)
    print('异常信息：', ex)
    print('堆栈跟踪信息：')
    print_tb(ex.__traceback__)

    # 将异常日志信息写入文件
    print('\n出错了：', file=log)
    print('日期时间：', x, file=log)
    print('异常信息：', ex.args[0], file=log)
    print('堆栈跟踪信息：', file=log)
    print_tb(ex.__traceback__, file=log)
    log.close()  # 关闭异常日志文件
    print('发生了错误，系统已退出')


