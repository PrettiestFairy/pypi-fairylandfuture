# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-18 下午6:44:40 UTC+8
"""

from typing import Tuple, Optional, Any

from dataclasses import dataclass, field


@dataclass
class SQLStruct:
    sql: str
    params: Optional[Tuple[Any, ...]] = field(default=None)
