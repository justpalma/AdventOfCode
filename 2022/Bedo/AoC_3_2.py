#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.
     
    Bugs: none known
 
 
    Author: Alessandro Bedini alle.bedo@gmail.com
    Date Created: 01/12/2022

"""

import os

if __name__ == "__main__":

    list = []
    
    items = []

    with open("/home/allebedo/Projects/AdventOfCode/2022/Bedo/resources/AoC_3.txt", 'r') as file:
        for line in file:
            list.append(line)

    index = [range(len(list))[x:x+3] for x in range(0, len(range(len(list))), 3)]

    for group in index:
        for c1 in list[group[0]].strip():
            if list[group[1]].find(c1) >= 0 and list[group[2]].find(c1) >= 0:
                items.append(ord(c1) - 38 if c1.isupper() else ord(c1) - 96)
                break

    print(sum(items))