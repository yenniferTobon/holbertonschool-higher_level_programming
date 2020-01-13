#!/usr/bin/python3
"""request to the URL- urllib.error.HTTPError exceptions and print: Error"""

import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as eRROR:
        print("Error code: {}".format(eRROR.code))
