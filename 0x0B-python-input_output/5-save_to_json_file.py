#!/usr/bin/python3

'''adado lih'''


import json


def save_to_json_file(my_obj, filename):

    """katbo lih"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
