#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.
     
    Bugs: none known
 
 
    Author: Alessandro Bedini alle.bedo@gmail.com
    Date Created: 01/12/2022

"""

if __name__ == "__main__":
    max = 0

    with open("/home/allebedo/Projects/AdventOfCode/2022/Bedo/resources/AoC_1.txt", 'r') as file:
        cur = 0
        for line in file:
            if line != '\n':
                cur += int(line)
            else:
                if cur > max:
                    max = cur
                cur = 0

    print(max)