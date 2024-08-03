# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-05 12:12:07 UTC+08:00
"""

import re
import psycopg2

from typing import Optional, Sequence, Tuple, Any, NamedTuple, Union
from psycopg2.extras import NamedTupleCursor

from fairylandfuture.modules.decorators import SingletonDecorator
from fairylandfuture.core.abstracts.databases import AbstractPostgreSQLConnector
from fairylandfuture.core.abstracts.databases import AbstractPostgreSQLOperation
from fairylandfuture.structures.builder.expression import StructurePostgreSQLExecute


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
        >>> print(result)
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
            self._dsn = " ".join((self._dsn, f"options='-c search_path={self._schema}'"))

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
        """
        Reconnect to PostgreSQL database.

        :return: ...
        :rtype: ...
        """
        if not self.connect.exist:
            self.connect: CustomPostgreSQLConnect = self.__connect()
            self.cursor: CustomPostgreSQLCursor = self.connect.cursor(cursor_factory=CustomPostgreSQLCursor)
        if not self.cursor.exist and self.connect.exist:
            self.cursor: CustomPostgreSQLCursor = self.connect.cursor(cursor_factory=CustomPostgreSQLCursor)

    def close(self) -> None:
        """
        Close the connection to PostgreSQL database.

        :return: ...
        :rtype: ...
        """
        if self.cursor.exist:
            self.cursor.close()

        if self.connect.exist:
            self.connect.close()

    def __del__(self):
        self.close()


@SingletonDecorator
class PostgreSQLOperation(AbstractPostgreSQLOperation):
    """
    PostgreSQLOperation is a class for executing SQL queries on PostgreSQL database.

    :param connector: The PostgreSQLConnector instance.
    :type connector: PostgreSQLConnector

    Usage::
        >>> from fairylandfuture.modules.databases.postgresql import PostgreSQLConnector, PostgreSQLOperation
        >>> from fairylandfuture.structures.builder.expression import StructurePostgreSQLExecute
        >>> connector = PostgreSQLConnector(host="localhost", port=5432, user="postgres", password="password", database="test")
        >>> operation = PostgreSQLOperation(connector)
        >>> data = operation.select(StructurePostgreSQLExecute("SELECT * FROM users"))
        >>> print(data)

    **Notice:**
    The `connector` must be an instance of `PostgreSQLConnector`.
    PostgreSQLOperation is singleton class.

    """

    def __init__(self, connector: PostgreSQLConnector):
        if not isinstance(connector, PostgreSQLConnector) or isinstance(connector, type):
            raise TypeError("The connector must be an instance or subclass instance of PostgreSQLConnector.")

        self.connector = connector

    def execute(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        """
        Execute a SQL query on PostgreSQL database.

        :param struct: PostgreSQL execute structure.
        :type struct: StructurePostgreSQLExecute
        :return: PostgreSQL query result.
        :rtype: bool | tuple
        """
        try:
            self.connector.reconnect()
            self.connector.cursor.execute(struct.query, struct.vars)
            data = self.connector.cursor.fetchall()

            if not data:
                return True

            return tuple(data)
        except Exception as err:
            raise err
        finally:
            self.connector.close()

    def select(self, struct: StructurePostgreSQLExecute, /) -> Tuple[NamedTuple, ...]:
        """
        Select data from PostgreSQL database.

        :param struct: PostgreSQL Query structure.
        :type struct: StructurePostgreSQLExecute
        :return: Query result.
        :rtype: tuple
        """
        try:
            data = self.execute(struct)
            return tuple(data)
        except Exception as err:
            raise err
        finally:
            self.connector.close()

    def executemany(self, struct: StructurePostgreSQLExecute) -> bool:
        """
        Execute multiple SQL queries on PostgreSQL database.
        Generally used for batch insertion, update, and deletion of data.

        :param struct: PostgreSQL execute structure.
        :type struct: StructurePostgreSQLExecute
        :return: Execute status.
        :rtype: bool
        """
        try:
            self.connector.reconnect()
            self.connector.cursor.executemany(struct.query, struct.vars)
            self.connector.connect.commit()
            return True
        except Exception as err:
            self.connector.connect.rollback()
            raise err
        finally:
            self.connector.close()

    def multi(self, structs: Sequence[StructurePostgreSQLExecute]):
        """
        Execute multiple SQL queries on PostgreSQL database.

        :param structs: Sequence of PostgreSQL execute structures.
        :type structs: Sequence[StructurePostgreSQLExecute]
        :return: Execute status.
        :rtype: bool
        """
        try:
            self.connector.reconnect()
            for struct in structs:
                self.connector.cursor.execute(struct.query, struct.vars)
            self.connector.connect.commit()
            return True
        except Exception as err:
            self.connector.connect.rollback()
            raise err
        finally:
            self.connector.close()
