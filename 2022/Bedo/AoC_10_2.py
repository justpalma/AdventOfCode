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
screen = []

def check_signal_strenght():
    if cycle < 41 and cycle in [X -1, X, X + 1]:
        screen.append("#")
    elif cycle < 81 and cycle - 40 in [X -1, X, X + 1]:
        screen.append("#")
    elif cycle < 121 and cycle - 80 in [X -1, X, X + 1]:
        screen.append("#")
    elif cycle < 161 and cycle - 120 in [X -1, X, X + 1]:
        screen.append("#")
    elif cycle < 201 and cycle - 160 in [X -1, X, X + 1]:
        screen.append("#")
    elif cycle < 241 and cycle - 200 in [X -1, X, X + 1]:
        screen.append("#")
    else:
        screen.append(".")
        

if __name__ == "__main__":

    cycle = 0
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
    
    #for i in range(int(len(screen) / 40 + 1)):
    #    print(*screen[i*40:i*40 + 39])
    print(*screen[0:40])
    print(*screen[40:80])
    print(*screen[80:120])
    print(*screen[120:160])
    print(*screen[160:200])
    print(*screen[200:240])