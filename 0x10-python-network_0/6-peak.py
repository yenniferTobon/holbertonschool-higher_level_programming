#!/usr/bin/python3
def find_peak(list):
    """ Python function to find peak number"""
    le = len(list)
    if le == 0:
        return
    mayor = 0
    for i in range(len(list)):
        if (list[i] > mayor):
            mayor = list[i]
    return mayor
