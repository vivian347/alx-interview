#!/usr/bin/env python3
import sys
import re

format = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[[^\]]+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
total_size = 0
status_code_count = {200: 0, 301: 0, 400: 0,
                     401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin):
        line = line.strip()

        if not re.match(format, line):
            continue

        match = re.search(format, line)
        status_code = int(match.group(1))
        file_size = int(match.group(2))

        total_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1

        if (i + 1) % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_code_count.items()):
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code, count in sorted(status_code_count.items()):
        if count > 0:
            print("{}: {}".format(code, count))
