#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.

    Bugs: none known
 

    Author: Alessandro Bedini alle.bedo@gmail.com

    Date Created: 05/12/2022
"""
 

FILE_PATH = "2022/Bedo/resources/AoC_6.txt"

if __name__ == "__main__":


    with open(FILE_PATH, "r") as file:
        for line in file:
            index = 14
            while index < len(line):
                if len(set(line[index - 14:index])) == 14:
                    print(index)
                    break
                index += 1