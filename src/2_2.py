#!/usr/bin/env python3

from task import Task


class Solution(Task):

    def parse_line(self, line):
        return list(map(int, (line.strip().split(','))))

    def test_data(self):
        return [
        ]

    def solve(self, data):

        solution = 0

        result_pos = 0
        noun_pos = 1
        verb_pos = 2

        found = False

        for noun in range(100):
            if found:
                break
            for verb in range(100):

                d = {k: v for k, v in enumerate(data[0])}
                d[noun_pos] = noun
                d[verb_pos] = verb
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

                if d[result_pos] == 19690720:
                    found = True
                    solution = 100 * d[noun_pos] + d[verb_pos]
                    break

        return solution

Solution(__file__)
