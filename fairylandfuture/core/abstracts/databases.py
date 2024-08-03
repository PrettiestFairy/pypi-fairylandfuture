# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-12 22:23:51 UTC+08:00
"""

import abc

from typing import List, Tuple, NamedTuple, Union

from fairylandfuture.structures.builder.expression import StructureSQLExecuteParams, StructureSQLInsertManyParams
from fairylandfuture.structures.builder.expression import StructurePostgreSQLExecute
from fairylandfuture.modules.exceptions import SQLSyntaxError


class AbstractDatabase(abc.ABC):

    @abc.abstractmethod
    def close(self) -> None: ...

    @abc.abstractmethod
    def reconnect(self) -> None: ...


class AbstractMySQLConnector(AbstractDatabase):

    @abc.abstractmethod
    def close(self) -> None: ...

    @abc.abstractmethod
    def reconnect(self) -> None: ...


class AbstractPostgreSQLConnector(AbstractDatabase):

    @abc.abstractmethod
    def close(self) -> None: ...

    @abc.abstractmethod
    def reconnect(self) -> None: ...


class AbstractMySQLOperation(abc.ABC):
    # Fixme: Refactor AbstractMySQLOperation

    @abc.abstractmethod
    def execute(self, params: StructureSQLExecuteParams) -> bool: ...

    def insert(self, params: StructureSQLExecuteParams) -> bool:
        return self.execute(params)

    def delete(self, params: StructureSQLExecuteParams) -> bool:
        return self.execute(params)

    def update(self, params: StructureSQLExecuteParams) -> bool:
        return self.execute(params)

    @abc.abstractmethod
    def select(self, params: StructureSQLExecuteParams): ...


class AbstractPostgreSQLOperation(abc.ABC):

    @abc.abstractmethod
    def execute(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        ...

    def insert(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("insert"):
            raise SQLSyntaxError("SQL syntax error. The query must be an insert statement.")
        return self.execute(struct)

    def delete(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("delete"):
            raise SQLSyntaxError("SQL syntax error. The query must be a delete statement.")
        return self.execute(struct)

    def update(self, struct: StructurePostgreSQLExecute, /) -> Union[bool, Tuple[NamedTuple, ...]]:
        if not struct.query.lower().startswith("update"):
            raise SQLSyntaxError("SQL syntax error. The query must be an update statement.")
        return self.execute(struct)

    @abc.abstractmethod
    def select(self, struct: StructurePostgreSQLExecute, /) -> Tuple[NamedTuple, ...]:
        ...
