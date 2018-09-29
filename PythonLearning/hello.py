#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zhongqionglun
# datetime:2018/08/08 19:49

'''
功能：搭建一个简单的web服务器，用于测试flask web开发验证例子
'''

from flask import Flask,request,render_template
import datetime


app = Flask(__name__)

now = datetime.datetime.now()

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name,now=now)

if __name__ == '__main__':
    app.run(host='172.29.1.88',port='8080')
