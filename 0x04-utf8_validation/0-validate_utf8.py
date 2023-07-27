#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines of a given data set represents a valid UTF-8 encoding"""
    numOfBytes = 1

    for char in data:
        if numOfBytes == 1:
            if char >> 5 in [0b110, 0b1110]:
                numOfBytes = 2
            elif char >> 4 == 0b1110:
                numOfBytes = 3
            elif char >> 3 == 0b11110:
                numOfBytes = 4
            elif char >> 7 == 0b1:
                return False
        else:
            if char >> 6 != 0b10:
                return False
            numOfBytes -= 1
    return numOfBytes == 1
