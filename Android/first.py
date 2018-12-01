# -*- coding: utf-8 -*-

import os, time

"""
The first python test script for Android
"""

def adb_act_camera():
    os.system("adb shell am start -n com.android.contacts/.activities.DialtactsActivity \n")


if __name__ == "__main__":
    print("The first python test script for Android!")
    print("Start camera...")
    adb_act_camera()