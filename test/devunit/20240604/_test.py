# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-04 下午12:08:02 UTC+8
"""

from fairylandfuture.modules.datetimes import DateTimeModule
from fairylandfuture.utils.journal import journal

if __name__ == '__main__':
    journal.debug(f"2024-05-20 00:00:00 转为unix时间戳: {DateTimeModule.datetime_to_timestamp('2024-05-20 00:00:00', millisecond=True)}")
    journal.debug(f"2024-06-10 00:00:00 转为unix时间戳: {DateTimeModule.datetime_to_timestamp('2024-06-10 00:00:00', millisecond=True)}")
    journal.debug(f"{DateTimeModule.timestamp_to_datetime(1717477912000)}")
    journal.debug(f"{DateTimeModule.timestamp_to_datetime(1717478032000)}")
    journal.debug(f"{DateTimeModule.timestamp_to_datetime(1716134400000)}")
    journal.debug(f"{DateTimeModule.timestamp_to_datetime(1717948800000)}")
