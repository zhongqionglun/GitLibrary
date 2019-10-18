#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:
# datetime:2018/07/09 19:49

'''
功能：搭建一个简单的web服务器，用于测试uc的事件上报功能，web服务器负责接收上传的事件信息，并将信息存储到
        文件中以方便查看，同时可以在web动态查看接收到的上传信息
'''

from flask import Flask,request,abort
import datetime


app = Flask(__name__)


def check_event(event):
    event_list = {
        "startup":"startup",
        "callstatus":"callstatus",
        "sip":"sip",
        "siptrunk":"siptrunk",
        "fxs":"fxs",
        "fxo":"fxo",
        "gsm":"gsm",
        "volte":"volte",
        "vpn":"vpn",
        "cdr":"cdr",
    }
    if event in event_list:
        return True
    else:
        return False


@app.route('/')
def index():
    return "<h1>Hello UC !</h1>"


@app.route('/<event>')
def Startup_event(event):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在事件
    if check_event(event):
        # print(request.url)
        # 接收到的url信息存储到log
        with open("./"+ event + ".log","a") as f:
            f.write(nowTime +" : "+ request.url + "\n")
            f.close()
    elif "favicon.ico" == event:
        # 无关事件
        pass
    else:
        # 错误URL日志
        with open("./Error.log", "a") as f:
            f.write(nowTime +" : "+ "ERROR URL :" + request.url + "\n")
            f.close()
    return "<h1>Event : %s</h1>" % event


if __name__ == '__main__':
    app.run(host='172.28.1.50', port="8080", debug=True)
