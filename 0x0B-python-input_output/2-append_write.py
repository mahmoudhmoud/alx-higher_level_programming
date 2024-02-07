#!/usr/bin/python3

'''haddlih dyalo tam'''


def append_write(filename="", text=""):

    """is forit"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
