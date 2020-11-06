#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:17:55 2020

@author: soji
"""

n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)