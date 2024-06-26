# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-26 00:09:01 UTC+8
"""

import os
import sys
import platform

from fairylandfuture.constants.enums import PlatformEnum

from fairylandfuture.utils.general.common import OSPlatform

print(PlatformEnum.WINDOWS.value)

print(sys.platform)
print(platform.architecture())
print(platform.system())
print(platform.node())

print(OSPlatform.get_os_platform())
print(sys.version)
print(sys.version_info.major, sys.version_info.minor)
print(sys.version.split()[0])

# print(os.getgid())
# print(os.getgid())
