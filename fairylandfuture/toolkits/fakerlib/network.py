# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-10-15 17:13:42 UTC+08:00
"""

from fairylandfuture.toolkits.fakerlib.general import FakeGeneralToolkits


class FakeNetworkToolkits(FakeGeneralToolkits):

    @classmethod
    def generate_ipv4_address(cls):
        return cls.faker.ipv4()
