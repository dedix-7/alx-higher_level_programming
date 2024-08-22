#!/usr/bin/python3
""" A module to add all arguments to a python list
    It uses previous moduels
"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
""" get the loading function
"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
""" Function to save the object to a file
"""

ls = [sys.argv[i] for i in range(1, (len(sys.argv)))]
with open('add_item.json', 'a', encoding="utf-8") as fildes:
    """ Use with so te context automatocally closes
    """

    try:
        form = load_from_json_file('add_item.json')
    except Exception as e:
        form = []
        form.extend(ls)
        save_to_json_file(form, 'add_item.json')
    else:
        form = load_from_json_file('add_item.json')
        form.extend(ls)
        save_to_json_file(form, 'add_item.json')
