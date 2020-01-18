#!/usr/bin/python3
"""script that takes your Github credentials and uses the Github API"""

import requests as res
from sys import argv

if __name__ == "__main__":
    try:
        resp = res.get('https://api.github.com/user',  auth=(argv[1], argv[2]))
        print(resp.json().get('id'))
    except BaseException:
        pass
