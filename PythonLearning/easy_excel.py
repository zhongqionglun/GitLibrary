# coding=utf-8

from win32com.client import Dispatch
import win32com.client
import os

class easy_excel:
    def __init__(self, filename=None):
        self.xlApp = win32com.client.Dispatch('Excel.Application')

        if filename:
            self.filename = os.getcwd() + "\\" + filename
            # self.xlApp.Visible=True
            self.xlBook = self.xlApp.Workbooks.Open(self.filename)
        else:
            # self.xlApp.Visible=True
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ''

    def save(self, newfilename=None):
        if newfilename:
            self.filename = os.getcwd() + "\\" + newfilename
            # if os.path.exists(self.filename):
            # os.remove(self.filename)
            self.xlBook.SaveAs(self.filename)
        else:
            self.xlBook.Save()

    def close(self):
        self.xlBook.Close(SaveChanges=0)
        self.xlApp.Quit()

    def getCell(self, sheet, row, col):
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row, col).Value

    def setCell(self, sheet, row, col, value):
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Value = value
        # 设置居中
        sht.Cells(row, col).HorizontalAlignment = 3
        sht.Rows(row).WrapText = True

    # def mergeCells(self, sheet, row1, col1, row2, col2):
    #     start_coloum = int(dic_config["start_coloum"])
    #     # 如果这列不存在就不合并单元格
    #     if col2 != start_coloum - 1:
    #         sht = self.xlBook.Worksheets(sheet)
    #         sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Merge()
    #         # else:
    #         # print 'Merge cells coloum %s failed!' %col2

    def setBorder(self, sheet, row, col):
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row, col).Borders.LineStyle = 1

    def set_col_width(self, sheet, start, end, length):
        start += 96
        end += 96
        msg = chr(start) + ":" + chr(end)
        # print msg
        sht = self.xlBook.Worksheets(sheet)
        sht.Columns(msg.upper()).ColumnWidth = length


