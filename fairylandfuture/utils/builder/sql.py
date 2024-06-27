# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-26 23:52:32 UTC+8
"""

from typing import Optional, Sequence

from fairylandfuture.structures.dataclass.utils.builder.sql import StructureFilterOption, StructureJoinOption, StructureGroupByOption


class BaseBuilderSQL:

    def __init__(self, table):
        self.table = table


class QueryBuilderSQL(BaseBuilderSQL):

    def __init__(self, table: str, fields: Sequence[str]):
        super().__init__(table)
        self.fields = fields
        self.__sql = " ".join(("select", ", ".join(fields), "from", self.table)) + ";"

    def operation(
        self,
        join: Optional[StructureJoinOption] = None,
        where: Optional[StructureFilterOption] = None,
        group_by: Optional[StructureGroupByOption] = None,
        order_by=None,
        limit=None,
    ):
        if group_by:
            group_by_field_list = group_by.field_list
            if group_by_field_list == self.fields:
                group_by = f"group_by {group_by}"
            elif [item.rsplit(".")[1] for item in group_by_field_list] == [item.rsplit(".")[1] for item in self.fields]:
                group_by = f"group_by {group_by}"
            else:
                raise 
        where = f"where {where}" if where else ""
        join = f"{join}" if join else ""
        
        return " ".join((self.__sql.rstrip(";"), join, where, group_by)) + ";"

    def __str__(self):
        return self.__sql


if __name__ == "__main__":

    # print(QueryBuilderSQL(database, table_name))
    from fairylandfuture.structures.dataclass.utils.builder.sql import (
        StructureFilterLogic,
        StructureFilterOption,
        StructureJoinCondition,
        StructureJoinLogic,
        StructureJoinOption,
        StructureGroupByOption,
    )

    database = "mysql"
    table_name = ("mysql.user", "mysql.host", "postgresql.id", "mog.name")

    leftjoin_table1 = "postgresql"
    leftjoin_condition1 = StructureJoinCondition("mysql", "user_id", "postgresql", "id")
    leftjoin_table2 = "mog"
    leftjoin_condition2 = StructureJoinCondition("mysql", "user_id", "mog", "id")

    join_postgresql = StructureJoinLogic("left join", leftjoin_table1, leftjoin_condition1)
    join_mog = StructureJoinLogic("left join", leftjoin_table2, leftjoin_condition2)

    where_add1 = StructureFilterLogic("name", "=")
    where_add2 = StructureFilterLogic("age", "!=")
    where_or1 = StructureFilterLogic("c", "is")
    where_or2 = StructureFilterLogic("d", "in")
    where_or_option1 = StructureFilterOption("or", (where_or1, where_or2))
    where_or_option2 = StructureFilterOption("and", (where_add1, where_add2))

    join_ = StructureJoinOption((join_postgresql, join_mog))
    where_ = StructureFilterOption("or", (where_or_option1, where_or_option2))
    group_ = StructureGroupByOption(("1", "2"))
    sql = QueryBuilderSQL(database, table_name).operation(join_, where_, group_)

    print(join_)
    print(where_, type(where_))
    print(sql, type(sql))
