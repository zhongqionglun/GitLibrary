# -*- coding: utf-8 -*-

from uiautomator import device as d
import os,time

"""
The fourth python test script for android
"""

# -*- coding: utf-8 -*-
from uiautomator import device as d
import os,time

"""
The third python test script for android
"""

def waite_accept_call():
    times = 60
    while True:
        if times == 0:
            break
        else:
            if d(className = "android.view.View", resourceId = "com.android.incallui:id/glow_pad_view").exists:
                print("selector find match!")
                # result = d(className="android.view.View", resourceId="com.android.incallui:id/glow_pad_view").swipe("right",steps=100,percent=33)
                result = d.swipe(540,1520,910,1520)
                print(result)
                break
            else:
                times -= 1
                print("times is %s",times)
                time.sleep(1)
                continue

def play_music():
    try:
        d(text=u"音乐",className="android.widget.TextView").click()
        time.sleep(5)
        d(className="android.widget.ImageView", resourceId = "com.android.mediacenter:id/song_play").click()
    except:
        print("UiObject not found")

    time.sleep(30)

def devinfo():
    phone = d.info
    return phone

def turnonscreen():
    d.screen.on()
    time.sleep(10)

def turnoffscreen():
    d.screen.off()

def hangup():
    hangup = os.popen("adb shell input tap 450 1486")
    time.sleep(10)

if __name__ == "__main__":
    # print("print device info!")
    # try:
    #     print(devinfo())
    # except:
    #     print("Can't retrieve the device info!")
    # print("turnonscreen!")
    # turnonscreen()
    # print("waite imcoming call...")
    # waite_accept_call()
    # time.sleep(5)
    print("turnonscreen!")
    turnonscreen()
    if d(className="android.widget.ImageView", resourceId="com.android.systemui:id/mask_bottom").exists:
        d.swipe(540,1792,540,1181)
    print("play a music!")
    play_music()
    print("turnonscreen!")
    turnonscreen()
    # print("hang up the call!")
    # hangup()
    # print("turnoffscreen!")
    # turnoffscreen()
