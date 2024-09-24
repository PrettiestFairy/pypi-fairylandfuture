# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-09-24 14:55:40 UTC+08:00
"""

import abc
from typing import Any, Callable, Optional


class AbstractValidator(abc.ABC):

    @abc.abstractmethod
    def validate(self, value: Any) -> Any: ...
