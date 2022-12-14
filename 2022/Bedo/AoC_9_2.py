#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.

    Bugs: none known
 

    Author: Alessandro Bedini alle.bedo@gmail.com

    Date Created: 11/12/2022
"""

from typing import List
 

FILE_PATH = "2022/Bedo/resources/AoC_9.txt"
position_list = [(0,0)]
rope_position = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

def calculate_tail_positon():
    for i in range(1,10):
        dif = (rope_position[i - 1][0] - rope_position[i][0], rope_position[i - 1][1] - rope_position[i][1])
        if dif[0] > 1 and dif[1] > 1:
            rope_position[i][0] += 1
            rope_position[i][1] += 1
        elif dif[0] > 1 and dif[1] < -1:
            rope_position[i][0] += 1
            rope_position[i][1] -= 1
        elif dif[0] < -1 and dif[1] > 1:
            rope_position[i][0] -= 1
            rope_position[i][1] += 1
        elif dif[0] < -1 and dif[1] < -1:
            rope_position[i][0] -= 1
            rope_position[i][1] -= 1
        elif dif[0] > 1:
            rope_position[i][0] += 1
            rope_position[i][1] += dif[1]
        elif dif[0] < -1:
            rope_position[i][0] -= 1
            rope_position[i][1] += dif[1]
        elif dif[1] > 1:
            rope_position[i][0] += dif[0]
            rope_position[i][1] += 1
        elif dif[1] < -1:
            rope_position[i][0] += dif[0]
            rope_position[i][1] -= 1
        position_list.append(tuple(rope_position[9]))


if __name__ == "__main__":


    with open(FILE_PATH, "r") as file:
        for line in file:
            direction = line.strip().split()[0]
            moves = int(line.strip().split()[1])
            if direction == "U":
                for i in range(moves):
                    rope_position[0][0] += 1
                    calculate_tail_positon()
            if direction == "D":
                for i in range(moves):
                    rope_position[0][0] -= 1
                    calculate_tail_positon()
            if direction == "R":
                for i in range(moves):
                    rope_position[0][1] += 1
                    calculate_tail_positon()
            if direction == "L":
                for i in range(moves):
                    rope_position[0][1] -= 1
                    calculate_tail_positon()

    print(len(set(position_list)))