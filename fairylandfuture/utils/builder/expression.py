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

    def __init__(self, table: str, fields: Sequence[str]):
        super().__init__(table=table)
        self.fields = fields
        self.__sql = " ".join(("select", ", ".join(fields), "from", self.table)) + ";"

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
        sql = " ".join((self.__sql.rstrip(";"), join, where, group_by, order_by, limit))

        return " ".join(sql.split()) + ";"

    def __str__(self):
        return self.__sql


if __name__ == "__main__":
    from fairylandfuture.structures.builder.expression import (
        StructureSQLFilterLogic,
        StructureSQLFilterOption,
        StructureSQLJoinCondition,
        StructureSQLJoinLogic,
        StructureSQLJoinOption,
        StructureSQLGroupByOption,
        StructureSQLOrderByOption,
    )

    database = "mysql"
    table_name = ("mysql.user", "mysql.host", "postgresql.id", "mog.name")

    leftjoin_table1 = "postgresql"
    leftjoin_condition1 = StructureSQLJoinCondition("mysql", "user_id", "postgresql", "id")
    leftjoin_table2 = "mog"
    leftjoin_condition2 = StructureSQLJoinCondition("mysql", "user_id", "mog", "id")

    join_postgresql = StructureSQLJoinLogic("left join", leftjoin_table1, leftjoin_condition1)
    join_mog = StructureSQLJoinLogic("left join", leftjoin_table2, leftjoin_condition2)

    where_add1 = StructureSQLFilterLogic("name", "=")
    where_add2 = StructureSQLFilterLogic("age", "!=")
    where_or1 = StructureSQLFilterLogic("c", "is")
    where_or2 = StructureSQLFilterLogic("d", "in")
    where_or_option1 = StructureSQLFilterOption("or", (where_or1, where_or2))
    where_or_option2 = StructureSQLFilterOption("and", (where_add1, where_add2))

    join_ = StructureSQLJoinOption((join_postgresql, join_mog))
    where_ = StructureSQLFilterOption("or", (where_or_option1, where_or_option2))
    group_ = StructureSQLGroupByOption(("mysql.user", "mysql.host"))
    order_ = StructureSQLOrderByOption(("userid desc", "id"))
    limit_ = StructureSQLLimitOption(limit=10)
    sql = QueryBuilderSQL(database, table_name).operation(join=join_, where=where_, order_by=order_, limit=limit_)

    print(repr(sql))
