#!/usr/bin/python3


class MyList(list):
    """Class who inherits from list"""
    def __init__(self):
        """Initializer"""
        super().__init__()

    def print_sorted(self):
        """Returns the list but sorted"""
        print(sorted(self.copy()))
