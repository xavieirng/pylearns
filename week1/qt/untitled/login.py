# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

import pymysql
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        self.ui = QUiLoader().load("login.ui")
        self.ui.login.clicked.connect(self.login)
        self.db = pymysql.connect(host="139.155.68.220", user="root", password='123456', database='users', port=3306)
        self.cursor = self.db.cursor()

    def login(self):
        username = self.ui.username.text().strip()
        password = self.ui.password.text().strip()

        sql = "select * from user where username = %s and  password = %s"
        ok= self.cursor.execute(sql,(username,password))
        self.db.commit()
        result = self.cursor.fetchall()
        if ok:
            print('登录成功')
        else:
            print('登录失败')
            self.ui.close()





if __name__ == "__main__":
    app = QApplication([])
    stats = MainWindow()
    stats.ui.show()
    app.exec()
