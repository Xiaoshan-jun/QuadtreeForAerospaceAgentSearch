# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:46:17 2022

@author: dekom
"""
#--------------------------example A*
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

#test parameter
NUM_AGENT = 10
NUM_TESTING = 5
RANDOM_POSITION = True
maxDepth = 9
maps = 0 # 0 means normal, 1 means hard map
vertex = [0, 0]
leafCapacity = 1
a = (1, 1)
alpha = 2
beta = 0.75
#start9 means normal, start means hard

#agentList.append(agent(1, (1, 1), (511, 511), maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
#agentList.append(agent(1, (1, 1), (511, 511), maxDepth, vertex, leafCapacity, reservedMap, 100, 2, beta))
# dynamic_env = DynamicEnv(reservedMap, agentList)
# dynamic_env.updateMapOnly()
# for i in range(50):
#     x = random.randint(3, len(reservedMap))
#     y = random.randint(3, len(reservedMap))
#     width = random.randint(len(reservedMap)//50, len(reservedMap)//10)
#     length = random.randint(len(reservedMap)//50, len(reservedMap)//10)
#     for i in range(x, x + width):
#         for j in range(y , y + length):
#             if i < len(reservedMap) and j < len(reservedMap):
#                 if reservedMap[i][j] != 99:
#                     reservedMap[i][j] = 100
# reservedMap[30][30] = 100
# reservedMap[30][31] = 100
# reservedMap[30][32] = 100
# reservedMap[31][30] = 100
# reservedMap[31][31] = 100
# reservedMap[31][32] = 100
# reservedMap[50][50] = 100
# reservedMap[50][51] = 100
# reservedMap[50][52] = 100
# reservedMap[51][50] = 100
# reservedMap[51][51] = 100
# reservedMap[51][52] = 100
# reservedMap[52][50] = 100
# reservedMap[52][51] = 100
# reservedMap[52][52] = 100
# agent1 = agent(1, (1, 3), (63, 63), maxDepth, vertex, leafCapacity, reservedMap, 2, 2, 0.75)
# #agent1.findRequiredNode()
# while agent1.arrive == False:
#     agent1.searchAndPlot()
#     agent1.move(1)
#     agent1.record(1)
#     if agent1.bestPath:
#        agent1.plotBestPath()
# agent1.searchAndPlot()
# agent1.plotBestPath()
# #plt = agent1.drawGraph()
# # plt.title('a sample task in a sample map')
# # plt.show()

#---------------------------------------
# start = np.genfromtxt('start9.csv', delimiter=',', dtype = int)
# target = np.genfromtxt("target9.csv", delimiter=',', dtype = int)
# reservedMap = obstacle(maxDepth, maps)
# reservedMap = reservedMap.getMap()
# agentList = []
# for i in range(0, NUM_AGENT):
#     current = tuple(start[i])
#     destination = tuple(target[i])
#     agentList.append(agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
# dynamic_env = DynamicEnv(reservedMap, agentList)
# dynamic_env.step()
# for agent in agentList:
#     fn = "figure/agent" + str(agent.agentNumber) + '.csv'
#     np.savetxt(fn, agent.history, delimiter=',')
# #fn = 'figure/MSAstarStressed.csv'
# fn = "figure/Astareasy.csv"
# np.savetxt(fn, reservedMap, delimiter=',')
#----------------------------------------MSA time test
start = np.genfromtxt('start9.csv', delimiter=',', dtype = int)
target = np.genfromtxt("target9.csv", delimiter=',', dtype = int)
reservedMap = obstacle(maxDepth, maps)
reservedMap = reservedMap.getMap()
time = []
for i in range(1000):
    current = tuple(start[i])
    destination = tuple(target[i])
    a = agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta)
    a.searchAndPlot()
    time.append(a.searchtime)


