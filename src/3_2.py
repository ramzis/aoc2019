#!/usr/bin/env python3

from task import Task
from collections import defaultdict


class Solution(Task):

    def parse_line(self, line):
        return [(x[0], int(x[1:])) for x in line.strip().split(",")]

    def test_data(self):
        return [
            (["R8,U5,L5,D3",
              "U7,R6,D4,L4"], 30),
            (["R75,D30,R83,U83,L12,D49,R71,U7,L72",
              "U62,R66,U55,R34,D71,R55,D58,R83"], 610),
            (["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
              "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"], 410)
        ]

    def solve(self, data):

        solution = 0

        def get_vector(dir):
            assert(type(dir) == tuple)
            if dir[0] == 'R':
                vector = (1, 0)
            elif dir[0] == 'L':
                vector = (-1, 0)
            elif dir[0] == 'U':
                vector = (0, 1)
            else:  # dir[0] == 'D'
                vector = (0, -1)
            return vector

        m = defaultdict(list)
        port = (0, 0)

        for wire_id, wire_path in enumerate(data):
            pos = tuple(port)
            steps = 0
            for point in wire_path:
                dir = get_vector(point)
                for step in range(point[1]):
                    steps += 1
                    pos = (pos[0] + dir[0], pos[1] + dir[1])
                    if wire_id not in [id for (id, _) in m[pos]]:
                        m[pos].append((wire_id, steps))

        solution = min([sum([step for (_, step) in wires])
                        for point, wires in m.items() if len(wires) > 1])

        return solution

Solution(__file__)
