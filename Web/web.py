#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, jsonify, redirect, url_for

from sql import menu_list

app = Flask(__name__, static_url_path = '')

array = [
    {'name': 'Lucy', 'age': 20.2},
    {'name': 'Lucas', 'age': 18.5}
]
#实现一个可以求长度的函数
def strLen(arg):
    return len(arg)

env = app.jinja_env
env.filters['strLen'] = strLen

# 首页
@app.route('/', methods=['GET'])
def home():
    # return render_template('page_home.html')
    return render_template('index.html')

@app.route('/signin2')
def signin_form():
    return render_template(
        'signin_form.html',
        title='jinja2测试', 
        people=array
    )

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)

    return '<h3>Bad username or password.</h3>'

@app.route('/api/list', methods=['GET'])
def list():
    # name=request.form['name']
    # age=request.form['age']
    res = menu_list()
    return jsonify(res)

@app.errorhandler(404)
def page_error(error):
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port='8080', host='127.0.0.1')
