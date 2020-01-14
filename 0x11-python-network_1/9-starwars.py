#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API"""
import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":

    values = {'search': sys.argv[1]}
    url = 'https://swapi.co/api/people/'
    response = requests.post(url, data=values)
    try:
        response.json()
        print("Number of results:", response.json().get("count"))
        for result in response.json().get("results"):
            print(result.get("name"))
    except ValueError:
        print("Not a valid JSON")
