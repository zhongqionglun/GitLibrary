# -*-coding:UTF-8-*-
from win32com.client import Dispatch
import win32com.client
from tkinter import *
import os, datetime, string

"""
auth:zhongqionglun
time:2019/03/29
description: 统计项目中每人每天测试用例数
"""


def cases_days():
    testers = member.get().split("|")
    print(testers)
    xlApp = win32com.client.Dispatch('Excel.Application')
    filepath = os.getcwd() + "\\" + filename.get() + ".xls"
    xlBook = xlApp.Workbooks.Open(filepath)
    # print(xlBook)
    xlSheet = xlBook.Worksheets("Worksheet")
    dic = dict.fromkeys(testers)
    # print(dic)
    for tester in testers:
        row = 6
        numday = dict.fromkeys(list(range(1, 31)), 0)
        # print(numday)
        while True:
            if not xlSheet.Cells(row, 1).Value:

                dic[tester] = numday
                # print(dic)
                break
            elif (xlSheet.Cells(row, 7).Value == tester):
                # print(xlSheet.Cells(row, 7))
                # days.append(xlSheet.Cells(row, 6).Value)
                # print(days)
                for day in range(1, 31):
                    # print("the day is : %s" % day)
                    if datetime.datetime.now().month >= 10:
                        substring = "2019-" + str(datetime.datetime.now().month) + "-" + str(day)
                    else:
                        if day >= 10:
                            substring = "2019-0" + str(datetime.datetime.now().month) + "-" + str(day)
                        else:
                            substring = "2019-0" + str(datetime.datetime.now().month) + "-0" + str(day)
                    # print(substring)
                    if not str(xlSheet.Cells(row, 6).Value).find(substring):
                        numday[day] = numday.get(day) + 1
                        # print(numday.get(day))
                        # print(numday)
                        break

            row += 1
            continue
    print(dic)


def writeexcel():
    outfilename = "执行效率月统计结果.xlsx"
    xlApp = win32com.client.Dispatch('Excel.Application')
    if os.path.exists("执行效率月统计结果.xlsx"):
        print("The file is exists....")
        # 判断shett是否存在，一个tester一个sheet#

    else:
        print("The file isn't exists....")


window = Tk()
window.title('用例执行分析')
window.iconbitmap('py-blue-trans-out.ico')
form = Frame(window)
form.pack()
lab1 = Label(form, text='文件名：')
filename = StringVar()
ent1 = Entry(form, textvariable=filename)
filename.set("")
lab1.grid(row=0, column=0)
ent1.grid(row=0, column=1)
lab2 = Label(window, text="测试成员：")
lab2.pack()
member = StringVar()
ent2 = Entry(window, width=40, textvariable=member)
member.set("")
ent2.pack()
btn = Button(window, text='统计', command=cases_days)
btn.pack()
window.mainloop()
