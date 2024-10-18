# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-10-15 17:13:42 UTC+08:00
"""

from faker import Faker

from fairylandfuture.core.superclass.toolkits.fakerlib import BaseFaker


class FakeNetworkToolkits(BaseFaker):

    @classmethod
    def generate_ipv4_address(cls):
        return cls.faker.ipv4()
