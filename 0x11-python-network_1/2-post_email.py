#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as res:
        response = res.read()
        print(response.decode('utf-8'))
