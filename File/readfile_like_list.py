#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:12:22 2021

@author: jumman
"""

#book = open('holmes.txt', 'r')
#
#char_count = 0
#for line in book:
#    char_count += len(line)
#print(char_count)
# book.close()
def countChar(filename):
    with open(filename, "r") as book:
        charCount = 0
        for line in  book:
            charCount += len(line)
    return charCount

#print(countChar("holmes.txt"))