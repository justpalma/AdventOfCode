#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.

    Bugs: none known
 

    Author: Alessandro Bedini alle.bedo@gmail.com

    Date Created: 11/12/2022
"""
 
from typing import List

FILE_PATH = "2022/Bedo/resources/AoC_7.txt"

def check_command(lines: List[str], fs: dict):
    try:
        while True:
            line = lines.pop(0)
            if line.strip() == "$ ls":
                check_dir(lines, fs)
            if line.strip() == "$ cd ..":
                return
            if "$ cd" in line.strip():
                check_command(lines, fs[line.strip().split()[2]])
    except Exception:
        return


def check_dir(lines: List[str], fs: dict):
        lines = iter(lines)
        line = next(lines)
        while line[0] != "$":
            if line.strip().split()[0] == "dir":
                fs.update({line.strip().split()[1]: {}})
            else:
                fs.update({line.strip().split()[1]:line.strip().split()[0]})
            line = next(lines)

def check_size(fs: dict, dirs: list):
    size = 0
    for k in fs.keys():
        if isinstance(fs.get(k), dict):
            dirs.append(check_size(fs.get(k), dirs))
            size += int(dirs[len(dirs) - 1])
        else:
            size += int(fs.get(k))
    return size

if __name__ == "__main__":

    fs = {"/": {}}
    dirs = []

    with open(FILE_PATH, 'r') as file:
        lines = file.readlines()

    check_command(lines[1:], fs["/"])

    check_size(fs, dirs)

    sum = 0

    for value in dirs:
        if int(value) <= 100000:
            sum += int(value)

    print(sum)