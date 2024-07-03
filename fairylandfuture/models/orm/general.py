# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-03 12:42:53 UTC+8
"""

from typing import Sequence

from fairylandfuture.core.metaclasses.model import ModelMeta


class BaseModel(metaclass=ModelMeta):

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        super().__init__()

    def save(self):
        sql = f"insert into {self.table_name}({', '.join(self.fields)}) values ({', '.join(['%({})s'.format(field) for field in self.fields])})"
        params = {field: getattr(self, field) for field in self.fields}
        print(sql, params)
