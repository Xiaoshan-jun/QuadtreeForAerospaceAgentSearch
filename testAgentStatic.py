# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 00:07:53 2022

@author: dekom
"""
from include.Node import Node
from include.agent import agent
from include.obstacle import obstacle
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm
import random

#test parameter
NUM_AGENT = 1
NUM_TESTING = 100
RANDOM_POSITION = True
maxDepth = 9 # 9 = 512*512
vertex = [0, 0]
leafCapacity = 1
a = (1, 1)
alpha = 2
beta = 0.25
reservedMap = obstacle(maxDepth)
reservedMap = reservedMap.getMap()
AgentSearchTime = np.zeros(NUM_AGENT)
TotalNode = []
PATHLENGTH = []
Succesful = []
AgentList = []
t1 = time.time()
totalNode = []
PathLength = []
start = [(1, 1), (511, 1), (1, 511), (511, 511), (1, 1), (511, 1), (1, 511), (511, 511) ]
target = [(310, 310), (199, 310), (310, 199), (199, 199), (511, 511), (1, 511), (511, 1), (1, 1)] 
#create agent
for i in range(1):
    AgentList.append(agent(i + 2, start[i], target[i], maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
arrive = 0
while arrive == 0:
    arrive = 1
    for agent in AgentList:
        if agent.arrive == False:
            agent.searchAndPlot()
            agent.move()
            arrive = 0

for agent in AgentList:
    PathLength.append(len(agent.history))
print("search time: ", time.time() - t1)
t = time.time() - t1
print("total search time: ", t)
AgentSearchTime[0] = t
Succesful.append(np.count_nonzero(PathLength)/NUM_TESTING)
#PathLength = PathLength[PathLength != 0]
averagePathLength = np.mean(PathLength)