#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenList = len(my_list)
    new_list = my_list.copy()
    if (idx < 0):
        return (new_list)
    elif (idx >= lenList):
        return (new_list)
    new_list.remove(idx + 1)
    new_list.insert(idx, element)
    return (new_list)
