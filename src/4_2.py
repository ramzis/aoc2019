#!/usr/bin/env python3

from task import Task


class Solution(Task):

    def parse_line(self, line):
        return line.strip()

    def test_data(self):
        return [
            (["112233", "112233"], 1),
            (["123444", "123444"], 0),
            (["111122", "111122"], 1),
            (["111111", "111111"], 0)
        ]

    def solve(self, data):

        def valid(number):
            steps = 5
            double = False
            repeating = 0
            for i in range(steps):
                a, b = int(number[i]), int(number[i + 1])
                d = b - a
                if d < 0:
                    return False
                if a == b:
                    repeating += 1
                    if i == 4 and repeating == 1:
                        double = True
                else:
                    if repeating == 1:
                        double = True
                    repeating = 0
            return double

        solution = 0

        low = int(data[0])
        high = int(data[1])

        solution = len([n for n in range(low, high + 1) if valid(str(n))])

        return solution

Solution(__file__)
