# -*-coding:UTF-8-*-

from openpyxl import Workbook, load_workbook, styles

import datetime

# Create workbook
wb = Workbook()
# grab active worksheet
ws = wb.active
ws.sheet_properties.tabColor = "ff0000"
# Data can be assigned directly cells
ws['A1'] = 10
ws['B1'] = 20
ws['C1'] = 30
styles.Color()
# Rows can also be
for row in range(1, 40):
	ws.append(range(600))
# Python types will automatically be converted
ws['A2'] = datetime.datetime.now()
# save the file
ws1 = wb.create_sheet()
ws1.title = "secondsheet"
ws1.cell(row=1, column=1, value="Passed")
ws1.cell(row=2, column=1, value="Failed")
# for sheet in wb:
# 	print(wb.sheetnames)
wb.save("test.xlsx")

Workbook1 = load_workbook('test.xlsx')
print(Workbook1.sheetnames)
worksheet1 = Workbook1.sheetnames[0]
print (worksheet1)
sheet1 = Workbook1.get_sheet_by_name(worksheet1)
print(sheet1.cell(row=1, column=2).value)
