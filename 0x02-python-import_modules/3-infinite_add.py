#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    suma = 0
    argvs = sys.argv
    for n in range(1, len(argvs)):
        suma = suma + int(argvs[n])
    print("{}".format(suma))
