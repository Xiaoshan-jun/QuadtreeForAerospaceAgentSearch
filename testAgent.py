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
alpha = 1.5
beta = 0.25
reservedMap = Obstacle()
reservedMap = reservedMap.getMap()
start = np.genfromtxt('start.csv', delimiter=',')
target = np.genfromtxt("target.csv", delimiter=',')
AgentSearchTime = np.zeros(NUM_AGENT)
TotalNode = []
PATHLENGTH = []
Succesful = []
AgentList = []
t1 = time.time()
totalNode = []
PathLength = []
for i in range(0, NUM_TESTING):
    t11 = time.time()
    agent2 = agent(i, start[i], target[i], maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta)
    agent2.searchAndPlot()
    totalNode.append(len(agent2.getRequiredNode()))
    while True:
        agent2.searchAndPlot()
        if agent2.arrive == False:
            #agent2.plotBestPath()
            agent2.move()
        else:
            break
    PathLength.append(len(agent2.history))
    print("search time: ", time.time() - t11)
t = time.time() - t1
print("total search time: ", t)
AgentSearchTime[0] = t
TotalNode.append(np.mean(totalNode))
Succesful.append(np.count_nonzero(PathLength)/NUM_TESTING)
#PathLength = PathLength[PathLength != 0]
averagePathLength = np.mean(PathLength)

# plt.figure(figsize = (8, 8), dpi=100)
# plt.axes()
# my_cmap = cm.get_cmap('Greys')
# min_val = 0
# max_val = 7
# norm = matplotlib.colors.Normalize(min_val, max_val)
# for i in range(512):
#     for j in range(512):
#         if reservedMap[i][j] != 0:
#             color_i = my_cmap(norm(reservedMap[i][j]))
#             square = plt.Rectangle((i, j), 1, 1, fc=color_i )
#             plt.gca().add_patch(square)
# plt.axis('scaled')
# plt.show()