class operate():
    def __init__(self, ExcelFileName, SheetName):
        self.excelFile = ExcelFileName + '.xlsx'
        self.excelSheet = SheetName
        self.temp = easy_excel(self.excelFile)
        self.dic_testlink = {}
        self.row_flag = 2
        self.testsuite = SheetName
        self.dic_testlink[self.testsuite] = {"node_order": "13", "details": "", "testcase": []}
        self.content = ""
        self.content_list = []

    def xlsx_to_dic(self, SheetName):
        while True:
            # print 'loop1'
            # list_testcase = dic_testlink[testsuite].["testcase"]
            testcase = {"casename": "", "node_order": "1", "externalid": "", "version": "1", "summary": "",
                        "preconditions": "", "execution_type": "1", "importance": "1", "stepactions":"","expectedresults":"", "steps":[],"keywords":""}
            testcase["casename"] = self.temp.getCell(self.excelSheet, self.row_flag, 1)
            # print(testcase["casename"])
            testcase["keywords"] = self.temp.getCell(self.excelSheet, self.row_flag, 4)
            # print(testcase["keywords"])
            testcase["summary"] = self.temp.getCell(self.excelSheet, self.row_flag, 5)
            testcase["preconditions"] = self.temp.getCell(self.excelSheet, self.row_flag, 6)
            # print(testcase["preconditions"])
            testcase["stepactions"] = self.temp.getCell(self.excelSheet,self.row_flag, 7)
            # print(testcase["stepactions"])
            testcase["expectedresults"] = self.temp.getCell(self.excelSheet, self.row_flag, 8)
            # print(testcase["expectedresults"])
            execution_type = self.temp.getCell(self.excelSheet, self.row_flag, 9)
            if execution_type == "自动":
                testcase["execution_type"] = 2
            actions = testcase["stepactions"].split('\n')
            results = testcase["expectedresults"].split('\n')
            # print(results)
            step_number = 1
            for actstring in actions:
                step = {"step_number": "", "actions": "", "expectedresults": "", "execution_type": "1"}
                step["step_number"] = step_number
                print(step["step_number"])
                step["actions"] = actstring[2:]
                print(step["actions"])
                if step_number <= len(results):
                    tempstring = results[step_number-1]
                    step["expectedresults"] = tempstring[2:]
                else:
                    step["expectedresults"] = ""
                testcase["steps"].append(step)
                print(testcase["steps"])
                step_number += 1
            self.row_flag += 1
            # print self.row_flag
            self.dic_testlink[self.testsuite]["testcase"].append(testcase)
            if self.temp.getCell(self.excelSheet, self.row_flag, 7) is None and self.temp.getCell(self.excelSheet, self.row_flag + 1, 7) is None:
                # print(self.dic_testlink)
                break
        self.temp.close()
        # print self.dic_testlink

    def content_to_xml(self, key, value=None):
        if key == 'step_number' or key == 'execution_type' or key == 'node_order' or key == 'externalid' or key == 'version' or key == 'importance':
            return "<" + key + "><![CDATA[" + str(value) + "]]></" + key + ">"
        elif key == 'actions' or key == 'expectedresults' or key == 'summary' or key == 'preconditions':
            return "<" + key + "><![CDATA[<p> " + str(value) + "</p> ]]></" + key + ">"
        elif key == 'keywords':
            return '<keywords><keyword name="' + str(value) + '"><notes><![CDATA[ aaaa ]]></notes></keyword></keywords>'
        elif key == 'name':
            return '<testcase name="' + str(value) + '">'
        else:
            return ''

    def dic_to_xml(self, ExcelFileName, SheetName):
        testcase_list = self.dic_testlink[self.testsuite]["testcase"]
        for testcase in testcase_list:
            for step in testcase["steps"]:
                self.content += "<step>"
                self.content += self.content_to_xml("step_number", step["step_number"])
                self.content += self.content_to_xml("actions", step["actions"] )
                self.content += self.content_to_xml("expectedresults", step["expectedresults"] )
                self.content += self.content_to_xml("execution_type", step["execution_type"] )
                self.content += "</step>"
            self.content = "<steps>" + self.content + "</steps>"
            self.content = self.content_to_xml("importance", testcase["importance"] ) + self.content
            self.content = self.content_to_xml("execution_type", testcase["execution_type"]) + self.content
            self.content = self.content_to_xml("preconditions", testcase["preconditions"]) + self.content
            self.content = self.content_to_xml("summary", testcase["summary"]) + self.content
            self.content = self.content_to_xml("version", testcase["version"]) + self.content
            self.content = self.content_to_xml("externalid", testcase["externalid"]) + self.content
            self.content = self.content_to_xml("node_order", testcase["node_order"]) + self.content
            self.content = self.content + self.content_to_xml("keywords", testcase["keywords"])
            self.content = self.content_to_xml("name", testcase["casename"]) + self.content
            self.content = self.content + "</testcase>"
            self.content_list.append(self.content)
            self.content = ""
        self.content = "".join(self.content_list)
        self.content = '<testsuite name="' + self.testsuite + '">' + self.content + "</testsuite>"
        self.content = '<?xml version="1.0" encoding="UTF-8"?>' + self.content
        self.write_to_file(ExcelFileName, SheetName)

    def write_to_file(self, ExcelFileName, SheetName):
        xmlFileName = ExcelFileName + '_' + SheetName + '.xml'
        cp = open(xmlFileName, "w")
        cp.write(self.content)
        cp.close()

if __name__ == "__main__":

    fileName = input('enter excel name:')
    sheetName = input('enter sheet name:')
    sheetList = sheetName.split(" ")
    for sheetName in sheetList:
        test = operate(fileName, sheetName)
        test.xlsx_to_dic(sheetName)
        test.dic_to_xml(fileName, sheetName)
    print("Convert success!")

