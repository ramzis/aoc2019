#!/usr/bin/env python3

from task import Task
from itertools import permutations


class Solution(Task):

    def parse_line(self, line):
        return list(map(int, (line.strip().split(','))))

    def test_data(self):
        return [(["3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"], 139629729),
                (["3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"], 18216)]

    def solve(self, data):

        solution = 0

        class Computer():

            def __init__(self, data):
                self.input_stream = []
                self.output_stream = []
                self.d = {k: v for k, v in enumerate(data[0])}
                self.ip = 0
                self.running = True

            def provide_input(self, input):
                self.input_stream.append(input)

            def read_output(self):
                return self.output_stream.pop(0) if self.output_stream else None

            def is_running(self):
                return self.running

            def process(self):

                while self.running:

                    cmd = self.d[self.ip]

                    opcode = cmd % 100

                    if opcode == 1:
                        cmd = cmd // 100
                        mode_a = cmd % 10
                        cmd = cmd // 10
                        mode_b = cmd % 10
                        a = self.d[
                            self.ip + 1] if mode_a else self.d[self.d[self.ip + 1]]
                        b = self.d[
                            self.ip + 2] if mode_b else self.d[self.d[self.ip + 2]]
                        c = self.d[self.ip + 3]
                        self.d[c] = a + b
                        self.ip += 4
                    elif opcode == 2:
                        cmd = cmd // 100
                        mode_a = cmd % 10
                        cmd = cmd // 10
                        mode_b = cmd % 10
                        a = self.d[
                            self.ip + 1] if mode_a else self.d[self.d[self.ip + 1]]
                        b = self.d[
                            self.ip + 2] if mode_b else self.d[self.d[self.ip + 2]]
                        c = self.d[self.ip + 3]
                        self.d[c] = a * b
                        self.ip += 4
                    elif opcode == 5:
                        cmd = cmd // 100
                        mode_a = cmd % 10
                        cmd = cmd // 10
                        mode_b = cmd % 10
                        a = self.d[
                            self.ip + 1] if mode_a else self.d[self.d[self.ip + 1]]
                        b = self.d[
                            self.ip + 2] if mode_b else self.d[self.d[self.ip + 2]]
                        if a > 0:
                            self.ip = b
                        else:
                            self.ip += 3
                    elif opcode == 6:
                        cmd = cmd // 100
                        mode_a = cmd % 10
                        cmd = cmd // 10
                        mode_b = cmd % 10
                        a = self.d[
                            self.ip + 1] if mode_a else self.d[self.d[self.ip + 1]]
                        b = self.d[
                            self.ip + 2] if mode_b else self.d[self.d[self.ip + 2]]
                        c = self.d[self.ip + 3]
                        if a == 0:
                            self.ip = b
                        else:
                            self.ip += 3
                    elif opcode == 7:
                        cmd = cmd // 100
                        mode_a = cmd % 10
                        cmd = cmd // 10
                        mode_b = cmd % 10
                        a = self.d[
                            self.ip + 1] if mode_a else self.d[self.d[self.ip + 1]]
                        b = self.d[
                            self.ip + 2] if mode_b else self.d[self.d[self.ip + 2]]
                        c = self.d[self.ip + 3]
                        self.d[c] = 1 if a < b else 0
                        self.ip += 4
                    elif opcode == 8:
                        cmd = cmd // 100
                        mode_a = cmd % 10
                        cmd = cmd // 10
                        mode_b = cmd % 10
                        a = self.d[
                            self.ip + 1] if mode_a else self.d[self.d[self.ip + 1]]
                        b = self.d[
                            self.ip + 2] if mode_b else self.d[self.d[self.ip + 2]]
                        c = self.d[self.ip + 3]
                        self.d[c] = 1 if a == b else 0
                        self.ip += 4
                    elif opcode == 3:
                        a = self.d[self.ip + 1]
                        if self.input_stream:
                            self.d[a] = self.input_stream.pop(0)
                            self.ip += 2
                        else:
                            break
                    elif opcode == 4:
                        a = self.d[self.ip + 1]
                        self.output_stream.append(self.d[a])
                        self.ip += 2
                    elif opcode == 99:
                        self.running = False
                        break
                    else:
                        print("Bad command")
                        self.running = False
                        break

        # (Permutation, signal)
        results = []
        ps = permutations(range(5, 10))
        for p in list(ps):

            cs = []
            for c in range(5):
                cs.append(Computer(data))

            for idx, c in enumerate(cs):
                c.provide_input(p[idx])
            cs[0].provide_input(0)

            while cs[-1].is_running():

                for idx, c in enumerate(cs):
                    if c.is_running():
                        prev = (idx - 1) % len(cs)
                        o = cs[prev].read_output()
                        if o != None:
                            c.provide_input(o)
                        c.process()

            results.append((p, cs[-1].read_output()))

        solution = max(results, key=lambda x: x[1])[1]
        return solution

Solution(__file__)
