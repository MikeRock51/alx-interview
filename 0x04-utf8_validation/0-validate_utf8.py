#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines of a given data set represents a valid UTF-8 encoding"""
    numOfBytes = 1

    for char in data:
        if numOfBytes == 1:
            if char >> 5 == 6:
                numOfBytes = 2
            elif char >> 4 == 14:
                numOfBytes = 3
            elif char >> 3 == 30:
                numOfBytes = 4
            elif char >> 7 == 1:
                return False
        else:
            if char >> 6 != 2:
                return False
            numOfBytes -= 1

    return numOfBytes == 1
