# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-18 下午6:44:40 UTC+8
"""

from typing import Tuple, Optional, Any, Union, List, Dict

from dataclasses import dataclass, field


@dataclass
class QueryParams:
    """
    Query parameters for a data source.
    
    Attributes:
        expression: The SQL expression to execute.
        params: The parameters to substitute into the expression.
    Usage:
        >>> from fairylandfuture.models.dataclasses.datasource import QueryParams
        >>> QueryParams(expression="SELECT * FROM table WHERE id = %s", params=[1])
        QueryParams(expression='SELECT * FROM table WHERE id = %s', params=[1])
    Note:
        The `params` attribute can be a list, tuple, or dictionary. If it is a list or tuple, the values will be substituted in the order they appear in the list or tuple. If it is a dictionary, the values will be substituted by their keys.
    """
    expression: str
    params: Optional[Union[List[Any], Tuple[Any, ...], Dict[str, Any]]] = field(default=None)
