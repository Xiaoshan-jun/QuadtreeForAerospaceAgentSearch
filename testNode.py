# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:45:47 2022

@author: dekom
"""
from include.Node import Node
import numpy as np
from include.Node import Node
from include.agent import agent
from include.obstacle import obstacle
from include.DynamicEnv import DynamicEnv
import time
import numpy as np

reservedMap = np.zeros((4,4))
vertex = (0, 0)
size = 1
#node1 = Node(2, 1, vertex, 2, None, None, reservedMap, 1)
#child = node1.addChild()
agent1 = agent(1, (0, 0), (3,3), 2, vertex, 1, reservedMap, 2, 2, 0.75)
agent1.MSA = True
agent1.searchAndPlot()
agent1.move(0)
agent1.record(0)
print(reservedMap)

agent1.searchAndPlot()
agent1.move(1)
agent1.record(1)
print(reservedMap)
agent1.searchAndPlot()
agent1.move(2)
agent1.record(2)
agent1.move(3)
agent1.record(4)
print(reservedMap)
