# -*- coding: utf-8 -*-
"""
CaaesOprator
1、for thanslate cases
2、for import cases to Testlink
"""

import os, sys
from easy_excel import *

if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    # Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    # Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    # import tkFileDialog
    # import tkSimpleDialog
else:  # Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    # import tkinter.filedialog as tkFileDialog
    # import tkinter.simpledialog as tkSimpleDialog    #askstring()
import win32com.client


class CasesOprator_ui(Frame):
    # 这个类实现界面生成，事件处理。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.iconbitmap("py-blue-trans-out.ico")
        self.master.title('CasesOprator')
        self.master.geometry('556x390')
        self.createWidgets()


    def createWidgets(self):
        self.top = self.winfo_toplevel()
        self.style = Style()
        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.062, rely=0.071, relwidth=0.888, relheight=0.876)

        self.TabStrip1_Tab1 = Frame(self.TabStrip1)
        self.TabStrip1_Tab1.pack()
        self.TabStrip1_Tab1Lbl = Label(self.TabStrip1_Tab1, text=u"请输入excel文件名：")
        self.filename = StringVar()
        self.TabStrip1_Tab1Ent1 = Entry(self.TabStrip1_Tab1, width=50, textvariable=self.filename)
        self.filename.set(" ")
        self.TabStrip1_Tab1Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1_Tab1Ent1.place(relx=0.1, rely=0.5)
        self.TabStrip1_Tab1Lbl.grid(row=0, column=0)
        self.TabStrip1_Tab1Ent1.grid(row=1, column=0)
        self.TabStrip1_Tab1Ent1.focus()  # save a click
        self.TabStrip1_Tab1Ent1.bind('<Return>', (lambda event: self.fetch(self.TabStrip1_Tab1Ent1)))
        self.TabStrip1_Tab1Lb2 = Label(self.TabStrip1_Tab1, text=u"请输入sheet文件名，多个sheet以空格分隔：")
        self.sheetname = StringVar()
        self.TabStrip1_Tab1Ent2 = Entry(self.TabStrip1_Tab1, width=69, textvariable=self.sheetname)
        self.sheetname.set(" ")
        self.TabStrip1_Tab1Lb2.place(relx=0.1, rely=0.5)
        self.TabStrip1_Tab1Lb2.grid(row=3, column=0)
        self.TabStrip1_Tab1Ent2.grid(row=5, column=0)
        self.TabStrip1_Tab1Ent2.focus()  # save a click
        self.TabStrip1_Tab1Ent2.bind('<Return>', (lambda event: self.fetch(self.TabStrip1_Tab1Ent2)))
        self.TabStrip1_Tab1Btn = Button(self.TabStrip1_Tab1, text='转换', command=self.EasyExcel)
        self.TabStrip1_Tab1Btn.grid(row=6, column=0)
        self.TabStrip1.add(self.TabStrip1_Tab1, text='用例转换')

        self.TabStrip1__Tab3 = Frame(self.TabStrip1)
        self.TabStrip1__Tab3Lbl = Label(self.TabStrip1__Tab3, text=u"项目：")
        self.TabStrip1__Tab3Lbl.place(relx=0.1, rely=0.5)
        ent3var = StringVar()
        self.TabStrip1__Tab3Ent1 = Entry(self.TabStrip1__Tab3, width=50, textvariable=ent3var)
        ent3var.set("")
        self.TabStrip1__Tab3Ent1.place(relx=0.1, rely=0.5)
        self.TabStrip1__Tab3Lbl.grid(row=0, column=0)
        self.TabStrip1__Tab3Ent1.grid(row=0, column=1)
        self.TabStrip1__Tab3Lb2 = Label(self.TabStrip1__Tab3, text=u"测试计划：")
        self.TabStrip1__Tab3Lb2.place(relx=0.1, rely=0.5)
        ent4var = StringVar()
        self.TabStrip1__Tab3Ent2 = Entry(self.TabStrip1__Tab3, width=50, textvariable=ent4var)
        ent4var.set("")
        self.TabStrip1__Tab3Ent2.place(relx=0.1, rely=0.5)
        self.TabStrip1__Tab3Lb2.grid(row=1, column=0)
        self.TabStrip1__Tab3Ent2.grid(row=1, column=1)
        self.TabStrip1__Tab3Lb3 = Label(self.TabStrip1__Tab3, text=u"测试套：")
        self.TabStrip1__Tab3Lb3.place(relx=0.1, rely=0.5)
        ent5var = StringVar()
        self.TabStrip1__Tab3Ent3 = Entry(self.TabStrip1__Tab3, width=50, textvariable=ent5var)
        ent5var.set("")
        self.TabStrip1__Tab3Ent3.place(relx=0.1, rely=0.5)
        self.TabStrip1__Tab3Lb3.grid(row=2, column=0)
        self.TabStrip1__Tab3Ent3.grid(row=2, column=1)
        self.TabStrip1__Tab3Btn = Button(self.TabStrip1__Tab3, text='导入', command=sys.exit)
        self.TabStrip1__Tab3Btn.grid(row=6, column=0)
        self.TabStrip1.add(self.TabStrip1__Tab3, text='用例导入')

    def fetch(self, ent):
        print('Input => "%s"' % ent.get())

    def EasyExcel(self):
        filename = self.filename.get()
        sheetList = self.sheetname.get().split(" ")
        for sheetname in sheetList:
            test = operate(filename, sheetname)
            test.xlsx_to_dic(sheetname)
            test.dic_to_xml(filename, sheetname)
        print("Convert success!")

    def ImportCases(self):
        pass


if __name__ == "__main__":
    window = Tk()
    CasesOprator_ui(window).mainloop()
