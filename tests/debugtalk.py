# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :       Meiyo
   date：          2018/2/11
-------------------------------------------------
   Change Activity:
                   2018/2/11:
-------------------------------------------------
"""
__author__ = 'Meiyo'

import os

activateCode = os.environ.get('activateCode')
userCode = os.environ.get('userCode')
userPwd = os.environ.get('userPwd')
vipTelephone = os.environ.get('vipTelephone')
base_url = os.environ.get('base_url')

default_request = {
    "base_url": base_url,
    "headers": {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36",
        "OEM": "caibao"
    }

}




