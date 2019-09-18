#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        firts = None
    else:
        firts = sentence[0]
    lenString = len(sentence)
    return (lenString, firts)
