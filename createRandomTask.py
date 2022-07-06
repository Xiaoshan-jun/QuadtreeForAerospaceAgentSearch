# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:52:01 2022

@author: dekom
"""
import random
from include.obstacle import Obstacle
import numpy as np

start = []
reservedMap = Obstacle(10)
reservedMap = reservedMap.getMap()
while len(start) < 1000:
    while True:
        x = random.randint(0, 1023)
        y = random.randint(0, 1023)
        if reservedMap[x][y] == 0:
            break
    start.append((x, y))
target = []
while len(target) < 1000:
    while True:
        x = random.randint(0, 1023)
        y = random.randint(0, 1023)
        if reservedMap[x][y] == 0:
            break
    target.append((x, y))
np.savetxt('start10.csv', start, delimiter=',')
np.savetxt('target10.csv', target, delimiter=',')

