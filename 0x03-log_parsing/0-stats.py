#!/usr/bin/python3
"""Computes metrics and print the statistics of inputs"""

from sys import stdin
import re


def logParser():
    """Reads each line of stdin and prints statistics"""

    inputFormat = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' \
        r' - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]' \
        r' "(\w+ \S+ \S+)"' \
        r' (\d{3})' \
        r' (\d+)$'

    counter = 0
    statusCodes = {}
    fileSizeSum = 0
    statuses = ["200", "301", "400", "401", "403", "404", "405", "500"]

    for line in stdin:
        match = re.match(inputFormat, line)
        if not match:
            continue

        statusCode = match.group(4)
        fileSize = match.group(5)

        if statusCode not in statusCodes:
            statusCodes[statusCode] = 1
        else:
            statusCodes[statusCode] += 1

        fileSizeSum += int(fileSize)

        counter += 1

        if not counter % 10:
            print(f"File size: {fileSizeSum}")
            for status, count in sorted(statusCodes.items()):
                if status in statuses:
                    try:
                        int(status)
                        print(f"{status}: {count}")
                    except Exception:
                        continue

if __name__ == '__main__':
    logParser()
