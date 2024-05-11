# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-11 17:02:12 UTC+8
"""

import requests
import os


def count_commits(token):
    url = "https://api.github.com/repos/PrettiestFairy/pypi-fairylandfuture/commits"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            commit_data = response.json()
            print(f"Fetched {len(commit_data)} commits")
            return len(commit_data)
        else:
            print(f"Failed to fetch commits, status code: {response.status_code}")
            return 0
    except Exception as err:
        print(f"Failed to fetch commits, error: {err}")
        return 0


def write_commit_count(commit_count):
    with open(".commitrc", "w") as file:
        file.write(commit_count)


if __name__ == "__main__":
    TOKEN = os.environ.get("GITHUB_TOKEN")
    commit_count = count_commits(TOKEN)
    if commit_count:
        write_commit_count(str(commit_count))
