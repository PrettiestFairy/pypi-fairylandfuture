# coding: utf-8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-08 11:15:14 UTC+08:00
"""

from fairylandfuture.modules.journal import Journal

journal = Journal(serialize=True)

journal.debug("DEBUG")
journal.info("INFO")
