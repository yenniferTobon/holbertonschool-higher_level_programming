#!/usr/bin/python3
for n in range(122, 96, -1):
    if (n % 2 != 0):
        letra = n - 32
    else:
        letra = n
    print("{:c}". format(letra), end="")
