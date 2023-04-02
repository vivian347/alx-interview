#!/usr/bin/python3
"""Determines whether all locked boxes can be opened"""


def canUnlockAll(boxes):
    """required method"""
    unlocked = [0]
    for id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != id:
                unlocked.append(key)

    if len(unlocked) == len(boxes):
        return True
    return False
