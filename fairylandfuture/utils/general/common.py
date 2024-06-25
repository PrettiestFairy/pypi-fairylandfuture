# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-26 00:29:04 UTC+8
"""

import os
import sys
import platform


class OSPlatform:
    """
    OS Platform
    """

    @staticmethod
    def get_os_platform():
        """
        Get OS Platform
        :return: OS Platform
        """
        return platform.system()

    @staticmethod
    def get_os_uid():
        """
        Get OS UID
        :return: OS UID
        """
        return os.getuid()

    @staticmethod
    def get_os_gid():
        """
        Get OS PID
        :return: OS PID
        """
        return os.getgid()

    @staticmethod
    def get_os_username():
        """
        Get OS Username
        :return: OS Username
        """
        return os.getlogin()

    @staticmethod
    def get_os_version():
        """
        Get OS Version
        :return: OS Version
        """
        return platform.version()

    @staticmethod
    def get_os_architecture():
        """
        Get OS Architecture
        :return: OS Architecture
        """
        return platform.machine()
