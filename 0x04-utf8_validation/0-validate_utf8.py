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

    for num in data:
        binary = bin(num)[2:].zfill(8)  #Convert decimal to 8-bit binary string
        if num_bytes == 0:
            if binary[0] == '0':
                # Single-byte character
                continue
            elif binary[:3] == '110':
                num_bytes = 1
            elif binary[:4] == '1110':
                num_bytes = 2
            elif binary[:5] == '11110':
                num_bytes = 3
            else:
                # Invalid first byte
                return False
        else:
            if binary[:2] != '10':
                # Invalid continuation byte
                return False
            num_bytes -= 1

    # Check if there are any unfinished characters
    return num_bytes == 0
