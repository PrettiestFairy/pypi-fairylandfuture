# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-10 11:27:49 UTC+8
"""

from typing import Literal, Union, Tuple, List, Dict

from fairylandfuture.models.dataclasses.datasource import SQLStruct

# log level
TypeLogLevel = Literal["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]

SQLStructList = Union[
    Tuple[SQLStruct, ...],
    List[SQLStruct]
]
