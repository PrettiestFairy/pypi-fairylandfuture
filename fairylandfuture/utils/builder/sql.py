# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-26 23:52:32 UTC+8
"""

from typing import Optional

from fairylandfuture.structures.dataclass.utils.builder.sql import StructureFilterOption


class BaseBuilderSQL:

    def __init__(self, table):
        self.table = table


class QueryBuilderSQL(BaseBuilderSQL):

    def __init__(self, table, fields):
        super().__init__(table)
        self.fields = fields
        self.__sql = f"select {self.fields} from {self.table};"

    def __str__(self):
        return self.__sql

    def operation(self, where: Optional[StructureFilterOption] = None):
        where = f"where {where}" if where else ""
        return " ".join((self.__sql.rstrip(";"), where)) + ";"


if __name__ == "__main__":
    database = "mysql"
    table_name = "user"
    print(QueryBuilderSQL(database, table_name))
    from fairylandfuture.structures.dataclass.utils.builder.sql import StructureFilterLogic, StructureFilterOption

    a = StructureFilterLogic("name", "=")
    b = StructureFilterLogic("age", "!=")
    c = StructureFilterLogic("c", "is")
    d = StructureFilterLogic("d", "in")
    print(a, type(a))
    print(isinstance(a, StructureFilterLogic))
    where_ = StructureFilterOption("or", (StructureFilterOption("or", (c, d)), StructureFilterOption("and", (a, b))))
    print(QueryBuilderSQL(database, table_name).operation(where_), type(QueryBuilderSQL(database, table_name).operation(where_)))
