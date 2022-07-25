# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:52:01 2022

@author: dekom
"""
import random
from include.obstacle import obstacle
import numpy as np
def getDistance(c1, c2):
    #important
    x = c1[0] - c2[0]
    y = c1[1] - c2[1]
    return np.sqrt(x**2 + y**2)

start = []
target = []
reservedMap = obstacle(9)
reservedMap = reservedMap.getMap()
while len(start) < 1000:
    while True:
        x = random.randint(0, 511)
        y = random.randint(0, 511)
        x2 = random.randint(0, 511)
        y2 = random.randint(0, 511)
        if reservedMap[x][y] == 0 and reservedMap[x2][y2] == 0 and getDistance((x, y), (x2, y2)) > 200:
            break
    start.append((x, y))
    target.append((x2, y2))
np.savetxt('start9.csv', start, delimiter=',')
np.savetxt('target9.csv', target, delimiter=',')



