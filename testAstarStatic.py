# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 19:34:16 2022

@author: dekom
"""

from include.astaragent import astaragent
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
    reservedMap = obstacle(maxDepth)
    reservedMap = reservedMap.getMap()
    start = np.genfromtxt('start.csv', delimiter=',', dtype = int)
    target = np.genfromtxt("target.csv", delimiter=',', dtype = int)
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    agentList = []
    for i in range(0, NUM_AGENT):
        current = tuple(start[i])
        destination = tuple(target[i])
        agentList.append(astaragent(i+1, current, destination, maxDepth, reservedMap))
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


# plt.figure(figsize = (8, 8), dpi=100)
# plt.axes()
# my_cmap = cm.get_cmap('Greys')
# min_val = 0
# max_val = 100
# norm = matplotlib.colors.Normalize(min_val, max_val)
# for i in range(512):
#     for j in range(512):
#         if reservedMap[i][j] != 0:
#             color_i = my_cmap(norm(reservedMap[i][j]))
#             square = plt.Rectangle((i, j), 1, 1, fc=color_i )
#             plt.gca().add_patch(square)
# plt.axis('scaled')
# plt.show()