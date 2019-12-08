#!/usr/bin/env python3

from task import Task
from collections import Counter


class Solution(Task):

    def parse_line(self, line):
        return line.strip()

    def test_data(self):
        return []

    def solve(self, data):

        x, y = 25, 6

        slice_size = x * y

        solution = "0" * slice_size

        slices = [data[0][i:i + slice_size]
                  for i in range(0, len(data[0]), slice_size)]

        def flatten(a, b):
            # a-bottom b-top
            return "".join([j if j != '2' else i for i, j in zip(a, b)])

        for s in reversed(slices):
            solution = flatten(solution, s)

        key = {"0": "█", "1": "░", "2": " "}
        solution = "".join(map(lambda x: key[x], solution))

        solution = "".join([solution[i:i + x] + "\n"
                            for i in range(0, slice_size, x)])

        return solution

Solution(__file__)
