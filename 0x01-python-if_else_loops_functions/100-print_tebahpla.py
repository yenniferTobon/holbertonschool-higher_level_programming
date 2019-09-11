#!/usr/bin/python3
for n in range(122, 96, -1):
    if (n % 2 == 0):
        count = 0
    else:
        count = -32
    print("{:c}". format(n + count), end="")
