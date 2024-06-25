# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-18 下午7:21:31 UTC+8
"""

from fairylandfuture.modules.datasource import MySQLDataSource

mysql = MySQLDataSource(
    _HOST,
    _PORT,
    _USER,
    _PASSWORD,
    _DATABASE
)

print(mysql.select("select now();"))



