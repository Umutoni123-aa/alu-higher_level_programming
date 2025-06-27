#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # For each (key, value) pair:
    #   The key remains the same.
    #   The value is multiplied by 2.
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict
