# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-02 上午12:02:50 UTC+8
"""

from fairylandfuture.utils.journal import journal
from fairylandfuture.utils.networking.local import LocalNetworkUtils
from fairylandfuture.modules.datetimes import DateTimeModule
from fairylandfuture.constants.enums import DateTimeEnum

ts = DateTimeModule.datetime_to_timestamp("2024-06-03", _format=DateTimeEnum.DATE)

journal.debug("测试DEBUG日志")
journal.debug(str(ts))
journal.debug(LocalNetworkUtils.default_ip_address())
