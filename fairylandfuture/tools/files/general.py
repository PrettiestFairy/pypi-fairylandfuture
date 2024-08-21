# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-06-30 14:20:28 UTC+08:00
"""

from fairylandfuture.core.superclass.files import FileBase, TextFileBase, YamlFileBase, JsonFileBase


class File(FileBase):
    """Base File class."""


class TextFile(TextFileBase):
    """Base Text File class."""


class YamlFile(YamlFileBase):
    """Base YAML File class."""


class JsonFile(JsonFileBase):
    """Base JSON File class."""


class OtherFile(TextFileBase):
    """Other File class."""
