import execjs
import requests
import json
import io

session = requests.session()

acounts = '******'
password = '*****'

def get_js():
    f = io.open("../js/RSA.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

def password_encry(password):
    global session
    pas = password[::-1]
    req = session.get('http://rpa.aliyun.net/rpa/user/sso/rsa/public/hex')
    data = req.json()['data']
    jsstr = get_js()
    ctx = execjs.compile(jsstr)
    return (ctx.call('returnPas', data['publicExp'], '', data['publicKey'], pas))

password =  password_encry(password)
data = {
    'userName': acounts,
    'password': password
}
req = session.post('http://rpa.aliyun.net/rpa/user/sso/login/hex', data=data)
print(req.json())

res = session.get('http://rpa.aliyun.net/rpa/user/baseinfo')
print(res.json())
