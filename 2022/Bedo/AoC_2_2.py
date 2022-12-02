#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Insert a description here.
     
    Bugs: none known
 
 
    Author: Alessandro Bedini alle.bedo@gmail.com
    Date Created: 01/12/2022

"""

# A -> Rock 1pt
# B -> Paper 2pt
# C -> Scissor 3pt

# X -> lose
# Y -> draw
# Z -> win

if __name__ == "__main__":
    score = 0

    with open("C:\\Users\\abedini\\IdeaProjects\\python_scripts\\resources\\AoC_2.txt", 'r') as file:

        for line in file:
            if line[2] == "X":
                if line[0] == "A":
                    score += 3
                if line[0] == "B":
                    score += 1
                if line[0] == "C":
                    score += 2

            if line[2] == "Y":
                if line[0] == "A":
                    score += 4
                if line[0] == "B":
                    score += 5
                if line[0] == "C":
                    score += 6

            if line[2] == "Z":
                if line[0] == "A":
                    score += 8
                if line[0] == "B":
                    score += 9
                if line[0] == "C":
                    score += 7

    print(score)