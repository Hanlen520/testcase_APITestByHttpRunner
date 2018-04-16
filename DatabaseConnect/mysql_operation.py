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
import sys


# 获取数据库连接，配置数据库IP，端口等信息，获取数据库连接
class MySQLOperation:
    def __init__(self, config_file, db_name):
        with io.open(config_file, 'r', encoding='utf-8') as stream:
            yaml_content = yaml.load(stream)

            host = yaml_content[db_name]['host']
            port = yaml_content[db_name]['port']
            user = yaml_content[db_name]['user']
            password = yaml_content[db_name]['password']
            db_name = yaml_content[db_name]['db']
            charset = yaml_content[db_name]['charset']

        try:
            self.dbconn = pymysql.connect(host=host, port=port, user=user, password=password, database=db_name,
                                          charset=charset)
        except Exception as e:
            logging.error('初始化数据连接失败：%s' % e)
            sys.exit()

    # 返回数据库的一条记录
    def select_one_record(self, query, data=""):
        logging.info('query：%s  data：%s' % (query, data))
        db_cursor = self.dbconn.cursor()
        query_result = None
        try:
            if data:
                db_cursor.execute(query, data)
            else:
                db_cursor.execute(query)
            query_result = db_cursor.fetchone()
        except Exception as e:
            logging.error('执行数据库查询操作失败：%s' % e)
        finally:
            db_cursor.close()
            return query_result

    def execute_insert(self, query, data=''):
        logging.info('query：%s  data：%s' % (query, data))
        with self.dbconn as cursor:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
        cursor.close()

    def close_dbconn(self):
        self.dbconn.close()


if __name__ == '__main__':
    mysql_connect = MySQLOperation('dbconfig.yml', 'caibaotc')
    query = "SELECT * FROM caibaotc.tc_order order by gmt_create DESC limit 10"
    result = mysql_connect.select_one_record(query)
    mysql_connect.close_dbconn()
    print(result)

