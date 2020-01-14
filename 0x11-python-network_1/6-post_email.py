#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data)
    print(response.text)
