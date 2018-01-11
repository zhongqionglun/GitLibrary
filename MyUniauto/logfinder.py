# -*- coding:UTF-8 -*-
from tkinter import *
from tkinter import messagebox
import os


errfilelist = []


def errlogfind():
    dir = ent1var.get()
    errstringslist = ent2var.get().split()
    for parent, dirnames, filenames in os.walk(dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:
            print("filename is:" + filename)
            print("the full name of the file is:" + os.path.join(parent, filename))  # 输出文件路径信息
            with open(os.path.join(parent, filename)) as logf:
                logfile = logf.read()
                for i in range(0, len(errstringslist)):
                    if errstringslist[i] in logfile:
                        print("This file contains the error string: " + errstringslist[i])
                        errfilelist.append(os.path.join(parent, filename)+"\n")
    messagebox.showinfo(title='ErrLogFile', message=(''.join(errfilelist)))

window = Tk()
window.title('LogFinder')
window.iconbitmap('py-blue-trans-out.ico')
form = Frame(window)
form.pack()
lab1 = Label(form, text='The path:')
ent1var = StringVar()
ent1 = Entry(form, textvariable=ent1var)
ent1var.set(" ")
lab1.grid(row=0, column=0)
ent1.grid(row=0, column=1)
lab2 = Label(window, text="Please, Enter the string you want to search,Delimited by whitespace:")
lab2.pack(side=TOP)
ent2var = StringVar()
ent2 = Entry(window, width=50, textvariable=ent2var)
ent2var.set(" ")
ent2.pack(side=TOP)
btn = Button(window, text='Find', command=errlogfind)
btn.pack(side=TOP)
window.mainloop()

