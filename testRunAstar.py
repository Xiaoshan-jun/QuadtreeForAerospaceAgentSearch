# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 01:24:26 2021

@author: dekom
"""
from include.Tree import Tree
from include.agent import agent
import numpy as np
import time

class PriorityQueue:
    def __init__(self, NodeList):
        self.queue = []
        self._index = 0
        self.NodeList = NodeList

    def insert(self, node):
        last = True
        for i in range(len(self.queue)):
            if self.NodeList[self.queue[i]].gh > node.gh:
                self.queue.insert(i, node.mark)
                last = False
                self._index += 1
                break
        if last:
            self.queue.append(node.mark)
            self._index += 1

    def pop(self):
        self._index -= 1
        return self.queue.pop(0)

def search(frontier, explored, targetIndex, NodeList):
    print('searching the best path...')
    time_start=time.time()
    count = 0
    while True:
        if frontier._index == 0:
            time_end=time.time()
            print('time cost',time_end-time_start,'s')
            return False, False
        node = NodeList[frontier.pop()]
        if node.mark == targetIndex:
            time_end=time.time()
            print('time cost',time_end-time_start,'s')
            return node.path, node.gh
        explored.append(node.mark)
        for mark in node.avaliable:
            child = NodeList[mark]
            if mark not in frontier.queue and mark not in explored :
                child.gh = node.gh + node.movingCost[node.avaliable.index(mark)] + child.cost + child.h
                child.path = node.path.copy()
                child.path.append(child.mark)
                frontier.insert(child)
            elif mark in frontier.queue:
                if node.gh + node.movingCost[node.avaliable.index(mark)] + child.cost + child.h < child.gh:
                    child.gh = node.gh + node.movingCost[node.avaliable.index(mark)] + child.cost + child.h
                    child.path = node.path
                    child.path.append(child.mark)
    time_end=time.time()
    print('time cost',time_end-time_start,'s')

## A star
time_start=time.time()
obstacleMap = np.zeros((128,128))
obstacleMap[5][5] = 1
obstacleMap[5][6] = 1
obstacleMap[5][7] = 1
reserveMap = np.zeros((128,128))
moveCostMap = np.zeros((128,128,8)) + 1
tree = Tree(7, obstacleMap, reserveMap, moveCostMap)
#AstarAgent = agent(tree, [2,2],[63,63], 100)
AstarAgent = agent(tree, [2,2],[100,100])
##

startIndex = AstarAgent.getCurrentNodeIndex() #find the currentNode
nodeList = AstarAgent.getRequiredNode() #get the current opened node list
graph = AstarAgent.getGraph() #get the graph  
for i in range(len(graph[0])):
    possiblePath = graph[i]
    avaliable = []
    cost = []
    for j in range(len(possiblePath)):
        if possiblePath[j] < 10000:
            avaliable.append(j)
            cost.append(possiblePath[j])
    nodeList[i].setAvaliable(avaliable)
    nodeList[i].setMovingCost(cost)
targetIndex = AstarAgent.getTargetNodeIndex()
frontier = PriorityQueue(nodeList)
startnode = nodeList[startIndex]
startnode.path = [startnode.mark]
frontier.insert(startnode)
explored = []
path, cost= search(frontier, explored, targetIndex, nodeList)
AstarAgent.setBestPath(path)
print(path)
AstarAgent.buildBestGraph()
#update costmap
for mark in path:
    node = nodeList[mark]
    vertex = node.getVertex()
    size = node.getSize()
    xl = int(vertex[0])
    yl = int(vertex[1])
    xh = int(vertex[0] + size)
    yh = int(vertex[1] + size)
    for x in range(xl, xh):
        for y in range(yl, yh):
            reserveMap[x][y] = 1/(size*size)
            
tree = Tree(5, obstacleMap, reserveMap, moveCostMap)

time_end=time.time()
print('time cost',time_end-time_start,'s')



