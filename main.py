# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:43:00 2022
main exiperience file
@author: jxiang
"""
from include.agent import agent
from include.obstacle import obstacle
from include.DynamicEnv import DynamicEnv
import time
import numpy as np
import random


def getDistance(c1, c2):
    """get euclidean distance between two grid"""
    x = c1[0] - c2[0]
    y = c1[1] - c2[1]
    return np.sqrt(x**2 + y**2)

if __name__ == "__main__":
    #test parameter
    NUM_AGENT = 10 #attention: can not exceed 99
    NUM_TESTING = 1 
    #---------------------map information--------------------------------------
    maxDepth = 9 #only support 9, map size
    maps = 1 # 0 means easy, 1 means hard map ,2 means random
    #-------------------initial parameter for agnet--------------------------
    vertex = [0, 0] #the world starts at [0, 0]
    leafCapacity = 1 #the number of agents can be in the same grid.
    a = (1, 1) 
    alpha = 2 
    beta = 0.75 
    #----------------------------result record----------------------------------
    t = [] #record process time
    dr = [] #record travel distance/manhatton distance
    iterations = [] #record iteration time
    fail = [] #record fail
    
    #------------------------------------test start--------------------------------
    for j in range(NUM_TESTING):
        #--------------------------------generate the simulated map---------------------
        random.seed(j)
        reservedMap = obstacle(maxDepth, maps, j)
        reservedMap = reservedMap.getMap()
        #--------------------------------generate the tasks-------------------------------------------
        start = []
        target = []
        while len(start) < NUM_AGENT :
            while True:
                x = random.randint(0, 2**maxDepth - 1)
                y = random.randint(0, 2**maxDepth - 1)
                x2 = random.randint(0, 2**maxDepth - 1)
                y2 = random.randint(0, 2**maxDepth - 1)
                if reservedMap[x][y] == 0 and reservedMap[x2][y2] == 0 and getDistance((x, y), (x2, y2)) > 200:
                    break
            start.append((x, y))
            target.append((x2, y2))
        #--------------------------------------assign tasks to the agent---------------------
        agentList = []
        straightDistance = 0
        for i in range(0, NUM_AGENT):
            current = tuple(start[i])
            destination = tuple(target[i])
            sd = abs(destination[0] - current[0]) + abs(destination[1] - current[1])
            agentList.append(agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
            straightDistance += sd
        #---------------------------------------create the dynamic environment--------------------
        dynamic_env = DynamicEnv(reservedMap, agentList, j)
        t0 = time.time()
        ct = time.time() 
        #start search and fly!
        while len(agentList) > 0:
            if time.time() - ct > 1:
                print(time.time())
                ct = time.time()
                dynamic_env.step()
        
        t1 = time.time() - t0
        #------------------------------record results---------------------------------------
        t.append(t1)
        dr.append(dynamic_env.totalDistance/straightDistance)
        iterations.append(dynamic_env.t)
        fail.append(dynamic_env.left)
    
    

