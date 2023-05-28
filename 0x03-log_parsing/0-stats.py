#!/usr/bin/python3
"""log parsing"""
import sys
from collections import defaultdict

# Initialize variables
total_size = 0
status_codes = defaultdict(int)
line_count = 0

try:
    # Read input lines from stdin
    for line in sys.stdin:
        line = line.strip()
        # Check if the line matches the expected input format
        if line.startswith("[") and line.endswith("]"):
            parts = line.split()
            ip_address = parts[0]
            status_code = parts[-2]
            file_size = parts[-1]

            # Update metrics
            total_size += int(file_size)
            status_codes[status_code] += 1
            line_count += 1

        # Check if we reached 10 lines or a keyboard interruption (CTRL + C)
        if line_count == 10:
            # Print metrics
            print("Total file size:", total_size)
            for code in sorted(status_codes.keys()):
                print(code + ":", status_codes[code])
            print()

            # Reset variables
            status_codes = defaultdict(int)
            line_count = 0

except KeyboardInterrupt:
    # If interrupted, print the metrics for the processed lines
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(code + ":", status_codes[code])

