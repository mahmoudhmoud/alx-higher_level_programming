#!/usr/bin/python3

'''fih ach biti'''


class Student:

    """takdim"""
    def __init__(self, first_name, last_name, age):

        """hamlo"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        '''ajo lih'''
        return self.__dict__
