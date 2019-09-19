#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lenList = len(my_list)
    new_list = my_list
    if (idx < 0):
        return my_list
    elif (idx > lenList):
        return my_list
    else:
        for i in range(len(my_list)):
            if (i == idx):
                new_list[idx:idx + 1] = []
                return (new_list)
