# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 18:29:47 UTC+08:00
"""


class InvalidParamsException(ProgramException):

    def __init__(self, message: str = "Parameter error."):
        super().__init__(message)


class ParamsTypeException(ProgramException):

    def __init__(self, message: str = "Parameter type error."):
        super().__init__(message)


class ParamsValueException(ProgramException):

    def __init__(self, message: str = "Parameter value error."):
        super().__init__(message)
