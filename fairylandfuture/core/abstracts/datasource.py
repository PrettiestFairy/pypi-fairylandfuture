# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-12 22:23:51 UTC+8
"""

from typing import Union, Tuple, Dict, Any, List

import abc

from fairylandfuture.models.dataclasses.datasource import QueryParams


class GenericDataSource(abc.ABC):

    @abc.abstractmethod
    def execute(self, params: QueryParams) -> bool: ...

    def insert(self, params: QueryParams) -> bool:
        return self.execute(params)

    def delete(self, params: QueryParams) -> bool:
        return self.execute(params)

    def update(self, params: QueryParams) -> bool:
        return self.execute(params)

    @abc.abstractmethod
    def select(self, params: QueryParams) -> Union[Dict[str, Any], List[Dict[str, Any]]]: ...

    @abc.abstractmethod
    def multiple(self, params: List[QueryParams]) -> bool: ...
    
    # TODO: execute many
