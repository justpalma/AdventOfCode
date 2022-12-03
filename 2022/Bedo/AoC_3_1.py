#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.
     
    Bugs: none known
 
 
    Author: Alessandro Bedini alle.bedo@gmail.com
    Date Created: 01/12/2022

"""

if __name__ == "__main__":
    
    items = []

    with open("/home/allebedo/Projects/AdventOfCode/2022/Bedo/resources/AoC_3.txt", 'r') as file:
        for line in file:
            found = False
            for c1 in line[0:int(len(line)/2)].strip():
                for c2 in line[int(len(line)/2):].strip():
                    if c1 == c2:
                        if str(c1).isupper():
                            items.append(ord(c1) - 38)
                        else:
                            items.append(ord(c1) - 96)
                        found = True
                    if found:
                        break
                if found:
                    break

    print(sum(items))