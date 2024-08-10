# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-10 10:45:41 UTC+08:00
"""

from fairylandfuture.core.superclass.enumerate import BaseEnum


class DateTimeEnum(BaseEnum):
    """
    Date time enum.
    """

    date = "%Y-%m-%d"
    time = "%H:%M:%S"
    datetime = "%Y-%m-%d %H:%M:%S"

    date_cn = "%Y年%m月%d日"
    time_cn = "%H时%M分%S秒"
    datetime_cn = "%Y年%m月%d日 %H时%M分%S秒"

    default = datetime
    default_cn = datetime_cn


class EncodingEnum(BaseEnum):
    """
    Encoding enum.
    """

    utf8 = "UTF-8"
    gbk = "GBK"
    gb2312 = "GB2312"
    gb18030 = "GB18030"

    default = utf8


class LogLevelEnum(BaseEnum):
    """
    Log level Enum.
    """

    trace = "TRACE"
    debug = "DEBUG"
    info = "INFO"
    success = "SUCCESS"
    warning = "WARNING"
    error = "ERROR"
    critical = "CRITICAL"

    default = info


class PlatformEnum(BaseEnum):
    """
    Platform enum.
    """

    windows = "Windows"
    linux = "Linux"
    macos = "Darwin"
    darwin = "Darwin"


class FileModeEnum(BaseEnum):
    """
    file mode enum.
    """

    r = "r"
    rb = "rb"
    r_plus = "r+"
    rb_plus = "rb+"

    w = "w"
    wb = "wb"
    w_plus = "w+"
    wb_plus = "wb+"

    a = "a"
    ab = "ab"
    a_plus = "a+"
    ab_plus = "ab+"

    default = r
