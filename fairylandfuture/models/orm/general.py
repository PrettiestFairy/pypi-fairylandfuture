# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-03 12:42:53 UTC+8
"""

from typing import Sequence


class BaseModel:

    def __init__(self, table: str, fields: Sequence[str]):
        self._table = table
        self._fields = fields

    @property
    def table(self):
        return self._table

    @property
    def fields(self):
        return self._fields
    
    def save(self, point): ...
