#!/usr/bin/python3
"""print dome stats"""

import sys


def print_stats(code_count, total_size):
    """
    Prints statistics about HTTP status codes and total file size.
    Args:
        code_count: a dictionary of status codes and their counts
        total_size: the total size of the file
    Returns:
        None
    """

    print("File size:", total_size)
    for code, count in sorted(code_count.items()):
        if count != 0:
            print(code + ":", count)


def process_lines(lines):
    """
    Process the lines from standard input and update statistics.
    Args:
        lines: a list of lines from standard input
    Returns:
        total_size: updated total file size
        code_count: updated dictionary of status codes and their counts
    """
    total_size = 0
    code_count = {"200": 0,
                  "301": 0,
                  "400": 0,
                  "401": 0,
                  "403": 0,
                  "404": 0,
                  "405": 0,
                  "500": 0}

    for line in lines:
        parsed_line = line.split()  # split line into fields
        parsed_line = parsed_line[::-1]  # reverse the order of fields

        if len(parsed_line) > 2:
            total_size += int(parsed_line[0])  # add file size to total
            code = parsed_line[1]  # get status code

            if code in code_count:
                code_count[code] += 1  # increment count for status code

    return total_size, code_count


def process_input():
    """
    Read lines from standard input and process them in batches.
    """
    counter = 0
    batch_size = 10
    lines = []

    try:
        for line in sys.stdin:
            counter += 1
            lines.append(line.strip())

            if counter == batch_size:
                total_size, code_count = process_lines(lines)  # process batch
                print_stats(code_count, total_size)  # print stats for batch
                counter = 0
                lines = []

    finally:
        total_size, code_count = process_lines(lines)  # process remaining lines
        print_stats(code_count, total_size)  # print final stats


if __name__ == '__main__':
    process_input()
