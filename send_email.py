#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class ErrorLogAlert:
    def check_log(self):
        pass

    def send_email(self):
        mail_host="smtp.qq.com"           # 设置服务器
        mail_user="*****@qq.com"     # 用户名
        mail_pass="ebevmrxtzfbybfdi"           # 口令(qq邮箱非密码)

        sender = '*****@qq.com'
        receivers = '*****@icloud.com'   # 接收邮箱，可设置为你的QQ邮箱或者其他邮箱

        message = MIMEText('这是邮件内容，假装这里有点东西', 'plain', 'utf-8')    # 邮件正文内容
        message['From'] = '*****@qq.com' # 最好是邮箱地址
        message['To'] = '*****@icloud.com' # 最好是邮箱地址
        message['Subject'] = '邮件标题'

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host)
            smtpObj.connect(mail_host, 465)        # 25 为 SMTP 端口号  qq 465 587
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
            
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
            print(e)
        
        
notice = ErrorLogAlert()
notice.send_email()