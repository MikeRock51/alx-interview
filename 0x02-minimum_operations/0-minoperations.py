#!/usr/bin/python3
"""
    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given a
    number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
"""

def minOperations(n: int) -> int:
    """
        Calculates the fewest number of operations needed to
        result in exactly n H characters in the file.
    """

    minOp: int = 0

    if n < 2:
        return 0

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                minOp += i
                n //= i
                break
    return minOp

# print(minOperations(12))
# print(minOperations(4))
# print(minOperations(9))
# print(minOperations(99))
# print(minOperations(2147483640))
# print(minOperations(19170307))
# print(minOperations(972))
