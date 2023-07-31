#!/usr/bin/python3
"""
    Solve the N Queens Problem
    (See README for instruction)
"""

from sys import argv


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    int(argv[1])
except Exception:
    print("N must be a number")
    exit(1)

N = int(argv[1])

if N < 4:
    print("N must be at least 4")
    exit(1)

print(type(N))
