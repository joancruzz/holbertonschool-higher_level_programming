#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    mylist = load_from_json_file(filename)
except FileNotFoundError:
    mylist = []

for num in range(1, len(argv)):
    mylist.append(argv[num])
save_to_json_file(mylist, filename)
