# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-19 上午11:26:00 UTC+8
"""

from datetime import datetime

from fairylandfuture.models.dataclasses.datasource import QueryParams
from fairylandfuture.modules.datasource import MySQLDataSource
from fairylandfuture.constants.enums import DateTimeEnum


datasource = MySQLDataSource(
    _HOST,
    _PORT,
    _USER,
    _PASSWORD,
    _DATABASE
)

query_now = QueryParams("select now() as now;")

add_col_sql = (
    "alter table tb_test "
    "add age int  default 0 not null;"
)
update_age = (
    "update tb_test "
    "set age = 18 "
    "where id = %(id)s"
)

query_name = (
    "select id, name, age "
    "from tb_test "
    "where id = %(id)s;"
)

instermany = (
    "insert into tb_test (name, age) "
    "values (%(name)s, %(age)s) ;"
)

instermany_v = (
    {
        "name": "于易轩",
        "age": 18
    },
    {
        "name": "郝清妍",
        "age": 20
    }
)

query_now_result = datasource.select(query_now)
now: datetime = query_now_result.get("now")
print(now.strftime(DateTimeEnum.DATETIME_CN))

multiple_exec = (
    QueryParams(add_col_sql),
    QueryParams(update_age, {"id": 1})
)

# print(datasource.multiple(multiple_exec))

datasource.insertmany(instermany, instermany_v)
