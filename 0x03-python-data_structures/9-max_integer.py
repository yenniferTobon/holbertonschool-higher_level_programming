#!/usr/bin/python3
def max_integer(my_list=[]):
    number = my_list[0]
    if not my_list:
        return None
    for i in range(len(my_list)):
        if number >= my_list[i]:
            number = number
        else:
            number = my_list[i]
    return number
