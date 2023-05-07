#!/usr/bin/python3

"""interview preparations - minimum operations"""

def min_Operations(n):
    """Returns the smallests number of operations (Copy All and Paste)
    needed to result in exactly n H
    characters in this file.

    Args:
    n (int): number of H characters desired

    Returns: number of operations
    """

    i = 0
    pasted_H = 1
    clipboard = 0

    while pasted_H < n:
        if clipboard == 0:
            clipboard = pasted_H
            i += 1

        if pasted_H == 1:
            pasted_H += clipboard
            i += 1
            continue

        remainder = n - pasted_H

        if remainder < clipboard:
            return 0

        if remainder % pasted_H != 0:
            pasted_H += clipboard
            i += 1
        else:
            clipboard = pasted_H
            pasted_H += clipboard
            i += 2

    if pasted_H == n:
        return i
    else:
        return 0

