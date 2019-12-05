#!/usr/bin/env python3

from task import Task


class Solution(Task):

    def parse_line(self, line):
        return list(map(int, (line.strip().split(','))))

    def test_data(self):
        return [(["3,0,4,0,99"], 1)]

    def solve(self, data):

        solution = 0

        input_stream = [1]
        output_stream = []
        d = {k: v for k, v in enumerate(data[0])}
        ip = 0

        while True:
            cmd = d[ip]

            opcode = cmd % 100

            if opcode == 1:
                cmd = cmd // 100
                mode_a = cmd % 10
                cmd = cmd // 10
                mode_b = cmd % 10
                a = d[ip + 1] if mode_a else d[d[ip + 1]]
                b = d[ip + 2] if mode_b else d[d[ip + 2]]
                c = d[ip + 3]
                d[c] = a + b
                ip += 4
            elif opcode == 2:
                cmd = cmd // 100
                mode_a = cmd % 10
                cmd = cmd // 10
                mode_b = cmd % 10
                a = d[ip + 1] if mode_a else d[d[ip + 1]]
                b = d[ip + 2] if mode_b else d[d[ip + 2]]
                c = d[ip + 3]
                d[c] = a * b
                ip += 4
            elif opcode == 3:
                a = d[ip + 1]
                d[a] = input_stream.pop(0)
                ip += 2
            elif opcode == 4:
                a = d[ip + 1]
                output_stream.append(d[a])
                ip += 2
            elif opcode == 99:
                break
            else:
                break

        if output_stream:
            solution = output_stream[-1]

        return solution

Solution(__file__)
