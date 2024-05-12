# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-12 02:24:21 UTC+8
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

from fairylandfuture.modules.datetimes import DateTimeModule
from fairylandfuture.constants.enums import DateTimeEnum
from fairylandfuture.modules.journal import journal

from _test import TestBase


class TestClass(TestBase):

    @classmethod
    def test_001(cls):
        journal.debug(DateTimeModule.timestamp())

    @classmethod
    def test_002(cls):
        a = datetime.now() - relativedelta(days=1)
        journal.debug(a.strftime(DateTimeEnum.TIME_CN.value))

    @classmethod
    def test_003(cls):
        a = DateTimeModule.daysdelta("2024/05/12", "2024/05/25", _format="%Y/%m/%d")
        b = DateTimeModule.datetime_to_timestamp("2024/05/12", millisecond=False, _format="%Y/%m/%d")
        c = DateTimeModule.datetime_to_timestamp("2024--05--25", millisecond=False, _format="%Y--%m--%d")
        d = DateTimeModule.daysdelta(b, c, timestamp=True)
        journal.debug(a)
        journal.debug(b)
        journal.debug(c)
        journal.debug(d)


if __name__ == "__main__":
    TestClass.run()
