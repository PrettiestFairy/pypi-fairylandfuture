# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-04 10:38:31 UTC+08:00
"""

import json

from dataclasses import dataclass, asdict, astuple

from typing import Dict, Any, Tuple, Self, Union


@dataclass(frozen=True)
class BaseStructure:

    @property
    def asdict(self: Self) -> Dict[str, Any]:
        return asdict(self)

    @property
    def astuple(self: Self) -> Tuple[Any, ...]:
        return astuple(self)

    @property
    def string(self: Self) -> str:
        return json.dumps(self.asdict, separators=(",", ":"), ensure_ascii=False)

    def to_dict(self: Self, /, *, ignorenone: bool = False) -> Union[Dict[Any, Any], property]:
        if ignorenone:
            return {k: v for k, v in self.asdict.items() if v is not None}
        else:
            return self.asdict

    def to_jsonstring(self: Self, /, *, ignorenone: bool = False) -> str:
        return json.dumps(self.to_dict(ignorenone=ignorenone), separators=(",", ":"), ensure_ascii=False)
