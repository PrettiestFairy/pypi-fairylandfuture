# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-26 23:16:19 UTC+08:00
"""

import functools
from typing import Union, Dict, Tuple, Any

import pymysql
from pymysql.cursors import DictCursor

from fairylandfuture.interface.databases import AbstractMySQLOperation
from fairylandfuture.utils.decorators import SingletonDecorator
from fairylandfuture.exceptions.databases import SQLSyntaxException
from fairylandfuture.structures.builder.databases import StructureMySQLExecute


class CustomMySQLConnection(pymysql.connections.Connection):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__exist = True

    def close(self):
        super().close()
        self.__exist = False

    @property
    def exist(self):
        return self.__exist


class CustomMySQLCursor(DictCursor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__exist = True

    def close(self):
        super().close()
        self.__exist = False

    @property
    def exist(self):
        return self.__exist


class MySQLConnector:
    """
    This class is used to connect to MySQL database and execute SQL statements.

    It is a subclass of AbstractMySQLConnector and implements the methods of AbstractMySQLOperation.

    :param host: The host name of the MySQL server.
    :type host: str
    :param port: The port number of the MySQL server.
    :type port: int
    :param user: The user name used to connect to the MySQL server.
    :type user: str
    :param password: The password used to connect to the MySQL server.
    :type password: str
    :param database: The name of the database to connect to.
    :type database: str
    :param charset: The character set used to connect to the MySQL server.
    :type charset: str, optional

    Usage:
        >>> from fairylandfuture.modules.databases.mysql import MySQLConnector
        >>> connector = MySQLConnector(host="localhost", port=3306, user="root", password="password", database="test")
        >>> connector.cursor.execute("SELECT * FROM users")
        >>> result = connector.cursor.fetchall()
        >>> print(result)
        [{'id': 1, 'name': 'John', 'age': 25}, {'id': 2, 'name': 'Mary', 'age': 30}]
        >>> connector.close()
    """

    def __init__(self, host: str, port: int, user: str, password: str, database: str, charset: str = "utf8mb4"):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__charset = charset
        self.connection: CustomMySQLConnection = self.__connect()
        self.cursor: CustomMySQLCursor = self.connection.cursor()

    @property
    def host(self) -> str:
        return self.__host

    @property
    def port(self) -> int:
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

    def __connect(self) -> CustomMySQLConnection:
        """
        This method is used to connect to the MySQL server.

        :return: Connection object.
        :rtype: CustomMySQLConnection
        """
        connection = CustomMySQLConnection(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database,
            charset=self.__charset,
            cursorclass=CustomMySQLCursor,
        )

        return connection

    def reconnect(self) -> None:
        """
        This method is used to reconnect to the MySQL server.

        :return: ...
        :rtype: ...
        """
        if not self.connection.exist:
            self.connection: CustomMySQLConnection = self.__connect()
            self.cursor: CustomMySQLCursor = self.connection.cursor()
        if not self.cursor.exist and self.connection.exist:
            self.cursor: CustomMySQLCursor = self.connection.cursor()

    @staticmethod
    def reload(func):
        """
        This method is used to reload the connection and cursor object if they are closed.

        :param func: Decorated function.
        :type func: MethodType
        :return: ...
        :rtype: ...
        """

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            self.reconnect()
            return func(self, *args, **kwargs)

        return wrapper

    def close(self) -> None:
        """
        This method is used to close the connection and cursor object.

        :return: ...
        :rtype: ...
        """
        if self.cursor.exist:
            self.cursor.close()
        if self.connection.exist:
            self.connection.close()

    def __del__(self):
        self.close()


@SingletonDecorator
class MySQLOperation(AbstractMySQLOperation):

    def __init__(self, connector: MySQLConnector):
        if not isinstance(connector, MySQLConnector) or isinstance(connector, type):
            raise TypeError("The connector must be an instance or subclass instance of MySQLConnector.")

        self.connector = connector

    def execute(self, struct: StructureMySQLExecute, /) -> Union[bool, Tuple[Dict[str, Any], ...]]:
        try:
            self.connector.reconnect()
            self.connector.cursor.execute(struct.query, struct.args)
            data = self.connector.cursor.fetchall()
            self.connector.connection.commit()

            if not data:
                return True

            return tuple(data)
        except Exception as err:
            raise err
        finally:
            self.connector.close()

    def select(self, struct: StructureMySQLExecute, /) -> Tuple[Dict[str, Any], ...]:
        if not struct.query.lower().startswith("select"):
            raise SQLSyntaxException("The query must be a select statement.")

        try:
            return self.execute(struct)
        except Exception as err:
            raise err
        finally:
            self.connector.close()
