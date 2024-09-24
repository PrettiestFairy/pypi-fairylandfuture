# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-24 15:26:48 UTC+08:00
"""

from typing import Any, Callable, Optional, Union, Sequence, Dict, Self

class Validator:
    def __init__(self: Self, required: bool, typedef: Union[type, Sequence[type]], validator_factory: Optional[Callable[[Any], bool]] = None) -> None: ...
    def validate(self: Self, value: Any) -> Any: ...

class RequestValidator:
    def __init__(self: Self, schema: Dict[str, Validator]) -> None: ...
    def validate(self: Self, request_data: Dict[str, Any]) -> Dict[str, Any]: ...
