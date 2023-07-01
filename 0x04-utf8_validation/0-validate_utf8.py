#!/usr/bin/python3
"""validUTF8 method"""


def validUTF8(data):
    """
    This method determines if a given data set
    represents a valid UTF-8 encoding

    Arguments:
    data (list of integers): The data to be checked

    Return: True or False
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                continue

            num_bytes = num_bytes_from_mask(byte)

            if num_bytes == 0 or num_bytes > 4:
                return False

        else:
            if byte >> 6 != 0b10:
                return False

        num_bytes -= 1

    return num_bytes == 0


def num_bytes_from_mask(byte):
    """Get the number of bytes needed to represent a character based on the first byte mask"""
    masks = [0b1111110, 0b111110, 0b11110, 0b1110]
    for i, mask in enumerate(masks):
        if byte >> (7 - i) == mask:
            return i + 1
    return 0
