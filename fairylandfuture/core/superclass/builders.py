# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-30 14:59:02 UTC+8
"""


class BaseBuilderSQL:
    """
    Base class for SQL builders.

    :param table: The table name.
    :type table: str

    Attributes:
        table: The table name.
    """

    def __init__(self, table):
        self.table = table


class BaseBuilderMySQL(BaseBuilderSQL):
    pass
