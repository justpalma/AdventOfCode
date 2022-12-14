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
head_position = [0,0]
tail_position = [0,0]

def calculate_tail_positon():
    dif = (head_position[0] - tail_position[0], head_position[1] - tail_position[1])
    if dif[0] > 1:
        tail_position[0] += 1
        tail_position[1] += dif[1]
    if dif[0] < -1:
        tail_position[0] -= 1
        tail_position[1] += dif[1]
    if dif[1] > 1:
        tail_position[0] += dif[0]
        tail_position[1] += 1
    if dif[1] < -1:
        tail_position[0] += dif[0]
        tail_position[1] -= 1
    position_list.append(tuple(tail_position))


if __name__ == "__main__":


    with open(FILE_PATH, "r") as file:
        for line in file:
            direction = line.strip().split()[0]
            moves = int(line.strip().split()[1])
            if direction == "U":
                for i in range(moves):
                    head_position[0] += 1
                    calculate_tail_positon()
            if direction == "D":
                for i in range(moves):
                    head_position[0] -= 1
                    calculate_tail_positon()
            if direction == "R":
                for i in range(moves):
                    head_position[1] += 1
                    calculate_tail_positon()
            if direction == "L":
                for i in range(moves):
                    head_position[1] -= 1
                    calculate_tail_positon()

    print(len(set(position_list)))