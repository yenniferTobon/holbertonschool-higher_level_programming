#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenList = len(my_list)
    if (idx < 0):
        return (my_list)
    elif (idx > lenList):
        return (my_list)
    else:
        for i in range(len(my_list)):
            if (i == idx):
                my_list[idx] = element
                return (my_list)
