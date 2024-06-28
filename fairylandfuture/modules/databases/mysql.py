# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-26 23:16:19 UTC+8
"""

from typing import Union, Dict, Tuple, Any, Iterable

import pymysql
from pymysql.cursors import DictCursor

from fairylandfuture.core.abstracts.datasource import AbstractDataSource
from fairylandfuture.structures.builder.expression import StructureSQLExecuteParams, StructureSQLInsertManyParams


class MySQLConnector:

    def __init__(self, host: str, port: int, user: str, password: str, database: str, charset: str = "utf8mb4"):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__charset = charset

    @property
    def host(self) -> str:
        return self.__host

    @property
    def post(self) -> int:
        return self.__port

    @property
    def user(self) -> str:
        return self.__user

    @property
    def database(self) -> str:
        return self.__database

    @property
    def charset(self) -> str:
        return self.__charset

    def __connect_mysql(self) -> pymysql.connections.Connection:
        connection = pymysql.connect(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database,
            charset=self.__charset,
            cursorclass=DictCursor,
        )
        return connection

    @property
    def connect(self) -> pymysql.connections.Connection:
        return self.__connect_mysql()

    @property
    def cursor(self) -> DictCursor:
        return self.connect.cursor()

    def close(self) -> None:
        self.connect.close()
        self.cursor.close()

    def __del__(self):
        self.close()


class MySQLDataSource(AbstractDataSource, MySQLConnector):

    def __init__(self, host, port, user, password, database):
        super().__init__(host=host, port=port, user=user, password=password, database=database)
        # self._connection = pymysql.connect(host=host, port=port, user=user, password=password, database=database, cursorclass=DictCursor)
        # self._cursor = self._connection.cursor()

    def execute(self, params: StructureSQLExecuteParams):
        try:
            self.cursor.execute(params.expression, params.params)
            self.connect.commit()
            return True
        except Exception as err:
            self.connect.rollback()
            raise err

    def select(self, params: StructureSQLExecuteParams) -> Union[Dict[str, Any], Tuple[Dict[str, Any]], ...]:
        try:
            self.cursor.execute(params.expression, params.params)
            result = self.cursor.fetchall()
            if len(result) == 1:
                return result[0]
            return result
        except Exception as err:
            raise err

    def multiple(self, params: Iterable[StructureSQLExecuteParams]) -> bool:
        try:
            for param in params:
                self.cursor.execute(param.expression, param.params)
            self.connect.commit()
            return True
        except Exception as err:
            self.connect.rollback()
            raise err

    def insertmany(self, params: StructureSQLInsertManyParams) -> bool:
        try:
            self.cursor.executemany(params.expression, params.params)
            self.connect.commit()
            return True
        except Exception as err:
            self.connect.rollback()
            raise err

    def __del__(self):
        self._cursor.close()
        self._connection.close()
