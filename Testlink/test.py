# -*-coding:UTF-8-*-
from win32com.client import Dispatch
import win32com.client
from tkinter import *
import os, datetime, string

"""
auth:zhongqionglun
time:
description:
"""


def writeexcel():
    outfilename = "ratio_excuteing.xlsx"
    xlApp = win32com.client.Dispatch('Excel.Application')
    if os.path.exists("执行效率月统计结果.xlsx"):
        print("The file is exists....")
        # 判断shett是否存在，一个tester一个sheet#

    else:
        testers = ["huaiwei xiong", "qionglun zhong", "xiao han"]
        dic = {"huaiwei xiong": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                                 "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15, "16": 16,
                                 "17": 17, "18": 18, "19": 19, "20": 20, "21": 21, "22": 22, "23": 23,
                                 "24": 24, "25": 25, "26": 26, "27": 27, "28": 28, "29": 29, "30": 30, "31": 31},
               "qionglun zhong": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                                  "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15, "16": 16,
                                  "17": 17, "18": 18, "19": 19, "20": 20, "21": 21, "22": 22, "23": 23,
                                  "24": 24, "25": 25, "26": 26, "27": 27, "28": 28, "29": 29, "30": 30, "31": 30},
               "xiao han": {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                            "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15, "16": 16,
                            "17": 17, "18": 18, "19": 19, "20": 20, "21": 21, "22": 22, "23": 23,
                            "24": 24, "25": 25, "26": 26, "27": 27, "28": 28, "29": 29, "30": 30, "31": 29}
               }
        print(dic["huaiwei xiong"]["1"])
        print("The file isn't exists....")
        # 创建一个新文件
        xlBook = xlApp.Workbooks.Add()
        print(xlBook)
        xlBook.SaveAs(outfilename)
        # 默认Sheet1，修改sheet名
        print(xlBook.Sheets.Count)
        # xlBook.Sheets[0].Name = "huaiwei xiong"
        # print(xlBook.Sheets[0].Name)
        i = 0
        for tester in testers:
            print(tester)
            if i == 0:
                xlBook.Sheets[i].Name = tester
                sheet = xlBook.Worksheets(tester)
                for day in range(1, 32):
                    print(dic[tester][str(day)])
                    sheet.Cells(day, 1).Value = dic[tester][str(day)]
                i = i + 1
                print(i)
                continue
            else:
                newsheet = xlBook.Sheets.Add()
                newsheet.Name = tester
                for day in range(1, 32):
                    print(dic[tester][str(day)])
                    newsheet.Cells(day, 1).Value = dic[tester][str(day)]
                i = i + 1
                print(i)
                continue
        # 默认Sheet1,删除不了
        # xlBook.Sheets("Sheet1").Delete
        print(xlBook.Sheets.Count)
        xlBook.SaveAs()
        xlBook.Close(0)
        xlApp.quit()


if __name__ == '__main__':
    writeexcel()
