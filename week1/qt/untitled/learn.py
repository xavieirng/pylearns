from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

a = ''
b = ''
sum = ''
symbol = ''


class mainpage():

    def __init__(self):
        self.ui = QUiLoader().load("form.ui")
        self.ui.btn1.clicked.connect(self.setnum1)
        self.ui.btn2.clicked.connect(self.setnum2)
        self.ui.btn3.clicked.connect(self.setnum3)
        self.ui.btn4.clicked.connect(self.setnum4)
        self.ui.btn5.clicked.connect(self.setnum5)
        self.ui.btn6.clicked.connect(self.setnum6)
        self.ui.btn7.clicked.connect(self.setnum7)
        self.ui.btn8.clicked.connect(self.setnum8)
        self.ui.btn9.clicked.connect(self.setnum9)
        self.ui.btn0.clicked.connect(self.setnum0)
        self.ui.btnadd.clicked.connect(self.setadd)
        self.ui.btnres.clicked.connect(self.result)
        self.ui.btndiv.clicked.connect(self.setdiv)
        self.ui.btnsub.clicked.connect(self.setsub)
        self.ui.btnpow.clicked.connect(self.setpow)
        self.ui.btnmul.clicked.connect(self.setmul)
        self.ui.btnce.clicked.connect(self.setce)


    def setce(self):
        global a, b,sum, symbol
        a = ''
        b = ''
        sum = ''
        symbol = ''
        self.showlable()
    def setnum1(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn1.text().strip()
        else:
            b = b + self.ui.btn1.text().strip()
        self.showlable()

    def setnum2(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn2.text().strip()
        else:
            b = b + self.ui.btn2.text().strip()
        self.showlable()

    def setnum3(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn3.text().strip()
        else:
            b = b + self.ui.btn3.text().strip()
        self.showlable()

    def setnum4(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn4.text().strip()
        else:
            b = b + self.ui.btn4.text().strip()
        self.showlable()

    def setnum5(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn5.text().strip()
        else:
            b = b + self.ui.btn5.text().strip()
        self.showlable()

    def setnum6(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn6.text().strip()
        else:
            b = b + self.ui.btn6.text().strip()
        self.showlable()

    def setnum7(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn7.text().strip()
        else:
            b = b + self.ui.btn7.text().strip()
        self.showlable()

    def setnum8(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn8.text().strip()
        else:
            b = b + self.ui.btn8.text().strip()
        self.showlable()

    def setnum9(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn9.text().strip()
        else:
            b = b + self.ui.btn9.text().strip()
        self.showlable()

    def setnum0(self):
        global a, b, symbol
        if symbol == '':
            a = a + self.ui.btn0.text().strip()
        else:
            b = b + self.ui.btn0.text().strip()
        self.showlable()

    def setnum(self):
        pass

    def showlable(self):
        global a, b, sum,symbol
        if sum=='':
            self.ui.label.setText(str(a) + symbol + str(b) )
        else:
            self.ui.label.setText(str(a) + symbol + str(b) + '=' + str(sum))

    def setadd(self):
        global symbol
        symbol = '+'
        self.showlable()

    def setsub(self):
        global symbol
        symbol = '-'
        self.showlable()
    def setdiv(self):
        global symbol
        symbol = '/'
        self.showlable()
    def setpow(self):
        global symbol
        symbol = '**'
        self.showlable()
    def setmul(self):
        global symbol
        symbol = '*'
        self.showlable()
    def setsymbol(self):
        global symbol
        symbol = self.ui.btnadd.text().strip()
        self.showlable()

    def result(self):
        global a, b, sum, symbol
        sa = float(a)
        sb = float(b)
        if symbol == '+':
            sum = int(a) + int(b)
        if symbol == '-':
            sum = int(a) - int(b)
        if symbol == '*':
            sum = int(a) * int(b)
        if symbol == '/':
            sum = int(a) / int(b)
        if symbol == '**':
            sum = int(a) ** int(b)

        self.showlable()
        a = sum
        sum=''
        b=''

if __name__ == '__main__':
    app = QApplication([])
    stats = mainpage()
    stats.ui.show()
    app.exec()
