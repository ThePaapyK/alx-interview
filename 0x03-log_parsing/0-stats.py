#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics"""

import sys


def print_metrics(metrics_dict, total_size):
    """
    Prints the metrics information.

    Args:
        metrics_dict (dict): A dictionary containing
        the metrics as key-value pairs.
        total_size (int): The total file size.

    Returns:
        None
    """
    print("File size: {:d}".format(total_size))
    for key in sorted(metrics_dict.keys()):
        if metrics_dict[key] != 0:
            print("{}: {:d}".format(key, metrics_dict[key]))


metrics = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
           "404": 0, "405": 0, "500": 0}

line_count = 0
total_size = 0

try:
    for line in sys.stdin:
        line_count += 1

        if line_count != 0 and line_count % 10 == 0:
            print_metrics(metrics, total_size)

        line_split = line.split()

        try:
            total_size += int(line_split[-1])
        except:
            pass

        try:
            if line_split[-2] in metrics:
                metrics[line_split[-2]] += 1
        except:
            pass

    print_metrics(metrics, total_size)

except KeyboardInterrupt:
    print_metrics(metrics, total_size)
    raise
