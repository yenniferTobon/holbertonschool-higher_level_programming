#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":

    if len(sys.argv) != 1:
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
    url = 'http://b6a6580ced66.19.hbtn-cod.io:5000/search_user'
    response = requests.post(url, values)
    try:
        if not response.json():
            print('No result')
        else:
            print('[{}] {}'.format(response.json().get('id'),
                                   response.json().get('name')))
    except ValueError:
        print("Not a valid JSON")
