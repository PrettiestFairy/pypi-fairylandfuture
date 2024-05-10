# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-10 12:34:34 UTC+8
"""

from typing import Union, Any, Optional
from datetime import datetime, timedelta
import time
from dateutil.relativedelta import relativedelta

from datetime import date as TypeDate
from datetime import time as TypeTime

from fairylandfuture.core.abstracts.metaclass import SingletonMeta
from fairylandfuture.constants.enums import DateTimeEnum
from fairylandfuture.util.verifies.validate import ParamTypeValidator


class DateTimeModule(SingletonMeta):
    """
    Date time utils.
    """

    @classmethod
    def date(cls, _format: str = DateTimeEnum.DATE.value) -> str:
        """
        Get the current date.

        :param _format: Date format.
        :type _format: str
        :return: Current date
        :rtype: str
        """
        return datetime.now().date().strftime(_format)

    @classmethod
    def time(cls, _fromat: str = DateTimeEnum.TIME.value) -> str:
        """
        Get the current time.

        :param _fromat: Time format.
        :type _fromat: str
        :return: Current time
        :rtype: str
        """
        return datetime.now().time().strftime(_fromat)

    @classmethod
    def datetime(cls, _format: str = DateTimeEnum.DATETIME.value) -> str:
        """
        Get the current datetime.

        :param _format: Datetime format.
        :type _format: str
        :return: Current datetime
        :rtype: str
        """
        return datetime.now().strftime(_format)

    @classmethod
    def timestamp(cls, millisecond: bool = False, n: Optional[int] = None) -> int:
        """
        Get the current timestamp.

        :return: Current timestamp.
        :rtype: int
        """
        validator = ParamTypeValidator({"millisecond": bool, "n": (int, type(None))})
        validator.validate({"millisecond": millisecond, "n": n})

        if millisecond:
            return int(round(time.time()) * 1000)
        if n:
            return int(round(time.time()) * (10 ** (n - 10)))

        return int(round(time.time()))

    @classmethod
    def timestamp_to_datetime(cls, timestamp: Union[int, float], _fromat: str = DateTimeEnum.DATETIME.value):
        """
        Convert timestamp to datetime.

        :param timestamp: Timestamp.
        :type timestamp: int or float
        :param _fromat: Datetime format.
        :type _fromat: str
        :return: Formatted datetime string.
        :rtype: str
        """
        if len(str(int(timestamp))) == 13:
            timestamp /= 1000
        return datetime.fromtimestamp(timestamp).strftime(_fromat)
