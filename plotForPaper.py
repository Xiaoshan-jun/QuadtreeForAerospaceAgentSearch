# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:46:17 2022
plot figures for the paper
@author: jxiang
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

def getDistance(c1, c2):
    #important
    x = c1[0] - c2[0]
    y = c1[1] - c2[1]
    return np.sqrt(x**2 + y**2)

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
# reservedMap = np.zeros((2**6,2**6))
# random.seed(1)
# agentList = []
# agentList.append(agent(1, (1, 1), (511, 511), maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
# agentList.append(agent(1, (1, 1), (511, 511), maxDepth, vertex, leafCapacity, reservedMap, 100, 2, beta))
# dynamic_env = DynamicEnv(reservedMap, agentList, 1)
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
# reservedMap[32][32] = 100
# reservedMap[32][33] = 100
# reservedMap[32][34] = 100
# reservedMap[33][32] = 100
# reservedMap[33][33] = 100
# reservedMap[33][34] = 100
# reservedMap[50][50] = 100
# reservedMap[50][51] = 100
# reservedMap[50][52] = 100
# reservedMap[51][50] = 100
# reservedMap[51][51] = 100
# reservedMap[51][52] = 100
# reservedMap[52][50] = 100
# reservedMap[52][51] = 100
# reservedMap[52][52] = 100
# agent1 = agent(1, (46,46), (63, 63), maxDepth, vertex, leafCapacity, reservedMap, 100, 2, 0.25)
# # while agent1.arrive == False:
# #     agent1.searchAndPlot()
# #     agent1.move(1)
# #     agent1.record(1)
# #     if agent1.bestPath:
# #         agent1.plotBestPath()
# agent1.searchAndPlot()
# agent1.plotBestPath()
# #agent1.findRequiredNode()
# # plt = agent1.drawGraph()
# # plt.title('moving along reserved path to destination', fontsize = 20)
# #plt.title('a sample task in a sample map', fontsize = 20)
# # plt.show()

#---------------------------------------
# start = np.genfromtxt('start9.csv', delimiter=',', dtype = int)
# target = np.genfromtxt("target9.csv", delimiter=',', dtype = int)
# reservedMap = obstacle(maxDepth, maps, 1)
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
#---------------------------------------------------
# random.seed(1)
# reservedMap = obstacle(maxDepth, maps, 1)
# reservedMap = reservedMap.getMap()
# start = []
# target = []
# while len(start) < NUM_AGENT :
#     while True:
#         x = random.randint(0, 511)
#         y = random.randint(0, 511)
#         x2 = random.randint(0, 511)
#         y2 = random.randint(0, 511)
#         if reservedMap[x][y] == 0 and reservedMap[x2][y2] == 0 and getDistance((x, y), (x2, y2)) > 200:
#             break
#     start.append((x, y))
#     target.append((x2, y2))
# agentList = []
# straightDistance = 0
# for i in range(0, NUM_AGENT):
#     current = tuple(start[i])
#     destination = tuple(target[i])
#     sd = abs(destination[0] - current[0]) + abs(destination[1] - current[1])
#     agentList.append(agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
#     straightDistance += sd
# dynamic_env = DynamicEnv(reservedMap, agentList, 1)
# dynamic_env.step()
# for agent in agentList:
#     fn = "figure/agent" + str(agent.agentNumber) + '.csv'
#     np.savetxt(fn, agent.history, delimiter=',')
# fn = 'figure/MSAstarRandom.csv'
# np.savetxt(fn, reservedMap, delimiter=',')

#----------------------------------------MSA time test
# start = np.genfromtxt('start9.csv', delimiter=',', dtype = int)
# target = np.genfromtxt("target9.csv", delimiter=',', dtype = int)
# reservedMap = obstacle(maxDepth, maps)
# reservedMap = reservedMap.getMap()
# time = []
# for i in range(1000):
#     current = tuple(start[i])
#     destination = tuple(target[i])
#     a = agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta)
#     a.searchAndPlot()
#     time.append(a.searchtime)

#----------------------------------------A time test
start = np.genfromtxt('start9.csv', delimiter=',', dtype = int)
target = np.genfromtxt("target9.csv", delimiter=',', dtype = int)
reservedMap = obstacle(maxDepth, maps, 1)
reservedMap = reservedMap.getMap()
time = []
start = []
target = []
while len(start) < 1000 :
    while True:
        x = random.randint(0, 511)
        y = random.randint(0, 511)
        x2 = random.randint(0, 511)
        y2 = random.randint(0, 511)
        if reservedMap[x][y] == 0 and reservedMap[x2][y2] == 0 and getDistance((x, y), (x2, y2)) > 200:
            break
    start.append((x, y))
    target.append((x2, y2))
for i in range(1000):
    current = tuple(start[i])
    destination = tuple(target[i])
    a = agent(1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta)
    a.searchAndPlot()
    time.append(a.searchtime)


