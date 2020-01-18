#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API"""
import requests as res
from sys import argv

if __name__ == "__main__":

    resp = res.get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    try:
        resp = resp.json()
        print("Number of results: {}".format(resp['count']))
        for result in resp['results']:
            print(result['name'])
    except ValueError:
        print("Not a valid JSON")
