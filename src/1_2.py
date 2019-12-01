#!/usr/bin/env python3

from task import Task


class Solution(Task):

    def parse_line(self, line):
        return int(line.strip())

    def test_data(self):
        return [
            (["14"], 2),
            (["1969"], 966),
            (["100756"], 50346)
        ]

    def solve(self, data):

        def fuel(mass):
            d = 3
            s = 2
            f = mass // d - s
            if f > 0:
                return f + fuel(f)
            else:
                return 0

        solution = 0

        for mass in data:
            solution += fuel(mass)

        return solution

Solution(__file__)
