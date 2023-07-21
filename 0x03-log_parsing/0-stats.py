#!/usr/bin/python3
"""Computes metrics and print the statistics of inputs"""

from sys import stdin
import re


statuses = ["200", "301", "400", "401", "403", "404", "405", "500"]


def displayMetrics(fileSize: int, statusStat: dict) -> None:
    """Prints passed statistics to stdout"""

    print("File size: {}".format(fileSize))
    for status, count in sorted(statusStat.items()):
        if status in statuses:
            print("{}: {}".format(status, count))


def logParser() -> None:
    """Reads each line of stdin and prints statistics"""

    inputFormat = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' \
        r' - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]' \
        r' "(\w+ \S+ \S+)"' \
        r' (\d{3})' \
        r' (\d+)$'

    counter = 0
    statusCodes = {}
    fileSizeSum = 0

    try:
        for line in stdin:
            match = re.match(inputFormat, line)
            if not match:
                continue

            statusCode = match.group(4)
            fileSize = match.group(5)

            try:
                int(statusCode)
            except Exception:
                continue

            if statusCode not in statusCodes:
                statusCodes[statusCode] = 1
            else:
                statusCodes[statusCode] += 1

            fileSizeSum += int(fileSize)
            counter += 1

            if not counter % 10:
                displayMetrics(fileSizeSum, statusCodes)
        displayMetrics(fileSizeSum, statusCodes)
    except KeyboardInterrupt:
        displayMetrics(fileSizeSum, statusCodes)
        raise


if __name__ == '__main__':
    logParser()
