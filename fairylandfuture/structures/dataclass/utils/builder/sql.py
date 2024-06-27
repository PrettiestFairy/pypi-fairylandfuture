# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-27 00:07:43 UTC+8
"""

from __future__ import annotations

from typing import Any, Sequence, Union, Optional
from dataclasses import dataclass, field


@dataclass(frozen=True)
class StructureFilterLogic:
    """
    SQL where clauses
    """

    name: str
    logic: str  # option: = , != ...
    value: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "value", f"%({self.name})s")

    def __str__(self):
        return f"{self.name} {self.logic} {self.value}"


@dataclass(frozen=True)
class StructureFilterOption:
    option: Optional[str]
    filter_field: Union[Sequence[StructureFilterLogic], Sequence[StructureFilterOption]]

    def __str__(self):
        return f" {self.option} ".join([str(element) for element in self.filter_field])


@dataclass(frozen=True)
class StructureJoinCondition:
    table1: str
    field1: str
    table2: str
    field2: str

    def __str__(self):
        return f"{self.table1}.{self.field1} = {self.table2}.{self.field2}"


@dataclass(frozen=True)
class StructureJoinLogic:
    type: str
    table: str
    condition: StructureJoinCondition

    def __str__(self):
        return f"{self.type} {self.table} on {self.condition}"


@dataclass(frozen=True)
class StructureJoinOption:
    option: Sequence[StructureJoinLogic]

    def __str__(self):
        return " ".join([str(element) for element in self.option])


@dataclass(frozen=True)
class StructureGroupByOption:
    field_list: Sequence[str]

    def __str__(self):
        return ", ".join(self.field_list)
