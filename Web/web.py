#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, jsonify

from sql import menu_list

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('page_home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('signin_form.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)

    return '<h3>Bad username or password.</h3>'

@app.route('/api/list', methods=['POST'])
def list():
    name=request.form['name']
    age=request.form['age']
    res = menu_list()
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, port='8080', host='127.0.0.1')