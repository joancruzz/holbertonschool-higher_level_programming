#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = []
try:
    filename = load_json("add_item.json")

except:
    filename = []
elements = len(sys.argv)
for num in range(1, elements):
    filename.append(sys.argv[num])
save_to_json_file(filename, "add_item.json")
