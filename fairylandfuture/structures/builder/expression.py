# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-27 00:07:43 UTC+08:00
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple, Union, Sequence, MutableSequence, Mapping, MutableMapping
from dataclasses import dataclass, field


@dataclass(frozen=True)
class StructureMySQLExecute:
    query: str
    args: Optional[Union[Sequence, MutableSequence, Mapping, MutableMapping]] = field(default=None)


@dataclass(frozen=True)
class StructurePostgreSQLExecute:
    query: str
    vars: Optional[Union[Sequence, MutableSequence, Mapping, MutableMapping]] = field(default=None)
