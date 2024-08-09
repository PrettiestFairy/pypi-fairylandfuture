# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-10 11:40:48 UTC+08:00
"""


class ProgramException(Exception):

    def __init__(self, message: str = "Internal program error."):
        self.message = f"{self.__class__.__name__}: {message}"

    def __str__(self) -> str:
        return self.message


class InvalidParamsException(ProgramException):

    def __init__(self, message: str = "Parameter error."):
        super().__init__(message)


class ParamsTypeException(ProgramException):

    def __init__(self, message: str = "Parameter type error."):
        super().__init__(message)


class ParamsValueException(ProgramException):

    def __init__(self, message: str = "Parameter value error."):
        super().__init__(message)


class FileReadException(ProgramException):

    def __init__(self, message: str = "File read error."):
        super().__init__(message=message)


class ConfigReadException(ProgramException):

    def __init__(self, message: str = "Config read error."):
        super().__init__(message=message)


class SQLExecutionException(ProgramException):

    def __init__(self, message: str = "SQL execution error."):
        super().__init__(message=message)


class SQLSyntaxException(ProgramException):

    def __init__(self, message: str = "SQL syntax error."):
        super().__init__(message=message)
