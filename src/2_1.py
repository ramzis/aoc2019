#!/usr/bin/env python3

from task import Task


class Solution(Task):

    def parse_line(self, line):
        return list(map(int, (line.strip().split(','))))

    def test_data(self):
        return [
            (["1,0,0,0,99"], 2),
            (["2,3,0,3,99"], 2),
            (["2,4,4,5,99,0"], 2),
            (["1,1,1,4,99,5,6,0,99"], 30),
        ]

    def solve(self, data):

        solution = 0

        result_pos = 0

        d = {k: v for k, v in enumerate(data[0])}

        ip = 0

        while True:
            opcode = d[ip]

            if opcode == 1:
                a = d[ip + 1]
                b = d[ip + 2]
                c = d[ip + 3]
                d[c] = d[a] + d[b]
                ip += 4
            elif opcode == 2:
                a = d[ip + 1]
                b = d[ip + 2]
                c = d[ip + 3]
                d[c] = d[a] * d[b]
                ip += 4
            elif opcode == 99:
                break
            else:
                break

        solution = d[result_pos]

        return solution

Solution(__file__)
