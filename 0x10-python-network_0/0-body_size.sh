#!/bin/bash
#Displays the size of the body of the response
curl -s --head "$1" | grep Content-Length | cut -d ':' -f2 | cut -d ' ' -f2
