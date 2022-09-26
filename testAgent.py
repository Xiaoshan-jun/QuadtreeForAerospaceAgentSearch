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
    NUM_TESTING = 5
    RANDOM_POSITION = True
    maxDepth = 9 # 9 = 512*512
    vertex = [0, 0]
    leafCapacity = 1
    a = (1, 1)
    alpha = 2
    beta = 0.75
    start = np.genfromtxt('start9.csv', delimiter=',', dtype = int)
    target = np.genfromtxt("target9.csv", delimiter=',', dtype = int)
    t = []
    dr = []
    iterations = []
    for j in range(NUM_TESTING):
        reservedMap = obstacle(maxDepth)
        reservedMap = reservedMap.getMap()
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        agentList = []
        straightDistance = []
        for i in range(0, NUM_AGENT):
            current = tuple(start[i + NUM_AGENT * j])
            destination = tuple(target[i + NUM_AGENT * j])
            sd = abs(destination[0] - current[0]) + abs(destination[1] - current[1])
            agentList.append(agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
            straightDistance.append(sd)
        dynamic_env = DynamicEnv(reservedMap, agentList)
        t0 = time.time()
        ct = time.time() 

        while len(agentList) > 0:
            if time.time() - ct > 1:
                print(time.time())
                ct = time.time()
                dynamic_env.step()
        
        t1 = time.time() - t0
        print(t1)
    
    

