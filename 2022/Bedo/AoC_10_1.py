#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.

    Bugs: none known
 

    Author: Alessandro Bedini alle.bedo@gmail.com

    Date Created: 11/12/2022
"""

from typing import List
 

FILE_PATH = "2022/Bedo/resources/AoC_10.txt"
strengths_list = []

def check_signal_strenght():
    if cycle == 20 or (cycle - 20) % 40 == 0:
        strengths_list.append(cycle*X)

if __name__ == "__main__":

    cycle = 1
    X = 1

    with open(FILE_PATH, "r") as file:
        for line in file:
            if line.strip().split()[0] == "noop":
                check_signal_strenght()
                cycle += 1
            else:
                for i in range(2):
                    check_signal_strenght()
                    cycle += 1
                X += int(line.strip().split()[1])
    
    print(sum(strengths_list))