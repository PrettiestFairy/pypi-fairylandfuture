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
from pymysql.cursors import DictCursor

from fairylandfuture.constants.typed import SQLStructList
from fairylandfuture.models.dataclasses.datasource import SQLStruct


class MySQLDataSource:
    def __init__(self, host, port, user, password, database):
        self._connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            cursorclass=DictCursor
        )
        self._cursor = self._connection.cursor()

    def insert(self, sql, params=None):
        try:
            self._cursor.execute(sql, params)
            self._connection.commit()
        except Exception as err:
            self._connection.rollback()
            raise err

    def delete(self, sql, params=None):
        try:
            self._cursor.execute(sql, params)
            self._connection.commit()
        except Exception as err:
            self._connection.rollback()
            raise err

    def update(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.connection.commit()
        try:
            self._cursor.execute(sql, params)
            self._connection.commit()
        except Exception as err:
            self._connection.rollback()
            raise err

    def select(self, sql, params=None):
        try:
            self._cursor.execute(sql, params)
            result = self._cursor.fetchall()
            if len(result) == 1:
                return result.__getitem__(0)
            return result
        except Exception as err:
            raise err

    def batch_insert(self, sql, param_list):
        try:
            self._cursor.executemany(sql, param_list)
            self._connection.commit()
        except Exception as err:
            self._connection.rollback()
            raise err

    def multiple_execute(self, multi: SQLStructList):
        try:
            for sql_struct in multi:
                self._cursor.execute(sql_struct.get("sql"), sql_struct.get("params"))
            self.connection.commit()
        except Exception as err:
            self.connection.rollback()
            raise err

    def execute(self, sql, params=None):
        try:
            self._cursor.execute(sql, params)
            self._connection.commit()
            return None
        except Exception as err:
            self._connection.rollback()
            raise err

    def __del__(self):
        self._cursor.close()
        self._connection.close()
