#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.
     
    Bugs: none known
 
 
    Author: Alessandro Bedini alle.bedo@gmail.com
    Date Created: 01/12/2022

"""

if __name__ == "__main__":
    count = 0
    with open("2022/Bedo/resources/AoC_4.txt", 'r') as file:
        for line in file:
            sections = line.split(',')
            first_set = set(range(int(sections[0].split('-')[0]), int(sections[0].split('-')[1]) + 1))
            second_set = set(range(int(sections[1].split('-')[0]), int(sections[1].split('-')[1]) + 1))
            if len(first_set.intersection(second_set)) > 0:
                count += 1
    print(count)