#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in the header"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
