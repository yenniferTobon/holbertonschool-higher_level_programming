#!/usr/bin/pyhton3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    if my_list == None:
        return None
    for i in my_list:
        print("{:d}".format(i))
