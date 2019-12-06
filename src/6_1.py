#!/usr/bin/env python3

from task import Task
from collections import defaultdict


class Solution(Task):

    def parse_line(self, line):
        return tuple(line.strip().split(")"))

    def test_data(self):
        return [(
            ["COM)B",
             "B)C",
             "C)D",
             "D)E",
             "E)F",
             "B)G",
             "G)H",
             "D)I",
             "E)J",
             "J)K",
             "K)L"], 42)]

    def solve(self, data):

        solution = 0

        d = defaultdict(list)
        s = set()

        for o in data:
            a, b = o
            d[a] += [b]
            s.add(a)
            s.add(b)

        q = [("COM", 0)]
        while q:
            val = q.pop()
            q += [(v, val[1] + 1) for v in d[val[0]]]
            if val[0] in s:
                solution += val[1]
                s.remove(val[0])

        return solution

Solution(__file__)
