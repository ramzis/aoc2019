#!/usr/bin/env python3

import os
import re
from collections import defaultdict


class Task:

    input_dir = '../input'
    output_dir = '../output'

    def __init__(self, caller):

        self.day, self.part = os.path.basename(
            caller).split('.')[0].split('_')
        self.data = []
        self.solution = None
        self.input = '{}/{}.txt'.format(self.input_dir, self.day)

        test_data = self.test_data()
        self.test(test_data)
        data = self.read_data()
        self.solution = self.solve(data)
        self.write_solution()
        print(self.solution)

    def write_solution(self):
        f = open('{}/{}_{}.txt'.format(self.output_dir, self.day, self.part),
                 'wt', encoding='utf-8')
        f.write(str(self.solution) + '\n')

    def test(self, test_data):
        for (data, expected) in test_data:
            data = list(map(self.parse_line, data))
            actual = self.solve(data)
            assert(actual == expected)

    def solve(self, data):
        pass

    def read_data(self):
        data = []
        with open(self.input) as f:
            for line in f:
                data.append(self.parse_line(line))
        return data

    def test_data(self):
        return []

    def parse_line(self, line):
        return line.strip()
