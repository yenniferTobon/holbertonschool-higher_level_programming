#!/usr/bin/python3
"""
MyList inherits from list
Public instance method: print_stored() that prints the sorted list
"""


class MyList(list):
    """
    Class that inherits from list.
    """
    def print_sorted(self):
        """
        Function that prints a list sorted.
        """
        list_new = []
        list_new = self.copy()
        list_new.sort()
        print(list_new)
