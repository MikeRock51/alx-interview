#!/usr/bin/python3
"""Computes metrics and print the statistics of inputs"""

from sys import stdin
from typing import List
import re


def validateFormat(splitInput: List[str]) -> bool:
    """Validates if input string is the right format"""

    pass


def logParser():
    """Reads each line of stdin and prints statistics"""

    inputFormat = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' \
                     r' - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]' \
                     r' "(\w+ \S+ \S+)"' \
                     r' (\d{3})' \
                     r' (\d+)$'

    for line in stdin:
       if re.match(inputFormat, line):
           print('Matched')
       else:
           print('Not Matched')

if __name__ == '__main__':
    logParser()
