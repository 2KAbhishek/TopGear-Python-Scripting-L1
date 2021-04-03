#!/usr/bin/python
def ruler(num: int) -> str:
    rul, mark = 0, 1
    numStr, first, second = '1234567890', '', ''
    while rul <= num:
        first += ' ' * 9 + repr(mark) if num - rul >= 10 else ''
        second += numStr[:min(10, num - rul)]
        mark += 1
        rul += 10
    return first + '\n' + second


print(ruler(43))
