#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.

    Bugs: none known
 

    Author: Alessandro Bedini alle.bedo@gmail.com

    Date Created: 11/12/2022
"""

from typing import List
 

FILE_PATH = "2022/Bedo/resources/AoC_8.txt"

def check_visibility(r: int, c: int, gird: List[List[str]]) -> bool:
    north = True
    south = True
    west = True
    east = True

    for i in range(r):
        if grid[i][c] >= gird[r][c]:
            north = False
    for i in range(r + 1, len(grid)):
        if grid[i][c] >= gird[r][c]:
            south = False
    for i in range(c):
        if grid[r][i] >= gird[r][c]:
            west = False
    for i in range(c + 1, len(grid[0])):
        if grid[r][i] >= gird[r][c]:
            east = False

    return True if north or south or west or east else False


if __name__ == "__main__":

    grid = []

    with open(FILE_PATH, 'r') as file:
        for line in file:
            grid.append([int(c) for c in line.strip()])


    visible_tree = (len(grid) * 2) + (len(grid[0]) * 2 - 4) 

    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if check_visibility(r, c, grid):
                visible_tree += 1

    print(visible_tree)