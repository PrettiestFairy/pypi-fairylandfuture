# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-26 23:52:32 UTC+8
"""

from typing import Optional, Sequence

from fairylandfuture.structures.builder.expression import (
    StructureSQLFilterOption,
    StructureSQLJoinOption,
    StructureSQLGroupByOption,
    StructureSQLOrderByOption,
    StructureSQLLimitOption,
)
from fairylandfuture.modules.exceptions import SQLSyntaxError


class BaseBuilderSQL:

    def __init__(self, table):
        self.table = table


class QueryBuilderSQL(BaseBuilderSQL):

    def __init__(self, table: str, fields: Optional[Sequence[str]] = None):
        super().__init__(table=table)
        self.fields = fields
        if not self.fields:
            self.sql = f"select * from {self.table};"
        else:
            self.sql = f"select {', '.join(fields)} from {self.table};"

    def operation(
        self,
        join: Optional[StructureSQLJoinOption] = None,
        where: Optional[StructureSQLFilterOption] = None,
        group_by: Optional[StructureSQLGroupByOption] = None,
        order_by: Optional[StructureSQLOrderByOption] = None,
        limit: Optional[StructureSQLLimitOption] = None,
    ):
        join = f"{join}" if join else ""
        where = f"where {where}" if where else ""
        if group_by:
            if group_by.field_list == self.fields:
                group_by = f"group_by {group_by}"
            else:
                raise SQLSyntaxError("group_by fields must be in select fields.")
        else:
            group_by = ""
        order_by = f"order_by {order_by}" if order_by else ""
        limit = f"limit {limit}" if limit else ""
        sql = " ".join((self.sql.rstrip(";"), join, where, group_by, order_by, limit))

        return " ".join(sql.split()) + ";"

    def to_string(self):
        return self.sql

    def __str__(self):
        return self.sql


class InsertBuilderSQL(BaseBuilderSQL):

    def __init__(self, table: str, fields: Sequence[str]):
        super().__init__(table=table)
        self.fields = fields
        self.sql = f"insert into {self.table} ({', '.join(fields)}) values ({', '.join(['%({})s'.format(field) for field in fields])});"
        # f"INSERT INTO {self.table} ({', '.join(fields)}) VALUES ({', '.join(['%(' + field + ')s' for field in fields])});"

    def to_string(self):
        return self.sql

    def __str__(self):
        return self.sql
