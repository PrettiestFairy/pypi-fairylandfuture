# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-08-10 18:31:36 UTC+08:00
"""

from fairylandfuture.core.superclass.exceptions import ProgramException


class SQLExecutionException(ProgramException):

    def __init__(self, message: str = "SQL execution error."):
        super().__init__(message=message)


class SQLSyntaxException(ProgramException):

    def __init__(self, message: str = "SQL syntax error."):
        super().__init__(message=message)
