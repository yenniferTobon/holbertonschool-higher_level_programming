#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == 'None':
        return 0
    new_list = []
    suma = 0
    diccio = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    for idx in range(len(roman_string)):
        for elem in diccio:
            if roman_string[idx] == elem:
                new_list.append(diccio[elem])
    if len(new_list) != len(roman_string):
        return (0)

    for k in range(len(roman_string)):
        new_list.append(diccio.get(roman_string[k]))
    for x in range(len(new_list)):
        if x  == len(new_list) - 1 or new_list[x] >= new_list[x + 1]:
            suma += new_list[x]
        else:
            suma -= new_list[x]
    return (suma)
