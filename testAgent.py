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


def getDistance(c1, c2):
    #important
    x = c1[0] - c2[0]
    y = c1[1] - c2[1]
    return np.sqrt(x**2 + y**2)

if __name__ == "__main__":
    #test parameter
    NUM_AGENT = 50
    NUM_TESTING = 5
    RANDOM_POSITION = True
    maxDepth = 9 
    maps = 2 # 0 means normal, 1 means hard map ,2 means random
    vertex = [0, 0]
    leafCapacity = 1
    a = (1, 1)
    alpha = 2
    beta = 0.75
    #start9 means normal, start means hard
    # start = np.genfromtxt('start.csv', delimiter=',', dtype = int)
    # target = np.genfromtxt("target.csv", delimiter=',', dtype = int)
    t = [] #record process time
    dr = [] #record travel distance/manhatton distance
    iterations = []
    fail = []
    for j in range(NUM_TESTING):
        random.seed(j)
        reservedMap = obstacle(maxDepth, maps, j)
        reservedMap = reservedMap.getMap()
        start = []
        target = []
        while len(start) < NUM_AGENT :
            while True:
                x = random.randint(0, 511)
                y = random.randint(0, 511)
                x2 = random.randint(0, 511)
                y2 = random.randint(0, 511)
                if reservedMap[x][y] == 0 and reservedMap[x2][y2] == 0 and getDistance((x, y), (x2, y2)) > 200:
                    break
            start.append((x, y))
            target.append((x2, y2))
        agentList = []
        straightDistance = 0
        for i in range(0, NUM_AGENT):
            current = tuple(start[i])
            destination = tuple(target[i])
            sd = abs(destination[0] - current[0]) + abs(destination[1] - current[1])
            agentList.append(agent(i + 1, current, destination, maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
            straightDistance += sd
        dynamic_env = DynamicEnv(reservedMap, agentList, j)
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
    
    

