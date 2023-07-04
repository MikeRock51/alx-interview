#!usr/bin/python3
"""Lockboxes"""

def canUnlockAll(boxes):
    unusedKeys = []
    locked = []

    index = 1
    while index < len(boxes) - 1:
        currentKeys = boxes[index - 1]

        if index in currentKeys:
            currentKeys.remove(index)
        else:
            locked.append(index)
        for key in currentKeys:
            unusedKeys.append(key)
        index += 1

    if len(locked) == 0:
        return True

    for index in locked:
        if not index in unusedKeys:
            return False
    return True
