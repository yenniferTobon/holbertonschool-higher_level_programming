#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status, use the package requests """
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
