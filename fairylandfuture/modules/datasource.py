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

    def execute(
        self,
        sql: str,
        params: Union[Tuple[Any, ...], Dict[str, Any], None] = None,
    ) -> bool:
        try:
            self.cur.execute(sql, params)
            self.close()
            return True
        except Exception as err:
            raise err

    def execute_set(self, mapping_data: Dict[str, Union[Tuple[Any, ...], Dict[str, Any]]]) -> bool:
        try:
            self.conn.begin()
            for sql, params in mapping_data.items():
                self.cur.execute(sql, params)
            self.conn.commit()
            return True
        except Exception as err:
            self.conn.rollback()
            raise err

    def insert(
        self,
        sql: str,
        params: Union[Tuple[Any, ...], Dict[str, Any], None] = None,
    ) -> bool:
        try:
            self.execute(sql, params)
            self.close()
            return True
        except Exception as err:
            raise err

    def insertmany(self, sql: str, paramset: Union[Tuple[[Tuple[Any, ...]], ...], Tuple[Dict[str, Any], ...]]) -> bool:
        try:
            self.cur.executemany(sql, paramset)
            self.close()
            return True
        except Exception as err:
            raise err

    def delete(
        self,
        sql: str,
        params: Union[Tuple[Any, ...], Dict[str, Any], None] = None,
    ) -> bool:
        try:
            self.execute(sql, params)
            self.close()
            return True
        except Exception as err:
            raise err

    def select(
        self,
        sql: str,
        params: Union[Tuple[Any, ...], Dict[str, Any], None] = None,
    ) -> Union[Tuple[Tuple[Any, ...], ...], List[List[Any]]]:
        try:
            self.execute(sql, params)
            results = self.cur.fetchall()
            self.close()
            return results
        except Exception as err:
            raise err

    def update(
        self,
        sql: str,
        params: Union[Tuple[Any, ...], Dict[str, Any], None] = None,
    ) -> bool:
        try:
            self.execute(sql, params)
            self.close()
            return True
        except Exception as err:
            raise err

    def updatemany(self, sql: str, paramset: Union[Tuple[[Tuple[Any, ...]], ...], Tuple[Dict[str, Any], ...]]) -> bool:
        try:
            self.cur.executemany(sql, paramset)
            self.close()
            return True
        except Exception as err:
            raise err
