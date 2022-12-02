#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.
     
    Bugs: none known
 
 
    Author: Alessandro Bedini alle.bedo@gmail.com
    Date Created: 01/12/2022

"""

if __name__ == "__main__":
    max1 = 0
    max2 = 0
    max3 = 0

    with open("C:\\Users\\abedini\\IdeaProjects\\python_scripts\\resources\\AoC_1.txt", 'r') as file:
        cur = 0
        for line in file:
            if line != '\n':
                cur += int(line)
            else:
                if cur > max1:
                    max3 = max2
                    max2 = max1
                    max1 = cur
                elif cur > max2:
                    max3 = max2
                    max2 = cur
                elif cur > max3:
                    max3 = cur
                cur = 0

    print(max1 + max2 + max3)