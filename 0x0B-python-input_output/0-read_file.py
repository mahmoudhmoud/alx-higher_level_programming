#!/usr/bin/python3

'''ajidho makn'''


def read_file(filename=""):

    '''krah'''
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
