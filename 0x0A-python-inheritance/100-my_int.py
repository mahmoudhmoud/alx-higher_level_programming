#!/usr/bin/python3

'''fih'''


class MyInt(int):

    """ikno wasr"""
    def __new__(cls, *args, **kwargs):

        """sawab jdid"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):

        """achno tam"""
        return int(self) != other

    def __ne__(self, other):

        """kan hatakan"""
        return int(self) == other
