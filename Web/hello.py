#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
作者:zhongqionglun
时间:2018/08/08 19:49
功能：搭建一个简单的web服务器，用于测试flask web开发验证例子
'''

from flask import Flask, request, render_template, session, url_for, redirect,flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import data_required


import datetime


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'dinstarcd'
now = datetime.datetime.now()


# 定义一个表单
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[data_required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    # 页面submit提交后
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('The username is not same as last entered!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name,now=now)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
