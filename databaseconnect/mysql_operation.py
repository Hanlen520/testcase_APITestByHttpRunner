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


# 获取数据库连接，配置数据库IP，端口等信息，获取数据库连接
class MySQLOperation:
    def __init__(self, config_file, database_name):

        with io.open(config_file, 'r', encoding='utf-8') as stream:
            yaml_content = yaml.load(stream)

            host = yaml_content[database_name]['host']
            port = yaml_content[database_name]['port']
            user = yaml_content[database_name]['user']
            password = yaml_content[database_name]['password']
            db_name = yaml_content[database_name]['db']
            charset = yaml_content[database_name]['charset']

        try:
            self.connection = pymysql.connect(host=host, port=port, user=user, password=password, database=db_name,
                                          charset=charset)
        except Exception as e:
            logging.error('初始化数据连接失败：%s' % e)

    # 返回数据库的一条记录
    def select_one_record(self, query, data=""):
        logging.info('query：%s  data：%s' % (query, data))

        with self.connection.cursor() as cursor:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            query_result = cursor.fetchone()

        return query_result

    def select_many_record(self, query, data=""):
        logging.info('query：%s  data：%s' % (query, data))

        with self.connection.cursor() as cursor:
            if data:
                numbers = cursor.execute(query, data)
            else:
                numbers = cursor.execute(query)
            query_result = cursor.fetchmany(numbers)

        return query_result

    def execute_insert(self, query, data=''):
        logging.info('query：%s  data：%s' % (query, data))
        with self.connection.cursor() as cursor:
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)

        # connection is not autocommit by default. So you must commit to save
        self.connection.commit()

    def close_connection(self):
        self.connection.close()





