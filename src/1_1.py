#!/usr/bin/env python3

from task import Task


class Solution(Task):

    def parse_line(self, line):
        return int(line.strip())

    def test_data(self):
        return [
            (["12"], 2),
            (["14"], 2),
            (["1969"], 654),
            (["100756"], 33583)
        ]

    def solve(self, data):

        def fuel(mass):
            d = 3
            s = 2
            return mass // d - s

        solution = 0

        for mass in data:
            solution += fuel(mass)

        return solution

Solution(__file__)
