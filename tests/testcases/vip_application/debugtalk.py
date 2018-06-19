#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     debugtalk.py
   Description :
   Author :        Meiyo
   date：          2018/6/19 14:50
-------------------------------------------------
   Change Activity:
                   2018/6/19:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

from databaseconnect.mysql_operation import *
import os
import time

base_url = os.environ.get('base_url')


def connect_database():
    global database_vip
    try:
        if base_url.__eq__('http://openapi.caibaopay.com//gateway.htm'):
            database_vip = MySQLOperation(os.getcwd() + '/databaseconfig/database_product.yml', 'caibaovip')
        else:
            database_vip = MySQLOperation(os.getcwd() + '/databaseconfig/database_devlop.yml', 'caibaovip')
    except Exception as ex:
        logging.error('连接数据库失败：%s', ex)


def close_connection():
    database_vip.close_connection()


# 获取会员vip_no的可用券列表的第一张券的券码
def get_first_coupon_code(vip_no):
    if not database_vip:
        return None

    query = ('SELECT coupon_code FROM caibaovip.vip_coupon where '
             'card_no = %s and status = %s and validity_stop_time >= %s')

    data = (vip_no, 'UNUSED', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    try:
        result = database_vip.select_many_record(query, data)

    except Exception as ex:
        print("执行数据库查询失败(get_coupon_code_by_vip_no) ", ex)
        logging.error("执行数据库查询失败(get_coupon_code_by_vip_no) ", ex)
        return None
    return result[0][0]

