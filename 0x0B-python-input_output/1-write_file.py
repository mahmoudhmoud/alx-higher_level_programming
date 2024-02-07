#!/usr/bin/python3

'''jidho lah'''


def write_file(filename="", text=""):

    """krah lih"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
