# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-05 12:12:07 UTC+8
"""

import re
import psycopg2
from typing import Optional

from psycopg2.extras import NamedTupleCursor

from fairylandfuture.core.abstracts.databases import AbstractPostgreSQLConnector


class CustomPostgreSQLConnect(psycopg2.extensions.connection):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._exist = True

    def close(self):
        super().close()
        self._exist = False

    @property
    def exist(self) -> bool:
        return self._exist


class CustomPostgreSQLCursor(NamedTupleCursor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._exist = True

    def close(self):
        super().close()
        self._exist = False

    @property
    def exist(self) -> bool:
        return self._exist


class PostgreSQLConnector(AbstractPostgreSQLConnector):
    """
    PostgreSQLConnector is a class for connecting to PostgreSQL database.

    :param host: The host of PostgreSQL database.
    :type host: str
    :param port: The port of PostgreSQL database.
    :type port: int
    :param user: The user of PostgreSQL database.
    :type user: str
    :param password: The password of PostgreSQL database.
    :type password: str
    :param database: The name of PostgreSQL database.
    :type database: str
    :param schema: The schema of PostgreSQL database.
    :type schema: str

    Usage::
        >>> from fairylandfuture.modules.databases.postgresql import PostgreSQLConnector
        >>> connector = PostgreSQLConnector(host="localhost", port=5432, user="postgres", password="password", database="test")
        >>> connector.cursor.execute("SELECT * FROM users")
        >>> result = connector.cursor.fetchall()
        >>> connector.close()
    """

    def __init__(self, host: str, port: int, user: str, password: str, database: str, schema: Optional[str] = None):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database
        self._schema = schema
        self._dsn = f"host={self._host} port={self._port} user={self._user} password={self._password} dbname={self._database}"

        if self._schema:
            self._dsn += f" options='-c search_path={self._schema}'"

        self.connect: CustomPostgreSQLConnect = self.__connect()
        self.cursor: CustomPostgreSQLCursor = self.connect.cursor(cursor_factory=CustomPostgreSQLCursor)

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def user(self) -> str:
        return self._user

    @property
    def database(self) -> str:
        return self._database

    def __dsn_mark_password(self):
        return re.sub(r"(password=)\S+", r"\1******", self._dsn)

    @property
    def dsn(self) -> str:
        return self.__dsn_mark_password()

    def __connect(self):
        connect = psycopg2.connect(dsn=self._dsn, connection_factory=CustomPostgreSQLConnect, cursor_factory=CustomPostgreSQLCursor)

        return connect

    def reconnect(self) -> None:
        if not self.connect.exist:
            self.connect: CustomPostgreSQLConnect = self.__connect()
            self.cursor: CustomPostgreSQLCursor = self.connect.cursor(cursor_factory=CustomPostgreSQLCursor)
        if not self.cursor.exist and self.connect.exist:
            self.cursor: CustomPostgreSQLCursor = self.connect.cursor(cursor_factory=CustomPostgreSQLCursor)

    def close(self) -> None:
        if self.cursor.exist:
            self.cursor.close()

        if self.connect.exist:
            self.connect.close()

    def __del__(self):
        self.close()
