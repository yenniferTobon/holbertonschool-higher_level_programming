#!/usr/bin/python3
import hidden_4
if (__name__ == "__main__"):
    namesModule = dir(hidden_4)
    for i in dir(hidden_4):
        if i[0] != "_":
            print(i)
