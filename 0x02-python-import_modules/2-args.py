#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argvs = sys.argv
    argvReal = len(argvs) - 1
    if argvReal == 0:
        print("{} arguments.".format(argvReal))
    elif argvReal == 1:
        print("{} argument:".format(argvReal))
    else:
        print("{} arguments:".format(argvReal))
    for n in range(1, argvReal + 1):
        print("{}: {}".format(n, argvs[n]))
