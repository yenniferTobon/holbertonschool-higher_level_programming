#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
copyNumber = number

if copyNumber < 0:
    copyNumber = -copyNumber
    lastDigit = copyNumber % 10
    lastDigit = lastDigit * (-1)
else:
    lastDigit = copyNumber % 10
print("Last digit of", end=" ")

if lastDigit > 5:
    print("{} is {} and is greater than 5". format(number, lastDigit))
elif lastDigit == 0:
    print("{} is {} and is 0". format(number, lastDigit))
else:
    print("{} is {} and is less than 6 and not 0". format(number, lastDigit))
