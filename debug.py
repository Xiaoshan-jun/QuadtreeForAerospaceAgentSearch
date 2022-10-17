# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 19:46:03 2022

@author: dekom
"""
from include.Node import Node
from include.agent import agent
from include.obstacle import obstacle
from include.DynamicEnv import DynamicEnv
import time
import numpy as np

reservedMap = obstacle(9, 1)
reservedMap = reservedMap.getMap()
NUM_AGENT = 10
NUM_TESTING = 100
RANDOM_POSITION = True
maxDepth = 9 # 9 = 512*512
vertex = [0, 0]
leafCapacity = 1
a = (1, 1)
alpha = 2
beta = 0.75
start = np.genfromtxt('start.csv', delimiter=',', dtype = int)
target = np.genfromtxt("target.csv", delimiter=',', dtype = int)
agentList = []
for i in range(0, NUM_AGENT):
    current = tuple(start[i])
    destination = tuple(target[i])
    agentList.append(agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
dynamic_env = DynamicEnv(reservedMap, agentList)
for i in range(300):
    dynamic_env.step()
for agents in agentList:
    fn = "figure/agent" + str(agents.agentNumber) + '.csv'
    np.savetxt(fn, agents.history, delimiter=',')
fn = "figure/hybridStressed.csv"
np.savetxt(fn, reservedMap, delimiter=',')