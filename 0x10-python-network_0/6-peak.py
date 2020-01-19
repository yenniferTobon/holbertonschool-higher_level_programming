#!/usr/bin/python3
""" Python function to find peak number"""


def find_peak(list):
    le = len(list)
    if le == 0:
        return
    de = le // 2
    if (de == le - 1 or list[de] >= list[de + 1]) and\
            (de == 0 or list[de] >= list[de - 1]):
        return (list[de])
    elif de != le - 1 and list[de + 1] > list[de]:
        return (find_peak(list[de + 1:]))
    else:
        return (find_peak(list[:de]))
