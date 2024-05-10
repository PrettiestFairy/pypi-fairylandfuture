# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-09 16:38:27 UTC+8
"""

import os
import setuptools

from deploy.publish import PackageInfo

package = PackageInfo(1, 0, 0, 6, "alpha")

setuptools.setup(
    name=package.name,
    fullname=package.fullname,
    keywords=package.keywords,
    version=package.version,
    author=package.author,
    author_email=package.email,
    description=package.description,
    long_description=package.long_description,
    long_description_content_type=package.long_description_content_type,
    url=package.url,
    packages=setuptools.find_packages(include=package.packages_include, exclude=package.packages_exclude),
    include_package_data=package.include_package_data,
    classifiers=package.classifiers,
    python_requires=package.python_requires,
    install_requires=package.install_requires,
    cmdclass=package.cmdclass,
)
