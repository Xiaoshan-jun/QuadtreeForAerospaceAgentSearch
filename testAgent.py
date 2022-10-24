# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:43:00 2022
main exiperience file
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
    NUM_TESTING = 50
    RANDOM_POSITION = True
    maxDepth = 9 
    maps = 1 # 0 means normal, 1 means hard map
    vertex = [0, 0]
    leafCapacity = 1
    a = (1, 1)
    alpha = 2
    beta = 0.75
    #start9 means normal, start means hard
    start = np.genfromtxt('start.csv', delimiter=',', dtype = int)
    target = np.genfromtxt("target.csv", delimiter=',', dtype = int)
    t = [] #record process time
    dr = [] #record travel distance/manhatton distance
    iterations = []
    fail = []
    for j in range(NUM_TESTING):
        reservedMap = obstacle(maxDepth, maps)
        reservedMap = reservedMap.getMap()
        agentList = []
        straightDistance = 0
        for i in range(0, NUM_AGENT):
            current = tuple(start[i + NUM_AGENT * j])
            destination = tuple(target[i + NUM_AGENT * j])
            sd = abs(destination[0] - current[0]) + abs(destination[1] - current[1])
            agentList.append(agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
            straightDistance += sd
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
        t.append(t1)
        dr.append(dynamic_env.totalDistance/straightDistance)
        iterations.append(dynamic_env.t)
        fail.append(dynamic_env.left)
    
    

