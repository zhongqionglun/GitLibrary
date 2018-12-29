# -*- coding: utf-8 -*-
"""
CaaesOprator
1、for thanslate cases
2、for import cases to Testlink
"""

import os, sys
from win32com.client import Dispatch

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
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.iconbitmap("py-blue-trans-out.ico")
        self.master.title('CasesOprator')
        self.master.geometry('650x500')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.062, rely=0.071, relwidth=0.887, relheight=0.876)

        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        self.TabStrip1__Tab1.pack()
        self.TabStrip1__Tab1Lbl = Label(self.TabStrip1__Tab1, text=u"请输入excel文件名：")
        ent1var = StringVar()
        self.TabStrip1_Tab1eEnt1 = Entry(self.TabStrip1__Tab1, width=50, textvariable=ent1var)
        ent1var.set(" ")
        self.TabStrip1__Tab1Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1__Tab1Lbl.grid(row=0, column=0)
        self.TabStrip1_Tab1eEnt1.grid(row=1, column=0)
        self.TabStrip1__Tab1Lb2 = Label(self.TabStrip1__Tab1, text=u"请输入sheet文件名，多个sheet以空格分隔：")
        ent2var = StringVar()
        self.TabStrip1__Tab1Ent2 = Entry(self.TabStrip1__Tab1, width=90, textvariable=ent2var)
        ent2var.set(" ")
        self.TabStrip1__Tab1Lb2.place(relx=0.1, rely=0.5)
        self.TabStrip1__Tab1Lb2.grid(row=3, column=0)
        self.TabStrip1__Tab1Ent2.grid(row=4, column=0)
        self.TabStrip1__Tab1Btn = Button(self.TabStrip1__Tab1, text='转换', command=CasesOprator.easy_excel)
        self.TabStrip1__Tab1Btn.grid(row=6, column=0)
        self.TabStrip1.add(self.TabStrip1__Tab1, text='用例转换')

        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        self.TabStrip1__Tab2Lbl = Label(self.TabStrip1__Tab2, text='Please add widgets in code.')
        self.TabStrip1__Tab2Lbl.place(relx=0.1, rely=0.5)
        self.TabStrip1.add(self.TabStrip1__Tab2, text='用例导入')


class CasesOprator(CasesOprator_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        CasesOprator_ui.__init__(self, master)

    def easy_excel(self):
        pass


if __name__ == "__main__":
    window = Tk()
    CasesOprator(window).mainloop()
