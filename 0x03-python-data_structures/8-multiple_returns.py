#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        firts = "None"
    else:
        firts = sentence[0]
    lenString = len(sentence)
    return (lenString, firts)
