import datetime
import shutil
import smtplib
from email.mime.text import MIMEText

from apscheduler.schedulers.background import BackgroundScheduler
from FlaskAPI.ext import db
from Client_API.models import UsermsgModel

users = ["1776383685@qq.com","s1776383685@163.com"]

# scheduler = BackgroundScheduler()
# scheduler.add_job(mail, 'date',
#                   run_date=datetime.strptime("2020-01-05 17:50:50", "%Y-%m-%d %H:%M:%S"),
#                   args=users, id="sendemail")
# scheduler.start()
# users = db.session.query.(UsermsgModel)
my_sender = 'houfuguo@sinosoft.com.cn'  # 发件人邮箱账号
my_pass = '5CXdf4DDy8Xw68p4'  # 发件人邮箱的授权码
def mail(my_user):
    ret= True
    try:
        ms_0 = """本次活动报名时限将至，为避免您错过精彩活动，请尽快填报活动报名信息。谢谢！
不论您来与不来，金融渠道分群都在等您。"""
        msg = MIMEText(ms_0, 'plain', 'utf-8')
        msg['From'] = my_sender # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = my_user[0] # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "金融渠道分群年会欢迎您参加！" # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465) # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_user, msg.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的ret=False
        print(e)
        ret = False
    return ret

# mail(users)


# a ={"w":121}
# b = a["q"]

# shutil.rmtree(r"D:\code\new_year\FlaskAPI\static\out_file\18")




# import ssl
# import random
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# import redis
# import requests
# # proxies ="http://proxy.piccnet.com.cn"
# # from FlaskAPI.ext import cache
# my_sender = 'houfuguo@sinosoft.com.cn'  # 发件人邮箱账号
# my_pass = '5CXdf4DDy8Xw68p4'  # 发件人邮箱的授权码
# my_user = '1776383685@qq.com'  # 收件人邮箱账号，我这边发送给自己
# def mail(my_user):
#     ret= True
#     try:
#         sercert_code = 2231
#         # sercert_code = '2231'
#         msg = MIMEText('验证码为：%s'% sercert_code, 'plain', 'utf-8')
#         msg['From'] = my_sender # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To'] = my_user # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject'] = "验证码" # 邮件的主题，也可以说是标题
#         server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465) # 发件人邮箱中的SMTP服务器，端口是25
#         server.login(my_sender, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender, my_user, msg.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         # cache.set(my_user, sercert_code)
#         server.quit()  # 关闭连接
#     except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的ret=False
#         print(e)
#         ret = False
#     return ret
# # mail(my_user)
#
# r = redis.StrictRedis(host="39.107.232.24", port=6379, db=3,password="pwd123456")
# a = "oYvjj5PFCVqyAKrk6D1bnKRRH3O0"
#
# print((r.get(a)).decode())

# print(12315646)
#
# print("wwe123")
#
# print(7845645)
a = datetime.datetime.now()
print(str(a)[:-7])