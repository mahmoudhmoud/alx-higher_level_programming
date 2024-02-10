#!/usr/bin/python3

"""namodaj dyalo"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """morabao"""

    def __init__(self, size, x=0, y=0, id=None):

        """bani lih"""
        super().__init__(size, size, x, y, id)

    def __str__(self):

        """ado moraba"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):

        """hajmo"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):

        """tarika dakhilya"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):

        """hadato lih"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):

        """blasto ajo"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
