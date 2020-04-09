# -*- coding: utf-8 -*-
import os
import os.path as path
import sys
import gzip
import matplotlib.pyplot as pyplot
from collections import defaultdict


def run():
    logs_path = sys.argv[1]
    log_files = [path.join(logs_path, f) for f in os.listdir(logs_path) if path.isfile(path.join(logs_path, f))]
    for log_file_path in log_files:
        counts = defaultdict(lambda: 0)
        with gzip.open(log_file_path, 'rt') as log_file:
            for line in log_file:
                if not line:
                    break
                if not is_incoming(line):
                    continue
                incoming_ip = parse_incoming_ip_address(line)
                counts[incoming_ip] += 1
        print(counts)
        show_pie_chart(counts)


def parse_incoming_ip_address(line):
    return line[line.find("From") + 5:].split(' ')[0]


def is_incoming(log_record):
    return "From" in log_record


def show_pie_chart(counts):
    pyplot.pie([int(count) for count in counts.values()],
               labels=[str(count) for count in counts.values()])
    pyplot.legend(counts.keys(), loc=3)
    pyplot.show()


# Run IT!
if __name__ == "__main__":
    run()
