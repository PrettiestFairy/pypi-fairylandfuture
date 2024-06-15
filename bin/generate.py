# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-19 下午2:15:55 UTC+8
"""

import os
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent

DEV_CASE_CONFIG_FILE_PATH = os.path.join(ROOT_PATH, "conf", "case", "dev.config.yaml")
