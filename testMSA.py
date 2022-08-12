# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 23:31:29 2022

@author: dekom
"""
from include.Node import Node
from include.agent import agent
from include.obstacle import obstacle
from include.DynamicEnv import DynamicEnv
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm
import random
import multiprocessing

maxDepth = 4 # 9 = 512*512
vertex = [0, 0]
leafCapacity = 1
a = (1, 1)
alpha = 2
beta = 0.75
reservedMap = obstacle(maxDepth)
reservedMap = reservedMap.getMap()
for i in range(1, 5):
    for j in range(1 , 5):
        if i < len(reservedMap) and j < len(reservedMap):
            if reservedMap[i][j] != 99:
                reservedMap[i][j] = 100
current = (2,2)
destination = (10, 10)
agent1 = agent(2, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta)
agent1.MSA = True
agent1.searchAndPlot()
path = agent1.bestPath
nodes = agent1.RequiredNode
for i in path:
    print(nodes[i].vertex)
