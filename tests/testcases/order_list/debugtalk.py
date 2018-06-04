#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     debugtalk.py
   Description :
   Author :        Meiyo
   date：          2018/6/4 20:54
-------------------------------------------------
   Change Activity:
                   2018/6/4:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import os
from databaseconnect.mysql_operation import *

base_url = os.environ.get('base_url')

mysql_single = MySQLOperation()


if base_url.__eq__('base_url=http://openapi.caibaopay.com//gateway.htm'):
    connection = mysql_single.get_connection('databaseconfig/database_product.yml', 'caibaotc')
else:
    connection = mysql_single.get_connection('databaseconfig/database_devlop.yml', 'caibaotc')

