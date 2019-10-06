#!/usr/bin/python3
def text_indentation(text):
    """
    This module cuts line with
    '., ?, ;' delimeters
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text is not None:
        for i in range(len(text)):
            if text[i] is " " and text[i + 1] is " ":
                continue
            if text[i] is " " and (text[i - 1] is "." or text[i - 1] is "?"):
                continue
            if text[i] is " " and (text[i - 1] is ":" or text[i - 1] is " "):
                continue
            print("{}".format(text[i]), end="")
            if text[i] is "." or text[i] is "?" or text[i] is ":":
                print()
                print()
