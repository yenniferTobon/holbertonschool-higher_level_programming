#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenList = len(my_list)
    new_list = []
    if (idx < 0):
        return (my_list)
    elif (idx >= lenList):
        return (my_list)
    new_list = my_list.copy()
    new_list.remove(idx)
    new_list.insert(idx, element)
    return (new_list)
