# -*- coding: utf-8 -*-

import os, time

"""
The first python test script for Android
"""

def adb_act_caller(number1):
#os.system("adb shell am start -n com.android.contacts/.activities.DialtactsActivity \n")
    call = os.popen("adb shell am start -a android.intent.action.CALL -d tel:{}".format(number1))
    time.sleep(10)
def adb_hangup_caller():
    hangup = os.popen("adb shell input tap 450 1486")
    time.sleep(5)

if __name__ == "__main__":
    print("The first python test script for Android!")
    print("Start caller...")
    call_num = "18980988348"
    adb_act_caller(call_num)
    adb_hangup_caller()
