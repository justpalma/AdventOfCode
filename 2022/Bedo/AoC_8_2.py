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

def count_tree_visibility(r: int, c: int, gird: List[List[str]]) -> int:
    north = 0
    south = 0
    west = 0
    east = 0

    for i in range(r - 1, -1, -1):
        if grid[i][c] < gird[r][c]:
            north += 1
        else:
            north += 1
            break
    for i in range(r + 1, len(grid)):
        if grid[i][c] < gird[r][c]:
            south += 1
        else:
            south += 1
            break
    for i in range(c - 1, -1, -1):
        if grid[r][i] < gird[r][c]:
            west += 1
        else:
            west += 1
            break
    for i in range(c + 1, len(grid[0])):
        if grid[r][i] < gird[r][c]:
            east += 1
        else:
            east += 1
            break

    return north * south * west * east 


if __name__ == "__main__":

    grid = []

    with open(FILE_PATH, 'r') as file:
        for line in file:
            grid.append([int(c) for c in line.strip()])


    max_visible_tree = 0 

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            cur =  count_tree_visibility(r, c, grid)
            if cur > max_visible_tree:
                max_visible_tree = cur

    print(max_visible_tree)