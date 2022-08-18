from tkinter import *
from tkinter import ttk
import pandas as pd
from pandas import *
import numpy as np
from openpyxl import *

result = []
formula = []


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(0, 0)  # 设置窗口不可拉伸
        self.master.geometry('800x420')  # 设置主窗口的初始尺寸

        self.result = StringVar()  # 用于显示结果的可变文本
        self.equation = StringVar()  # 显示计算方程
        self.result.set(' ')
        self.equation.set('0')
        # 显示框
        self.show_result_eq = Label(self.master, bg='white', fg='black',
                                    font=('Arail', '16'), bd='0',
                                    textvariable=self.equation, anchor='se')
        self.show_result = Label(self.master, bg='white', fg='black',
                                 font=('Arail', '20'), bd='0',
                                 textvariable=self.result, anchor='se')
        # 按钮
        self.button_back = Button(self.master, text='<-', bg='DarkGray', command=self.back)  # 返回
        self.button_lbracket = Button(self.master, text='(', bg='DarkGray', command=lambda: self.getNum('('))  # 左括号
        self.button_rbracket = Button(self.master, text=')', bg='DarkGray', command=lambda: self.getNum(')'))  # 左括号
        self.button_division = Button(self.master, text='÷', bg='DarkGray', command=lambda: self.getNum('÷'))  # 除号
        # 7 8 9 4 5 6 1 2 3
        self.button_7 = Button(self.master, text='7', bg='DarkGray', command=lambda: self.getNum('7'))  # 7号
        self.button_8 = Button(self.master, text='8', bg='DarkGray', command=lambda: self.getNum('8'))  # 8号
        self.button_9 = Button(self.master, text='9', bg='DarkGray', command=lambda: self.getNum('9'))  # 9号
        self.button_multiplication = Button(self.master, text='*', bg='DarkGray',
                                            command=lambda: self.getNum('*'))  # 乘号
        # 按钮的command参数,是回调函数。lambda函数是为了可以传参数给回调函数
        self.button_4 = Button(self.master, text='4', bg='DarkGray', command=lambda: self.getNum('4'))  # 4号
        self.button_5 = Button(self.master, text='5', bg='DarkGray', command=lambda: self.getNum('5'))  # 5号
        self.button_6 = Button(self.master, text='6', bg='DarkGray', command=lambda: self.getNum('6'))  # 6号
        self.button_minus = Button(self.master, text='-', bg='DarkGray', command=lambda: self.getNum('-'))  # -号

        self.button_1 = Button(self.master, text='1', bg='DarkGray', command=lambda: self.getNum('1'))  # 1号
        self.button_2 = Button(self.master, text='2', bg='DarkGray', command=lambda: self.getNum('2'))  # 2号
        self.button_3 = Button(self.master, text='3', bg='DarkGray', command=lambda: self.getNum('3'))  # 3号
        self.button_plus = Button(self.master, text='+', bg='DarkGray', command=lambda: self.getNum('+'))  # +号
        # 控制按钮 0 .
        self.button_MC = Button(self.master, text='MC', bg='DarkGray', command=self.clear)  # MC
        self.button_0 = Button(self.master, text='0', bg='DarkGray', command=lambda: self.getNum('0'))  # 0
        self.button_dot = Button(self.master, text='.', bg='DarkGray', command=lambda: self.getNum('.'))  # .
        self.button_eq = Button(self.master, text='=', bg='DarkGray', command=self.run)  # =

        # Layout布局
        self.show_result_eq.place(x='10', y='10', width='300', height='50')
        self.show_result.place(x='10', y='60', width='300', height='50')

        self.button_back.place(x='10', y='150', width='60', height='40')
        self.button_lbracket.place(x='90', y='150', width='60', height='40')
        self.button_rbracket.place(x='170', y='150', width='60', height='40')
        self.button_division.place(x='250', y='150', width='60', height='40')
        self.button_7.place(x='10', y='205', width='60', height='40')
        self.button_8.place(x='90', y='205', width='60', height='40')
        self.button_9.place(x='170', y='205', width='60', height='40')
        self.button_multiplication.place(x='250', y='205', width='60', height='40')
        self.button_4.place(x='10', y='260', width='60', height='40')
        self.button_5.place(x='90', y='260', width='60', height='40')
        self.button_6.place(x='170', y='260', width='60', height='40')
        self.button_minus.place(x='250', y='260', width='60', height='40')

        self.button_1.place(x='10', y='315', width='60', height='40')
        self.button_2.place(x='90', y='315', width='60', height='40')
        self.button_3.place(x='170', y='315', width='60', height='40')
        self.button_plus.place(x='250', y='315', width='60', height='40')

        self.button_MC.place(x='10', y='370', width='60', height='40')
        self.button_0.place(x='90', y='370', width='60', height='40')
        self.button_dot.place(x='170', y='370', width='60', height='40')
        self.button_eq.place(x='250', y='370', width='60', height='40')

        # 查询表格
        columns = ("计算式", "结果")
        self.master = ttk.Treeview(self.master, height=18, show="headings", columns=columns)  # 表格
        self.master.column("计算式", width=250, anchor='center')  # 表示列,不显示
        self.master.column("结果", width=100, anchor='center')
        self.master.heading("计算式", text="计算式")  # 显示表头
        self.master.heading("结果", text="结果")
        self.master.pack(side=LEFT, fill=BOTH)
        self.master.place(x='400', y='10', width='350', height='400')   # 表格位置
        name = ['']
        ipcode = ['']
        for i in range(min(len(name), len(ipcode))):  # 写入数据
            self.master.insert('', i, values=(name[i], ipcode[i]))

    def back(self):
        temp_equ = self.equation.get()
        self.equation.set(temp_equ[:-1])  # 一个一个删

    def getNum(self, arg):
        temp_equ = self.equation.get()  # 输入算式
        print(temp_equ)
        temp_result = self.result.get()

        # 判断基本语法错误
        if temp_result != ' ':  # 计算器输入前还没有结果，那么结果区域应该设置为空。
            self.result.set(' ')
        if temp_equ == '0' and (arg not in ['.', '+', '-', '*', '÷']):  # 如果首次输入为0，则紧跟则不能是数字，只是小数点或运算符
            temp_equ = ''
        if len(temp_equ) > 2 and temp_equ[-1] == '0':  # 运算符后面也不能出现0+数字的情形03，09，x
            if (temp_equ[-2] in ['+', '-', '*', '÷']) and (
                    arg in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']):
                temp_equ = temp_equ[:-1]
        temp_equ = temp_equ + arg
        self.equation.set(temp_equ)

    def clear(self):
        self.equation.set('0')
        self.result.set(' ')

    def run(self):
        temp_equ = self.equation.get()
        temp_equ = temp_equ.replace('÷', '/')
        if temp_equ[0] in ['+', '-', '*', '÷']:
            temp_equ = '0' + temp_equ
            print(temp_equ)
        try:
            formula.append(temp_equ)
            answer = '%.4f' % eval(temp_equ)  # 保留两位小数
            self.result.set(str(answer))
            result.append(answer)
            print(result)
        except (ZeroDivisionError, SyntaxError):  # 其他除0错误，或语法错误返回Error
            self.result.set(str('Error'))


def save_record(result, formula):
    equ = {'计算式': formula, '结果': result}
    data = pd.DataFrame(equ)
    writer = pd.ExcelWriter('A.xlsx')  # 写入Excel文件
    data.to_excel(writer, 'page_1', float_format='%.5f')  # ‘page_1’是写入excel的sheet名
    writer.save()
    writer.close()


def open_excel():
    workbook = load_workbook(r'.\A.xlsx')
    sheet1 = workbook['page_1']
    data = []
    for row in sheet1.rows:
        list = []
        for cell in row:
            aa = str(cell.value)
            if aa == "":
                aa = "1"
            list.append(aa)
        data.append(list)
    print(data)


if __name__ == "__main__":
    open_excel()
    root = Tk()
    my_cal = Calculator(root)
    root.mainloop()
    save_record(result, formula)
