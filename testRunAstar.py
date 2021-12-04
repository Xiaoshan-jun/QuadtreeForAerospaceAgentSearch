# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 01:24:26 2021

@author: dekom
"""
from include.Tree import Tree
from include.agent import agent
from include.obstacle import obstacle
import numpy as np
import time

#PriorityQueue for A star search------------------------don't change
#the node is sorted by lowest gh to highest gh.
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
#--------------------------PriorityQueue------------

#----------------------------Astar Search Algorithm-----------don't change
def search(frontier, explored, targetIndex, NodeList):
    print('searching the best path...')
    time_start=time.time()
    count = 0
    while True:
        if frontier._index == 0:
            time_end=time.time()
            print('fail time cost',time_end-time_start,'s')
            return False, False
        node = NodeList[frontier.pop()]
        if node.mark == targetIndex:
            time_end=time.time()
            print('Search time cost: ',time_end-time_start,'s')
            path = node.path
            return path, node.gh
        #explored.append(node.mark)
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
    print('Search time cost',time_end-time_start,'s')
#----------------------------Astar Search Algorithm-----------
#----------------------------create obstacle map ------------------------
obstacleMap = np.zeros((1024,1024))
for i in range(0,5):
    for j in range(55,62):
        obstacleMap[i][j] = 1        

for i in range(0,30):
    for j in range(50,55):
        obstacleMap[i][j] = 1
        
for j in range(45,55):
    obstacleMap[50][j] = 1
    
for j in range(46,54):
    obstacleMap[49][j] = 1

for j in range(47,53):
    obstacleMap[48][j] = 1
    
for j in range(48,53):
    obstacleMap[47][j] = 1
    
for j in range(45,54):
    obstacleMap[51][j] = 1
    
for j in range(43,55):
    obstacleMap[52][j] = 1

for j in range(40,55):
    obstacleMap[53][j] = 1

for j in range(39,55):
    obstacleMap[54][j] = 1

for j in range(41,52):
    obstacleMap[55][j] = 1

for j in range(40,50):
    obstacleMap[56][j] = 1
        
for i in range(40, 48):
    for j in range(30, 30 + i - 39):
        obstacleMap[i][j] = 1

for i in range(10,128):
    a = [ 9 ,10, 11, 12, 13, 14, 15]
    for j in a:
        obstacleMap[i][j] = 1

for i in range(15,20):
    for j in range(20,30):
        obstacleMap[i][j] = 1
        
for i in range(35,39):
    for j in range(35,50):
        obstacleMap[i][j] = 1
        
        
for i in range(38,52):
    for j in range(20,24):
        obstacleMap[i][j] = 1

for i in range(15, 20):
    for j in range(40 - i + 15 , 40 + i - 15):
        obstacleMap[i][j] = 1
    
obstacleMap[17][42] = 1
obstacleMap[18][43] = 1
obstacleMap[17][37] = 1
obstacleMap[18][36] = 1
        
for i in range(20, 25):
    for j in range(40 + i - 25 , 40 - i + 25):
        obstacleMap[i][j] = 1

for i in range(0,90):
    a = [78, 79 ,80, 81]
    for j in a:
        obstacleMap[i][j] = 1
for i in range(100,105):
    for j in range(90,125):
        obstacleMap[i][j] = 1
#----------------------------create obstacle map ------------------------
reserveMap = np.zeros((1024,1024)) #ignore it
moveCostMap = np.zeros((1024,1024,8)) + 1 #ignore it
#create the tree object with Maps
tree = Tree(6, obstacleMap, reserveMap, moveCostMap) 
#         size of map, 6->2^6 =64, 7->2^7 = 128 etc...

#create agent object
#AstarAgent = agent(tree, [2.5,2.5],    [61.5,61.5],      2, printb = True)
#                       start position, target postion, explore distance 
#---------------------------full map----------------------------------
time_start=time.time()
AstarAgent = agent(tree, [2.5,2.5],[60.5,60.5],1000) #open all the node
centerHistory = []
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
AstarAgent.buildBestGraph()
print(path)
print('total step of the path:' , len(path))
time_end = time.time()
print('full map Astar',time_end-time_start,'s')
#---------------------------------------------------------------------------------
#--------------------------------part tree--------------------------------------
time_start=time.time()
AstarAgent = agent(tree, [2.5,2.5],[61.5,61.5],2, printb = True) #change start position, end position, search distance
centerHistory = []
while AstarAgent.getCurrentNodeIndex() != AstarAgent.getTargetNodeIndex():
    center = AstarAgent.position
    centerHistory.append(center)
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
    AstarAgent.buildBestGraph()
    print(path)
    AstarAgent.move(1)
time_end = time.time()
print('partial map Astar',time_end-time_start,'s')
AstarAgent.buildBestGraph()
print(centerHistory)
print('total step of the path:' , len(centerHistory))
#--------------------------------part tree--------------------------------------




