#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.

    Bugs: none known
 

    Author: Alessandro Bedini alle.bedo@gmail.com

    Date Created: 11/12/2022
"""

from contextlib import redirect_stdout
from io import StringIO
from math import floor
from typing import List, Tuple
 

FILE_PATH = "2022/Bedo/resources/AoC_11.txt"

class Monkey(object):


    def __init__(self, input: List[str]) -> None:
        self.__id = input[0].replace(":","").split()[1]
        self.__count = 0
        self.__objects = [int(x) for x in input[1][input[1].find(":") + 2:].split(",")]
        self.__operation = "print(" + input[2][input[2].find("=") + 2:].strip() + ")"
        self.__test = int(input[3].split()[-1])
        self.__true = int(input[4].split()[-1])
        self.__false = int(input[5].split()[-1])

    @property
    def id(self):
        return self.__id

    @property
    def count(self):
        return self.__count

    @property
    def objects(self):
        return self.__objects
    @property
    def operation(self):
        return self.__operation

    @property
    def test(self):
        return self.__test

    @property
    def true(self):
        return self.__true

    @property
    def false(self):
        return self.__false

    def increase_count(self) -> None:
        self.__count += 1

    def calculate_new_level(self, old: int) -> int:
        f = StringIO()
        with redirect_stdout(f):
            exec(self.__operation)
        return int(f.getvalue())

    def test_worry_level(self, worry_level: int) -> int:
        if worry_level % self.__test == 0:
            return self.__true
        else:
            return self.__false

    def do_the_turn(self) -> List[Tuple[int, int]]:
        moves = []
        for object in self.__objects:
            new = floor(self.calculate_new_level(object) / 3)
            self.__objects[self.__objects.index(object)] = new
            dest = self.test_worry_level(new)
            moves.append([new, dest])
            self.increase_count()
        return moves

        

if __name__ == "__main__":

    monkeys = []
    total_count = []

    with open(FILE_PATH, "r") as file:
        lines = file.readlines()

    for line in lines:
        if "Monkey" in line:
            monkeys.append(Monkey(lines[lines.index(line):lines.index(line) + 6]))

    for round in range(20):
        for monkey in monkeys:
            moves = monkey.do_the_turn()
            for move in moves:
                monkeys[move[1]].objects.append(monkey.objects.pop(monkey.objects.index(move[0])))

    for monkey in monkeys:
        total_count.append(monkey.count)

    total_count = sorted(total_count, reverse=True)
    print(total_count[0]*total_count[1])