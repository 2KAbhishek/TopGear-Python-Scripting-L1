#!/usr/bin/python
import sys


def isWhiteLine(line: str) -> bool:
    return line.isspace()


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    print(''.join([x for x in lines if not isWhiteLine(x)]))
