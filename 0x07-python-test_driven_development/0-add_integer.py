#!/usr/bin/python3
'''A module'''


def add_integer(a, b=98):
    '''A function'''

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int):
        raise TypeError('b must be an integer')
    else:
        return (a + b)
