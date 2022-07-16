# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:50:21 2022
static map
multi agents

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
import multiprocessing

#test parameter
NUM_AGENT = 10
NUM_TESTING = 100
RANDOM_POSITION = True
maxDepth = 9 # 9 = 512*512
vertex = [0, 0]
leafCapacity = 1
a = (1, 1)
alpha = 1.5
beta = 0.25
start = []
target = []
#create reservedMap
global reservedMap
original = Obstacle(maxDepth,0)
reservedMap = original.getMap()
#create multiple agent
agentList = []
for i in range(NUM_AGENT):
    agentList.append(agent(i + 2, start[i], target[i], maxDepth, vertex, leafCapacity, reservedMap, alpha, 2, beta))
