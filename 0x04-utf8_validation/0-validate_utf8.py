#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines of a given data set represents a valid UTF-8 encoding"""
    if type(data) != list or len(data) < 1:
        return False

    bits = len(format(data[0], '07b'))

    for n in data:
        if len(format(n, '07b')) != bits:
            return False

    return True
