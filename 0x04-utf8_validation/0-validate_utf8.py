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
            if (byte >> 7) == 0b0:
                # Single-byte character
                continue
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                # Invalid first byte
                return False
        else:
            if (byte >> 6) != 0b10:
                # Invalid continuation byte
                return False
            num_bytes -= 1

    # Check if there are any unfinished characters
    return num_bytes == 0

