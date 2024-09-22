# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-08-10 17:42:20 UTC+08:00
"""

import os
import re
import json

from array import array


class ValidateStringModule:

    @classmethod
    def valid_parentheses(cls, string: str, /) -> bool:
        """
        Validate parentheses.

        :param string: String to validate
        :type string: str
        :return: True if the parentheses are balanced, False otherwise
        :rtype: bool
        """
        stack = array("u")
        matching = {")": "(", "}": "{", "]": "["}

        for char in string:
            char: str

            if char in matching.values():
                stack.append(char)
            elif char in matching.keys():
                if not stack or stack.pop() != matching.get(char):
                    return False

        return not stack

    @classmethod
    def valid_json(cls, string: str, /) -> bool:
        """
        Validate JSON.

        :param string: String to validate
        :type string: str
        :return: True if the JSON is valid, False otherwise
        :rtype: bool
        """
        try:
            json.loads(string)
            return True
        except json.JSONDecodeError:
            return False
        except Exception as err:
            raise err

    @classmethod
    def vaild_url(cls, string: str, /) -> bool:
        """
        Validate URL.

        :param string: String to validate
        :type string: str
        :return: True if the URL is valid, False otherwise
        :rtype: bool
        """
        url_regex = re.compile(
            r"^(https?|ftp)://"
            r"((([A-Z0-9][A-Z0-9_-]*)(?:\.[A-Z0-9][A-Z0-9_-]*)+)"
            r"|localhost"
            r"|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
            r"|\[?[A-F0-9]*:[A-F0-9:]+]?)"
            r"(?::\d+)?"
            r"(?:/\S*)?$",
            re.IGNORECASE,
        )

        return re.match(url_regex, string) is not None

    @classmethod
    def valid_email(cls, string: str, /) -> bool:
        """
        Validate email.

        :param string: String to validate
        :type string: str
        :return: True if the email is valid, False otherwise
        :rtype: bool
        """
        email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

        return re.match(email_regex, string) is not None
