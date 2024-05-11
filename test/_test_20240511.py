# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-11 13:53:27 UTC+8
"""

# 日志
from fairylandfuture.modules.journal import journal, logger

# 时间模块
from fairylandfuture.modules.datetimes import DateTimeModule

# 注解
from fairylandfuture.modules.decorators import ActionDecorator, TimingDecorator

# 枚举
from fairylandfuture.constants.enums import DateTimeEnum

from test._test_20240510 import TestDateTimeModule as TestDateTimeModule20240510


class TestDateTimeModule:

    @classmethod
    @TimingDecorator
    def run(cls):
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
        for method in method_list:
            if method.startswith("test_"):
                getattr(cls, method)()

    @classmethod
    @ActionDecorator(action="日期转时间戳")
    def test_datetime_to_timestamp(cls):
        _date = "2024-05-11"
        _time = "13:53:27"
        timestamp = DateTimeModule.datetime_to_timestamp(" ".join((_date, _time)))
        journal.debug(timestamp)


if __name__ == "__main__":
    TestDateTimeModule.run()
