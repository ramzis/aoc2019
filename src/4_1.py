#!/usr/bin/env python3

from task import Task


class Solution(Task):

    def parse_line(self, line):
        return line.strip()

    def test_data(self):
        return [
            (["111111", "111111"], 1),
            (["223450", "223450"], 0),
            (["123789", "123789"], 0)
        ]

    def solve(self, data):

        def valid(number):
            steps = 5
            double = False
            for i in range(steps):
                d = int(number[i + 1]) - int(number[i])
                if d < 0:
                    return False
                if d == 0:
                    double = True
            return double

        solution = 0

        low = int(data[0])
        high = int(data[1])

        solution = len([n for n in range(low, high + 1) if valid(str(n))])

        return solution

Solution(__file__)
