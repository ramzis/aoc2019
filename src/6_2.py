#!/usr/bin/env python3

from task import Task
from collections import defaultdict


class Solution(Task):

    def parse_line(self, line):
        return tuple(line.strip().split(")"))

    def test_data(self):
        return []

    def solve(self, data):

        solution = 0

        d = defaultdict(list)
        s = set()

        for o in data:
            a, b = o
            d[a] += [b]
            s.add(a)
            s.add(b)

        targets = []
        q = [("COM", 0, ["COM"])]
        while q:
            val = q.pop()
            q += [(v, val[1] + 1, val[2] + [v]) for v in d[val[0]]]
            if val[0] in s:
                if val[0] in ["SAN", "YOU"]:
                    targets.append(val[2])
                s.remove(val[0])

        targets.sort(key=len)
        common = ""
        for x in targets[0]:
            if x in targets[1]:
                common = x

        solution = len(targets[0][targets[0].index(common):]) + \
            len(targets[1][targets[1].index(common):]) - 4

        return solution

Solution(__file__)
