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

from databaseconnect.mysql_operation import *
import os

base_url = os.environ.get('base_url')
activateCode = os.environ.get('activateCode')


def connect_database():
    global database_tc
    try:
        if base_url.__eq__('http://openapi.caibaopay.com//gateway.htm'):
            database_tc = MySQLOperation(os.getcwd() + '/databaseconfig/database_product.yml', 'caibaotc')
        else:
            database_tc = MySQLOperation(os.getcwd() + '/databaseconfig/database_devlop.yml', 'caibaotc')
    except Exception as ex:
        logging.error('连接数据库失败：%s', ex)


def close_connection():
    database_tc.close_connection()


def get_order_detail_by_orderno(local_order_no):
    if not database_tc:
        return None

    query = 'SELECT * FROM caibaotc.tc_order_cp where viewer_id1 = %s and local_order_no = %s'
    data = (activateCode, local_order_no)
    try:
        result = database_tc.select_one_record(query, data)

    except Exception as ex:
        print("执行数据库查询失败(get_order_detail_by_orderno) ", ex)
        logging.error("执行数据库查询失败(get_order_detail_by_orderno) ", ex)
        return None
    return result


def get_order_list_by_datetime(begin, end):

    if not database_tc:
        return None

    query = ('SELECT * FROM caibaotc.tc_order_cp where viewer_id1 = %s and trade_time between %s and %s '
             'order by trade_time DESC')
    data = (activateCode, begin, end)
    try:
        result = database_tc.select_many_record(query, data)

    except Exception as ex:
        print("执行数据库查询失败(get_order_list_by_datetime) ", ex)
        logging.error("执行数据库查询失败(get_order_list_by_datetime) ", ex)
        return None

    return list(result)


def get_order_count_by_datetime(begin, end):

    if not database_tc:
        return None

    query = ('SELECT COUNT(*) FROM caibaotc.tc_order_cp where viewer_id1 = %s and trade_time between %s and %s')
    data = (activateCode, begin, end)
    try:
        result = database_tc.select_one_record(query, data)

    except Exception as ex:
        print("执行数据库查询失败(get_order_count_by_datetime) ", ex)
        logging.error("执行数据库查询失败(get_order_count_by_datetime) ", ex)
        return None

    return str(result[0])

# 获取外部交易号（非充值订单），根据不同的测试环境
def get_out_order_no():
    if base_url.__eq__('http://openapi.caibaopay.com//gateway.htm'):
        out_order_no = '4200000117201806122546412562'
    else:
        out_order_no = '4200000109201806124355210311'

    return out_order_no


# 获取本地订单号（充值订单），根据不同的测试环境
def get_recharge_order_no():
    if base_url.__eq__('http://openapi.caibaopay.com//gateway.htm'):
        recharge_order_no = 'TCCASH1806190622027509782855'
    else:
        recharge_order_no = 'TCCASH1806191050400752301432'

    return recharge_order_no

