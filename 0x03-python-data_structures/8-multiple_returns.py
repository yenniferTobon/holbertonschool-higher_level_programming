#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        firts = None
    else:
        firts = sentence[0]
    lenString = len(sentence)
    return (lenString, firts)
