# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-27 00:07:43 UTC+08:00
"""

from dataclasses import dataclass, field
from typing import Optional, Union, Sequence, MutableSequence, Mapping, MutableMapping


@dataclass(frozen=True)
class StructureMySQLExecute:
    query: str
    args: Optional[Union[Sequence, MutableSequence, Mapping, MutableMapping]] = field(default=None)


@dataclass(frozen=True)
class StructurePostgreSQLExecute:
    query: str
    vars: Optional[Union[Sequence, MutableSequence, Mapping, MutableMapping]] = field(default=None)
