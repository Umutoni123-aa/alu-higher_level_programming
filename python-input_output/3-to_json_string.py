#!/usr/bin/python3
'''script that returns a string'''


import json


def to_json_string(my_obj):
    '''json representation of a string'''
    return json.dumps(my_obj)
