#!/usr/bin/python3
"""Computes metrics and print the statistics of inputs"""

from sys import stdin
import re


# statuses = ["200", "301", "400", "401", "403", "404", "405", "500"]


def displayMetrics(fileSize: int, statusStat: dict) -> None:
    """Prints passed statistics to stdout"""
    print("File size: {}".format(fileSize))
    for status, count in sorted(statusStat.items()):
        print("{}: {}".format(status, count))


def logParser() -> None:
    """Reads each line of stdin and prints statistics"""

    inputFormat = r'^(?P<ip>.+)' \
        r'\s*-\s*\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\]' \
        r'\s+"GET\s+/projects/260\s+HTTP/1\.1"' \
        r'\s+(?P<statusCode>200|301|400|401|403|404|405|500)' \
        r'\s+(?P<fileSize>\d{1,4})\n$'

    counter = 0
    statusCodes = {}
    fileSizeSum = 0

    try:
        for line in stdin:
            match = re.match(inputFormat, line)
            if not match:
                fileSize = (line.split()[-1].strip('\\n'))
                try:
                    fileSizeSum += int(fileSize)
                except Exception:
                    pass
                continue

            statusCode = match.group('statusCode')
            fileSize = match.group('fileSize')

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
    except KeyboardInterrupt:
        displayMetrics(fileSizeSum, statusCodes)
        raise
    finally:
        displayMetrics(fileSizeSum, statusCodes)


if __name__ == '__main__':
    logParser()
