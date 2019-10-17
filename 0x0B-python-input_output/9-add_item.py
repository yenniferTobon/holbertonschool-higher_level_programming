#!/usr/bin/python3
import sys
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    list = load_from_json_file(filename)
except:
    list = []

if list is not None:
    for aux in range(1, len(sys.argv)):
        list.append(sys.argv[aux])
    save_to_json_file(list, filename)
else:
    save_to_json_file(list, filename)
