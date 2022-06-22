# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:45:47 2022

@author: dekom
"""
from include.Node import Node
import numpy as np
reservedMap = np.zeros((2,2))
reservedMap[0][0] = 1
reservedMap[0][1] = 2
reservedMap[1][0] = 3
reservedMap[1][1] = 4
maxDepth = 1
target = (1,1)
vertex = [0, 0]
leafCapacity = 1

root = Node(maxDepth, 0, vertex, pow(2,maxDepth), None, None, reservedMap, leafCapacity)

A = root.addChild()

