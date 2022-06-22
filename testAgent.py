# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:43:00 2022

@author: dekom
"""
from include.Node import Node
from include.agent import agent
from include.obstacle import Obstacle
import time
import numpy as np
reservedMap = Obstacle()
reservedMap = reservedMap.getMap()
#
maxDepth = 9
target = (511,511)
position = (0, 0)
vertex = [0, 0]
leafCapacity = 1
agent2 = agent(2, position, target, maxDepth, vertex, leafCapacity, reservedMap, 2, 2, 0.5)
t1 = time.time()
while agent2.arrive == False:
    agent2.searchAndPlot()
    agent2.move()
t = time.time() - t1
print("search time: ", t)