# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:32:45 2021

@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""

from include.Tree import Tree
from include.agent import agent
import numpy as np


#test case1: create tree
#random costMap and moveCostMap
costMap = np.round(np.random.random((32,32))) + 1
moveCostMap = np.round(np.random.random((32,32,8))) + 1
tree = Tree(5, costMap, moveCostMap)
agent = agent(tree, [2,2],[30,30])
#test case2: move agent to specific postion
agent.move([2,5])
#test case3: move based on move cost 
#pick a node to move
index = agent.getCurrentNodeIndex() #find the currentNode
nodeList = agent.getRequiredNode() #get the current opened node list
graph = agent.getGraph() #get the graph 
possiblePath = graph[index] #get the avaliable path from current node
index = possiblePath.argmin() #find the path with the min cost
step = nodeList[index].getCenter() #move to the desired node
agent.move(step)




