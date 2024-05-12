# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-12 23:11:45 UTC+8
"""

import pymysql


class MySQLDataSource:

    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = self.connect()
        self.cur = self.conn.cursor()

    def connect(self):
        conn = pymysql.connect(
            host=self.host, port=self.port, user=self.user, password=self.password, database=self.database
        )
        return conn

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def execute(self, query, params):
        return self.cur.execute(query, params)

    def create(self, sql, params):
        try:
            self.execute(sql, params)
            self.close()
            return True
        except Exception as err:
            raise err

    def delete(self, sql, params):
        try:
            self.execute(sql, params)
            self.close()
            return True
        except Exception as err:
            raise err

    def select(self, sql, params):
        try:
            results = self.execute(sql, params)
            self.close()
            return results
        except Exception as err:
            raise err

    def update(self, sql, params):
        try:
            self.execute(sql, params)
            self.close()
            return True
        except Exception as err:
            raise err
