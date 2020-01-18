#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl --head -s "$1" | grep "Allow" | cut -d " " -f 2,3,4
