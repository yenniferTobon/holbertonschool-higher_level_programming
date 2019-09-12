#!/usr/bin/python3
import sys
from calculator_1 import sub
n = 0
argvs = sys.argv
countArgv = len(argvs)
argvReal = sub(countArgv, 1)
if argvReal == 0:
    print("{} arguments.".format(argvReal))
else:
    print("{} arguments:".format(argvReal))

for n in range(1, countArgv):
    print("{}: {}".format(n, (argvs[n])))
