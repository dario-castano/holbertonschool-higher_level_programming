#!/usr/bin/python3

import sys
import os.path

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

newlist = my_list + sys.argv[1:]
save_to_json_file(newlist, filename)
