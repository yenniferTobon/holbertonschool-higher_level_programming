#!/usr/bin/pyhton3
def print_reversed_list_integer(my_list=[]):
    lenList = len(my_list) - 1
    if my_list is None:
        return None
    for i in range(len(my_list)):
        print("{:d}".format(my_list[lenList - i]))
