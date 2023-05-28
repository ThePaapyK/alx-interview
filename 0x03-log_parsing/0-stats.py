#!/usr/bin/python3

"""
This module provides functionality to compute and
print metrics based on input data.

It reads input from stdin line by line,
computes statistics, and prints the results.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C),
it prints the following statistics:
- Total file size: the sum of all previous file sizes
- Number of lines by status code: counts the occurrences of each status code

Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500

The module uses the `print_stats()` function to print the statistics and
a dictionary `status_codes` to keep track of the counts for each status code.

Usage:
    $ python3 <module_name.py>

Author: Paa Kojo Effah Annan
"""
import sys
from collections import defaultdict


def print_stats(status_dict, total_size):
    """Prints the computed statistics.

    Args:
        status_dict (dict): Dictionary containing
        the count of lines per status code.

        total_size (int): Total file size computed from the input.

     Prints:
        File size: Total size of all files processed.
        <status code>: Number of lines with the respective status code.
    """
    print(f"File size: {total_size}")
    for status_code, count in sorted(status_dict.items()):
        if count != 0:
            print(f"{status_code}: {count}")


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

count = 0
total_size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_stats(status_codes, total_size)

        parts = line.split()
        count += 1

        try:
            file_size = int(parts[-1])
            total_size += file_size
        except ValueError:
            pass

        try:
            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        except IndexError:
            pass

    print_stats(status_codes, total_size)

except KeyboardInterrupt:
    print_stats(status_codes, total_size)
    raise
