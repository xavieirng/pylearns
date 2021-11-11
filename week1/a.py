import  tkinter as tk

class App:

    def __init__(self, master):
        # 基本界面
        self.master = master
        # 输入组件
        self.initWidgets()
        # 表达式
        self.hi = None

    def initWidgets(self):
        # 创建一个输入组件
        self.show = tk.Label(relief=tk.SUNKEN, width=23,
                             bg="white", anchor=tk.W)
        # 对该输入组件使用pack布局
        self.show.pack(side=tk.TOP, pady=10)
        p = tk.Frame(self.master)
        p.pack(side=tk.TOP)
        # 定义字符串的元组
        names = ("1", "2", "3", "4", "5", "6",
                 "7", "8", "9", "0", ".", "+", "-", "*", "**", "//", "/", "%", "=", "☭",)
        # 遍历元组
        for i in range(len(names)):
            # 创建按钮，放入frame中
            b = tk.Button(p, text=names[i], width=5)
            b.grid(row=i // 5, column=i % 5)
            # b.pack(side=tk.LEFT, padx=0, pady=5)
            # 为鼠标左键的单击事件绑定事件处理方法
            b.bind("<Button-1>", self.click)
            # 为鼠标左键双击事件绑定事件处理方法
            if b["text"] == "☭":
                b.bind("<Button-1>", self.clean)
        # 定义一个记录输入数字次数的变量
        self.i = 0

    def click(self, event):
        # 如果用户单击数字或点号
        if (event.widget["text"] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")):
            # 判断self.i是否为0，0的话清空show【”text“】的值
            if self.i == 0:
                self.show["text"] = ""
            self.show["text"] = self.show["text"] + event.widget["text"]
            self.i = self.i + 1
            print(self.i)
        # 如果用户单击了运算符
        elif (event.widget["text"] in ("+", "-", "*", "/", "%", "**", "//")):
            self.show["text"] = self.show["text"] + event.widget["text"]
        elif (event.widget["text"] == "=" and self.show["text"] is not None):
            # 赋值给self.hi
            self.hi = self.show["text"]
            # 调试时使用
            print(self.hi)
            # 使用eval（）函数计算结果
            self.show["text"] = str(eval(self.hi))
            self.hi = None
            self.i = 0

    def clean(self, event):
        # 点击恢复按钮时，清空表达式，计数器清空
        self.hi = None
        self.show["text"] = ""


root = tk.Tk()
root.title("计算器")
App(root)
root.mainloop()