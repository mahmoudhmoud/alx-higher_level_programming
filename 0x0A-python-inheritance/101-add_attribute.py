#!/usr/bin/python3

'''kalka ichhar'''


def add_attribute(obj, att, value):

    """zido alih"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
