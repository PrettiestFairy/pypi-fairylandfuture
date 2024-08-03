# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 12:40:00 UTC+08:00
"""

from pathlib import Path
from collections import namedtuple, deque
from typing import Tuple
from dataclasses import dataclass

from test.utils.config import TestConfig

from fairylandfuture.modules.databases.postgresql import PostgreSQLConnector, PostgreSQLOperation
from fairylandfuture.structures.builder.expression import StructurePostgreSQLExecute
from fairylandfuture.utils.builder.convert import ConvertDataStructure


@dataclass(frozen=True)
class Data:
    id: int
    name: str
    gender: bool


class TestPostgreSQL(PostgreSQLConnector):
    pass


config = TestConfig(Path(r"C:\Lionel-Johnson\ProjectCodes\002-Python\github-PrettiestFairy\pypi-fairylandfuture\conf\dev\config.yaml")).config.get("postgresql")

connector = TestPostgreSQL(
    host=config.get("host"),
    port=config.get("port"),
    user=config.get("user"),
    password=config.get("password"),
    database=config.get("database")
)

pgsql = PostgreSQLOperation(connector)
pgsql2 = PostgreSQLOperation(connector)

# connector.cursor.execute("SELECT * FROM public_dev_test.author;")

data: Tuple[Data, ...] = pgsql.select(StructurePostgreSQLExecute("SELECT id, name, gender FROM public_dev_test.author where id = %s;", (1, )))
print(repr(data), repr(type(data[0])))
# data_column = ("id", "name", "gender")
# data = map(lambda x: namedtuple("Data", data_column)(*x), data)
# data = ConvertDataStructure.namedtuple(data_column, data)
res_data = [{"id": row.id, "name": row.name, "gender": "男" if row.gender else "女"} for row in data]

print(tuple(res_data), type(res_data))
