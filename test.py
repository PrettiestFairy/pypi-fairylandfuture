# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-09 17:04:24 UTC+8
"""

import setuptools

if __name__ == "__main__":
    exclude_tuple = (
        "bin",
        "conf",
        "deploy",
        "docs",
        "scripts",
        "temp",
        "test",
    )
    install_package_list = setuptools.find_packages(exclude=exclude_tuple)
    for i in install_package_list:
        print(i)
