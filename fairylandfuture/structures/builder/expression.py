# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-27 00:07:43 UTC+8
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union, Sequence
from dataclasses import dataclass, field


@dataclass
class StructureSQLExecuteParams:
    """
    Execcute Query parameters for a data source.

    Attrs:
        expression: The SQL expression to execute.
        params: The parameters to substitute into the expression.
    Usage:
        >>> from fairylandfuture.structures.builder.expression import ExecuteParams
        >>> ExecuteParams(expression="select * from table where id = %s", params=[1])
        QueryParams(expression='select * from table where id = %s', params=[1])
    Note:
        The `params` attribute can be a list, tuple, or dictionary. If it is a list or tuple,
        the values will be substituted in the order they appear in the list or tuple. If it is a dictionary,
        the values will be substituted by their keys.
    """

    expression: str
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[str, Any]]] = field(default=None)


@dataclass
class StructureSQLInsertManyParams:
    """
    Multiple Execute Query parameters for a data source.

    Attrs:
        expression: The SQL expression to execute.
        params: The parameters to substitute into the expression.
    Usage:
        >>> from fairylandfuture.structures.builder.expression import InsertManyParams
        >>> parasm = [
        >>>     ("郝淑慧", 18),
        >>>     ("李雪琴", 19)
        >>> ]
        >>> InsertManyParams(expression="insert into table (name, age) values (%s, %s)", params=parasm)
        MultipleParams(expression='insert into table (name, age) values (%s, %s)', params=[('郝淑慧', 18), ("李雪琴", 19)])
    """

    expression: str
    params: Union[List[Union[List[Any], Tuple[Any, ...], Dict[str, Any]]], Tuple[Union[List[Any], Tuple[Any, ...], Dict[str, Any]], ...]]


@dataclass(frozen=True)
class StructureSQLFilterLogic:
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
class StructureSQLFilterOption:
    option: Optional[str]
    filter_field: Union[Sequence[StructureSQLFilterLogic], Sequence[StructureSQLFilterOption]]

    def __str__(self):
        return f" {self.option} ".join([str(element) for element in self.filter_field])


@dataclass(frozen=True)
class StructureSQLJoinCondition:
    table1: str
    field1: str
    table2: str
    field2: str

    def __str__(self):
        return f"{self.table1}.{self.field1} = {self.table2}.{self.field2}"


@dataclass(frozen=True)
class StructureSQLJoinLogic:
    type: str
    table: str
    condition: StructureSQLJoinCondition

    def __str__(self):
        return f"{self.type} {self.table} on {self.condition}"


@dataclass(frozen=True)
class StructureSQLJoinOption:
    option: Sequence[StructureSQLJoinLogic]

    def __str__(self):
        return " ".join([str(element) for element in self.option])


@dataclass(frozen=True)
class StructureSQLGroupByOption:
    field_list: Sequence[str]

    def __str__(self):
        return ", ".join(self.field_list)


@dataclass(frozen=True)
class StructureSQLOrderByOption:
    field_list: Sequence[str]

    def __str__(self):
        return ", ".join(self.field_list)


@dataclass(frozen=True)
class StructureSQLLimitOption:
    limit: int
    offset: int = field(default=0)

    def __str__(self):
        return f"{self.limit} offset {self.offset}"
