#!/usr/bin/python3
"""log parsing"""


import sys

total_file_size = 0
lines_by_status_code = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        if i % 10 == 0:
            print("File size:", total_file_size)
            for status_code in sorted(lines_by_status_code):
                print(f"{status_code}: {lines_by_status_code[status_code]}")
            print()

        line = line.strip()
        parts = line.split()
        if len(parts) != 7:
            continue

        _, _, _, _, status_code, file_size = parts

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        total_file_size += file_size
        lines_by_status_code[status_code] = lines_by_status_code.get(status_code, 0) + 1

except KeyboardInterrupt:
    pass

print("File size:", total_file_size)
for status_code in sorted(lines_by_status_code):
    print(f"{status_code}: {lines_by_status_code[status_code]}")
