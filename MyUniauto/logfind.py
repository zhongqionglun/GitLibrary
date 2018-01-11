import os
rootdir = 'D:\data'
errstringslist = ["reboot", "error"]
errfilelist = []
for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:
        print("filename is:" + filename)
        print("the full name of the file is:" + os.path.join(parent, filename))  # 输出文件路径信息
        with open(os.path.join(parent, filename)) as logf:
            logfile = logf.read()
            for i in range(0, len(errstringslist)):
                if errstringslist[i] in logfile:
                    print("This file contains the error string: " + errstringslist[i])
                    errfilelist.append(os.path.join(parent, filename))
print("__________________*************_______________")
for i in range(0, len(errfilelist)):
    print(errfilelist[i])

