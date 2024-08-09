# coding: utf8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-03 21:45:41 UTC+08:00
"""

from fairylandfuture.modules.datetimes import DatetimeModule
from fairylandfuture.constants.enums import DateTimeEnum

a = DatetimeModule.datetime_to_timestamp("2024-01-01", _format=DateTimeEnum.date)
a = DatetimeModule.datetime_to_timestamp("2024/01/01", _format="%Y/%m/%d")
a = DatetimeModule.datetime_to_timestamp("2024--01--01", _format="%Y--%m--%d")

print(a)
