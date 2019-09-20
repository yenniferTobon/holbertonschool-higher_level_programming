#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    new_list = []
    sortList = []
    for k in a_dictionary:
        new_list.append(a_dictionary.get(k))
        new_list.sort()
    for l in a_dictionary:
        if new_list[-1] == a_dictionary.get(l):
            return l
