#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.

    Bugs: none known
 

    Author: Alessandro Bedini alle.bedo@gmail.com

    Date Created: 05/12/2022
"""
 

FILE_PATH = "2022/Bedo/resources/AoC_5.txt"


def separates(lines):
    for line in lines:
        if not line.strip():
            return lines[:lines.index(line)], lines[lines.index(line) + 1:]
 

def get_stacks_number(lines):
    for line in lines:
        line = line.strip().replace(" ", "")
        if line[0] == "1":
            return len(line)
 

def get_stacks(lines):
    stacks = []
    for i in range(get_stacks_number(lines)):
        stacks.append([])
    for line in lines:
        line = line.replace('[', '').replace(']', '').replace('    ', '0').replace(' ', '').replace('\n', '')
        if line[0] == '1':
            break
        index = 0
        for c in line:
            if c != '0':
                stacks[index].insert(0, c)
            index += 1
    return stacks


if __name__ == "__main__": 

    with open(FILE_PATH, 'r') as file:
        lines = file.readlines()
    
    input, moves = separates(lines)

    stacks = get_stacks(input)

    for move in moves:
        split = move.split()
        stacks[int(split[5]) - 1].extend(stacks[int(split[3]) - 1][-int(split[1]):])
        stacks[int(split[3]) - 1] = stacks[int(split[3]) - 1][:-int(split[1])]

    for stack in stacks:
        print(stack.pop())