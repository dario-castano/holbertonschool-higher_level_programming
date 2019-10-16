#!/usr/bin/python3


class MyInt(int):
    """This is a rebel int"""
    def __eq__(self, other):
        """Weird =="""
        return self.__int__() != other.__int__()

    def __ne__(self, other):
        """Even more weird !="""
        return self.__int__() == other.__int__()
