#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code > 200:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
