# -*- coding: utf-8 -*-
from uiautomator import device as d
import os, time
"""
The second python test script for android
"""
def devinfo():
    phone = d.info
    return phone

def turnonscreen():
    d.screen.on()
    time.sleep(10)

def turnoffscreen():
    d.screen.off()

def opencaller():
    pass
def call(number1):
    call = os.popen("adb shell am start -a android.intent.action.CALL -d tel:{}".format(number1))
    time.sleep(30)

def hangup():
    hangup = os.popen("adb shell input tap 450 1486")
    time.sleep(5)

def acceptincall():
    pass

if __name__ == "__main__":
    print("print device info!")
    try:
        print(devinfo())
    except:
        print("Can't retrieve the device info!")
    call_num = "18683720168"
    print("turnonscreen!")
    turnonscreen()
    print("make a call!")
    call(call_num)
    print("hang up the call!")
    hangup()
    print("turnoffscreen!")
    turnoffscreen()


