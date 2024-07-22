# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-12 22:23:51 UTC+8
"""

import abc
from typing import List, Any

from fairylandfuture.structures.builder.expression import StructureSQLExecuteParams, StructureSQLInsertManyParams
from fairylandfuture.structures.builder.expression import StructurePostgreSQLExecute


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

    @abc.abstractmethod
    def multiple(self, params: List[StructureSQLExecuteParams]) -> bool: ...

    @abc.abstractmethod
    def insertmany(self, params: StructureSQLInsertManyParams) -> bool: ...


class AbstractPostgreSQLOperation(abc.ABC):

    @abc.abstractmethod
    def execute(self, struct: StructurePostgreSQLExecute) -> bool: ...

    def insert(self, struct: StructurePostgreSQLExecute) -> bool:
        return self.execute(struct)

    def delete(self, struct: StructurePostgreSQLExecute) -> bool:
        return self.execute(struct)

    def update(self, struct: StructurePostgreSQLExecute) -> bool:
        return self.execute(struct)

    @abc.abstractmethod
    def select(self, struct: StructurePostgreSQLExecute) -> List[Any]: ...
