#!/usr/bin/env python
# encoding: utf-8

"""
-------------------------------------------------
   File Name：     mysql_operation
   Description :
   Author :        Meiyo
   date：          2018/3/14 14:44
-------------------------------------------------
   Change Activity:
                   2018/3/14:
------------------------------------------------- 
"""
__author__ = 'Meiyo'

import pymysql
import yaml
import io
import logging
from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return get_instance


# 获取数据库连接，配置数据库IP，端口等信息，获取数据库连接
@singleton
class MySQLOperation:
    def __init__(self):
        self.connection = None

    def get_connection(self, config_file, db_name):
        with io.open(config_file, 'r', encoding='utf-8') as stream:
            yaml_content = yaml.load(stream)

            host = yaml_content[db_name]['host']
            port = yaml_content[db_name]['port']
            user = yaml_content[db_name]['user']
            password = yaml_content[db_name]['password']
            db_name = yaml_content[db_name]['db']
            charset = yaml_content[db_name]['charset']

        try:
            self.connection = pymysql.connect(host=host, port=port, user=user, password=password, database=db_name,
                                          charset=charset)
        except Exception as e:
            logging.error('初始化数据连接失败：%s' % e)

        return self.connection

    # 返回数据库的一条记录
    def select_one_record(self, query, data=""):
        logging.info('query：%s  data：%s' % (query, data))
        # db_cursor = self.connection.cursor()
        query_result = None
        # try:
        #     if data:
        #         db_cursor.execute(query, data)
        #     else:
        #         db_cursor.execute(query)
        #     query_result = db_cursor.fetchone()
        # except Exception as e:
        #     logging.error('执行数据库查询操作失败：%s' % e)
        # finally:
        #     db_cursor.close()
        # return query_result
        with self.connection as cursor:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            query_result = cursor.fetchone()
        return query_result

    def execute_insert(self, query, data=''):
        logging.info('query：%s  data：%s' % (query, data))
        with self.connection as cursor:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)

    def close_connection(self):
        self.connection.close()


if __name__ == '__main__':
    mysql_single1 = MySQLOperation()
    connection1 = mysql_single1.get_connection('dbconfig.yml', 'caibaotc')
    query1 = "SELECT * FROM caibaotc.tc_order where viewer_id1 = 'A00300100000035' and local_order_no = 'TCAP1704270948504427757832'"
    result1 = mysql_single1.select_one_record(query1)
    mysql_single1.close_connection()

    print(result1)

    mysql_single2 = MySQLOperation()
    connection2 = mysql_single2.get_connection('dbconfig.yml', 'zypPlatformTest')
    query2 = "SELECT * FROM zypPlatformTest.zyp_merchant where user_code = 'A00300100000035'"
    result2 = mysql_single2.select_one_record(query2)
    mysql_single2.close_connection()
    print(result2)





