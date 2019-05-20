#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, jsonify, redirect, url_for

from sql import menu_list

app = Flask(__name__, static_url_path = '')

# 首页
@app.route('/' )
def home():
    return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    print(request.args.get('name'))
    return 'User %s' % username

if __name__ == '__main__':
    app.run(debug=True, port='8080', host='127.0.0.1')