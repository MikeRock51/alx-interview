#!/usr/bin/python3
"""Solution to 0x01-lockboxes interview question"""

def canUnlockAll(boxes):
    """Checks whether or not all lockboxes can be unlocked"""
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
