# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-12 22:23:51 UTC+8
"""

from typing import Union, Tuple, Dict, Any, List

import abc


class GenericSQL:

    def __init__(self, host: str, port: int, user: str, passwd: str, database: str):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database

    @abc.abstractmethod
    def connect(self): ...

    @abc.abstractmethod
    def cursor(self): ...

    @abc.abstractmethod
    def execute(
        self,
        query: str,
        params: Union[Tuple[str, int, float, ...], Dict[str, Union[str, int, float]]],
        *args,
        **kwargs,
    ) -> Union[List[List[Any]], Tuple[Tuple[Any, ...], ...]]: ...
