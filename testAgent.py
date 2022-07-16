# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:43:00 2022

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

if __name__ == "__main__":
    #test parameter
    NUM_AGENT = 10
    NUM_TESTING = 100
    RANDOM_POSITION = True
    maxDepth = 9 # 9 = 512*512
    vertex = [0, 0]
    leafCapacity = 1
    a = (1, 1)
    alpha = 2
    beta = 0.75
    reservedMap = obstacle(maxDepth)
    reservedMap = reservedMap.getMap()
    start = np.genfromtxt('start.csv', delimiter=',')
    target = np.genfromtxt("target.csv", delimiter=',')
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    agentList = []
    for i in range(0, NUM_AGENT):
        agentList.append(agent(i + 1, start[i], target[i], maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
    #managerList = manager.list(agentList)
    dynamic_env = DynamicEnv(reservedMap, agentList)
    t0 = time.time()
    ct = time.time() #current time 
    #processes = []
    # for Agent in agentList:
    #     p = multiprocessing.Process(target = Agent.searchAndPlot)
    # processes.append(p)
    while len(agentList) > 0:
        if time.time() - ct > 1:
            print(time.time())
            ct = time.time()
            for i in range(len(agentList)):
                agentList[i].searchAndPlot()
            dynamic_env.step()
    t1 = time.time() - t0
    
    

