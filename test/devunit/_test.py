# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-12 12:34:53 UTC+8
"""

from pathlib import Path

from fairylandfuture.modules.decorators import TryCatchDecorator


class TestBase:
    @classmethod
    @TryCatchDecorator
    def run(cls):
        """
        This method will run all test methods in the class.
        It will try to catch any exception raised during the test and print it out.

        :return: None
        :rtype: NoneType
        """
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]
        for method in method_list:
            if method.startswith("test_"):
                getattr(cls, method)()



BASE_PATH = Path(__file__).resolve().parent.parent.parent


if __name__ == "__main__":
    print(BASE_PATH)
