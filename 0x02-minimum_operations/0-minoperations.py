#!/usr/bin/env python3

#""" Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file."""


def minOperations(n: int) -> int:
    """returns an integer"""
    result = 0
    current = 2

    if n <= 1:
        return 0

    while (n > 1):
        while (n % current == 0):
            result += current
            n /= current

        current += 1

    return result
