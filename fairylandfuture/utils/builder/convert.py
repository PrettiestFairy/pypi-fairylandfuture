# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-22 15:26:23 UTC+08:00
"""

from collections import namedtuple


class ConvertDataStructure:

    @classmethod
    def namedtuple(cls, fields, dataset, typename="BuildNamedtuple"):
        return map(lambda x: namedtuple(typename, fields)(*x), dataset)
