#!/usr/bin/python3
"""This module contains the pascal_triangle function"""


def pascal_triangle(n):
    """prints the pascal triangle of n
    Args:
    n (int): the number whose pascal triangle is to be printed
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while (len(triangle) != n):
        list_ = triangle[-1]
        item = [1]
        for i in range(len(list_) - 1):
            item.append(list_[i] + list_[i + 1])
        item.append(1)
        triangle.append(item)

    return triangle
