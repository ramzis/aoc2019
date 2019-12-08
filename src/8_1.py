#!/usr/bin/env python3

from task import Task
from collections import Counter


class Solution(Task):

    def parse_line(self, line):
        return line.strip()

    def test_data(self):
        return [(["123456789012", "3 2"], 1),
                (["111222000000", "3 2"], 9)]

    def solve(self, data):

        solution = 0

        if len(data) > 1:
            x, y = data[1].split(" ")
            x, y = int(x), int(y)
        else:
            x, y = 25, 6

        slice_size = x * y
        slices = [data[0][i:i + slice_size]
                  for i in range(0, len(data[0]), slice_size)]
        cs = map(lambda l: Counter(l), slices)
        m = min(cs, key=lambda c: c['0'])
        solution = m['1'] * m['2']

        return solution

Solution(__file__)
