# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-09 16:48:09 UTC+8
"""

from typing import Literal

import setuptools
import subprocess
import os.path
from datetime import datetime

_MARK_TYPE = Literal["release", "test", "alpha", "beta"]

ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class InstallDependenciesCommand(setuptools.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        command = "python -m pip install --force git+https://github.com/imba-tjd/pip-autoremove@ups"
        subprocess.call(command, shell=True)


class PackageInfo(object):
    """
    Public package

    :param major: major num
    :type major: int
    :param sub: sub num
    :type sub: int
    :param stage: stage num
    :type stage: int
    :param revise: revise num
    :type revise: int
    :param mark: version mark
    :type mark: str
    """

    def __init__(self, major: int, sub: int, stage: int, revise: int, mark: _MARK_TYPE):
        self.__major = self.__paramscheck(major, int)
        self.__sub = self.__paramscheck(sub, int)
        self.__stage = self.__paramscheck(stage, int)
        self.__revise = self.__paramscheck(revise, int)

        if not mark.lower() in _MARK_TYPE.__args__:
            raise TypeError(f"Param: mark type error, mark must in {_MARK_TYPE.__args__}.")

        self.__mark = mark

    @property
    def name(self):
        return "PyFairylandFuture"

    @property
    def author(self):
        return "Lionel Johnson"

    @property
    def email(self):
        return "fairylandfuture@outlook.com"

    @property
    def url(self):
        return "https://github.com/PrettiestFairy/pypi-fairylandfuture"

    @property
    def version(self):
        if len(self.__revise.__str__()) < 5:
            nbit = 5 - len(self.__revise.__str__())
            self.__revise = "".join((("0" * nbit), self.__revise.__str__()))
        else:
            self.__revise = self.__revise.__str__()

        date_str = datetime.now().date().__str__().replace("-", "")
        revise_after = "-".join((self.__revise.__str__(), date_str))
        release_version = ".".join((self.__major.__str__(), self.__sub.__str__(), self.__stage.__str__()))

        if self.__mark == "release":
            version = release_version
        elif self.__mark == "test":
            version = ".".join((release_version, "".join(("rc", revise_after))))
        elif self.__mark == "alpha":
            version = ".".join((release_version, "".join(("alpha", revise_after))))
        elif self.__mark == "beta":
            version = ".".join((release_version, "".join(("beta", revise_after))))
        else:
            version = ".".join((release_version, "".join(("rc", revise_after))))

        return version

    @property
    def description(self):
        return "personally developed Python library."

    @property
    def long_description(self):
        with open(os.path.join(self.__root, "README.md"), "r", encoding="UTF-8") as FileIO:
            long_description = FileIO.read()

        return long_description

    @property
    def long_description_content_type(self):
        return "text/markdown"

    @property
    def packages_include(self):
        include = ("fairylandfuture",)

        return include

    @property
    def packages_exclude(self):
        exclude = ("fairylandfuture/test",)

        return exclude

    @property
    def fullname(self):
        return self.name + self.version

    @property
    def python_requires(self):
        return ">=3.7"

    @property
    def keywords(self):
        return ["fairyland", "Fairyland", "pyfairyland", "PyFairyland", "fairy", "Fairy"]

    @property
    def include_package_data(self):
        return True

    @property
    def classifiers(self):
        results = [
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Programming Language :: SQL",
            "Framework :: Django :: 2",
            "Framework :: Django :: 3",
            "Framework :: Django :: 4",
            "Framework :: Flask",
            "Framework :: FastAPI",
            "Framework :: Flake8",
            "Framework :: IPython",
            "Framework :: Jupyter",
            "Framework :: Scrapy",
            "Natural Language :: English",
            "Natural Language :: Chinese (Simplified)",
            "Operating System :: Microsoft :: Windows :: Windows 11",
            "Operating System :: POSIX :: Linux",
            "Operating System :: POSIX :: Linux",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Software Development :: Libraries :: Application Frameworks",
            "Topic :: Software Development :: Version Control :: Git",
            "Topic :: System :: Operating System Kernels :: Linux",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        ]

        return results

    @property
    def install_requires(self):
        results = [
            "loguru",
            "pip-review",
            # "pip-autoremove",
            # "black",
            # "python-dotenv",
            # "pymysql",
            # "psycopg2-binary",
            # "pyyaml",
            # "requests",
            # "fake-useragent",
            # "tornado",
            # "pandas",
            # "django",
            # "django-stubs",
            # "djangorestframework",
            # "django-cors-headers",
        ]
        return results

    @property
    def cmdclass(self):
        results = {
            "install_dependencies": InstallDependenciesCommand,
        }
        return results

    def __paramscheck(self, param, _type):
        if not isinstance(param, _type):
            raise TypeError(f"{param} type error.")

        return param
