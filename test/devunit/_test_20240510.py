# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-10 10:15:06 UTC+8
"""

# 常量 - 工具类
from fairylandfuture.util.general.constants import DefaultConstantUtils, APIConstantUtils, EncodingConstantUtils

# 常量
from fairylandfuture.constants.enums import DateTimeEnum, EncodingEnum, LogLevelEnum

# 日志
from fairylandfuture.modules.journal import journal, logger

# 注解
from fairylandfuture.modules.decorators import SingletonDecorator, TimingDecorator, TipsDecorator, ActionDecorator, TryCatchDecorator

# 抽象类 - 枚举
from fairylandfuture.core.abstracts.enumerate import EnumBase, StringEnum, IntegerEnum

# 抽象类 - 元类
from fairylandfuture.core.abstracts.metaclass import SingletonMeta, SingletonABCMeta

# 类型标识
from fairylandfuture.constants.typed import TypeLogLevel

# 时间模块
from fairylandfuture.modules.datetimes import DateTimeModule


class TestDateTimeModule:

    @classmethod
    @TimingDecorator
    def run(cls):
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
        for method in method_list:
            if method.startswith("test_"):
                getattr(cls, method)()

    @classmethod
    @ActionDecorator(action="获取当前日期")
    def test_date(cls):
        date = DateTimeModule.date()
        journal.debug(date)
        date = DateTimeModule.date("%Y/%m/%d")  # format: %Y/%m/%d
        journal.debug(date)  # Output: 2024/05/10

    @classmethod
    @ActionDecorator(action="获取当前时间")
    def test_time(cls):
        time = DateTimeModule.time()
        journal.debug(time)
        time = DateTimeModule.time("%H--%M--%S")  # format: %H--%M--%S
        journal.debug(time)  # Output: 10--15--06

    @classmethod
    @ActionDecorator(action="获取当前日期时间")
    def test_datetime(cls):
        datetime = DateTimeModule.datetime()
        journal.debug(datetime)
        datetime = DateTimeModule.datetime("%Y/%m/%d %H--%M--%S")  # format: %Y/%m/%d %H--%M--%S
        journal.debug(datetime)  # Output: 2024/05/10 10--15--06

    @classmethod
    @ActionDecorator(action="获取当前时间标准时间戳")
    def test_timestamp(cls):
        timestamp = DateTimeModule.timestamp(n=9)
        journal.debug(timestamp)  # Output: 1620689306

    @classmethod
    @ActionDecorator(action="时间戳转日期时间")
    def test_timestamp_to_datetime(cls):
        timestamp = 1715340030  # 2021-05-11 07:28:26
        # timestamp = 1620689306000  # 2021-05-11 07:28:26
        datetime = DateTimeModule.timestamp_to_datetime(timestamp)
        journal.debug(datetime)  # Output: 2021-05-11 07:28:26


if __name__ == "__main__":
    TestDateTimeModule.run()
