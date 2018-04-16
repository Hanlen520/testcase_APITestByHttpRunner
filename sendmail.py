#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     sendmail
   Description :
   Author :        Meiyo
   date：          2018/1/11 15:45
-------------------------------------------------
   Change Activity:
                   2018/1/11: Create the file
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import logging
import io


def load_env_file(path):
    """ load .env file and set to os.environ
    """
    if not os.path.isfile(path):
        return

    with io.open(path, 'r', encoding='utf-8') as fp:
        for line in fp:
            variable, value = line.strip('\n').split("=")
            os.environ[variable] = value


def get_attach_path():
    folder_path = os.path.join(os.getcwd(), 'reports')
    file_path = ''

    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        for filename in filenames:
            if not filename.endswith('.html'):
                continue
            file_path = os.path.join(dirpath, filename)

    return file_path


def get_email_content():
    content = ''

    file_path = get_attach_path()
    if not file_path:
        print('Not find the attach!')

    with open(file_path, 'rb') as report_file:
        content = report_file.read()

    return content


def get_email_msg():
    html_content = get_email_content()

    msg = MIMEMultipart('mixed')
    content = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(content)

    attach = MIMEText(html_content, 'html', 'utf-8')
    attach["Content-Type"] = 'application/octet-stream'
    attach["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(attach)

    msg['From'] = from_addr
    msg['To'] = to_email
    msg['Subject'] = Header(u'PC收银台接口测试报告', 'utf-8').encode()

    return msg


def send_email(stmp, from_addr, from_password, to_email):
    try:
        email_msg = get_email_msg()
        server = smtplib.SMTP(host=stmp, port=25, timeout=30)
        server.login(from_addr, from_password)
        # server.set_debuglevel(1)
        server.sendmail(from_addr, to_email, email_msg.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        print('error', e)


if __name__ == '__main__':
    if not os.environ.get('stmp'):
        env_path = os.path.join(os.getcwd(), "email.env")
        if env_path:
            load_env_file(env_path)
        else:
            logging.error('email.env is not found!')

    from_addr = os.environ.get('from_addr')
    from_password = os.environ.get('from_password')
    to_email = os.environ.get('to_email')
    stmp = os.environ.get('stmp')

    if from_addr and from_password and to_email and stmp:
        send_email(stmp, from_addr, from_password, to_email)
    else:
        logging.error('some params is error!')

