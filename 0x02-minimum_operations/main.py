#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# print(minOperations(12))
# print(minOperations(4))
# print(minOperations(9))
# print(minOperations(99))
# print(minOperations(2147483640))
# print(minOperations(19170307))
# print(minOperations(972))
