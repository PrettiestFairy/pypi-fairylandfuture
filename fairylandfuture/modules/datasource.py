# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-12 23:11:45 UTC+8
"""

from typing import Union, Tuple, Dict, List, Any

import pymysql


class MySQLDataSource:
    def __init__(self, host, port, user, password, db):
        self._connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        self._cursor = self._connection.cursor()

    def insert(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.connection.commit()

    def delete(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.connection.commit()

    def update(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.connection.commit()

    def select(self, sql, params=None):
        self.cursor.execute(sql, params)
        result = self.cursor.fetchall()
        if len(result) == 1:
            return result[0]
        return result

    def batch_insert(self, sql, param_list):
        self.cursor.executemany(sql, param_list)
        self.connection.commit()

    def execute_multiple_statements(self, statements):
        try:
            for statement in statements:
                self.cursor.execute(statement['sql'], statement.get('params'))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e

    def execute_no_return(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
