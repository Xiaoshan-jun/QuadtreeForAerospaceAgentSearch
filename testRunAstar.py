# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 01:24:26 2021

@author: dekom
"""
from include.Tree import Tree
from include.agent import agent
from include.obstacle import Obstacle
import matplotlib.pyplot as plt
import numpy as np
import time
textfile = open("record.txt", "w")
np.random.seed(6)
def obstacleRatio(obstacle):
    count = 0
    for i in range(len(obstacle)):
        for j in range(len(obstacle[0])):
            if obstacle[i][j] == 1:
                count += 1
    return count/(len(obstacle)**2)

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

#----------------------------Astar Search Algorithm start -----------don't change
def search(frontier, explored, targetIndex, NodeList):
    print('searching the best path...')
    time_start=time.time()
    count = 0
    while True:
        time_end=time.time()
        p = time_end-time_start
        #if p > 10:
            
            #print('fail a star',p,'s')
            #return False, False, time_end-time_start
        if frontier._index == 0:
            time_end=time.time()
            print('fail time cost',time_end-time_start,'s')
            return False, False, time_end-time_start
        node = NodeList[frontier.pop()]
        if node.mark == targetIndex:
            time_end=time.time()
            print('Search time cost: ',time_end-time_start,'s')
            path = node.path
            return path, node.gh, time_end-time_start
        explored.append(node.mark)
        for mark in node.avaliable:
            child = NodeList[mark]
            #print(mark)
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
#----------------------------Astar Search Algorithm end-----------

treeLevel = 8 # mapsize = 2^treeLevel * 2^treeLevel
#----------------------------create obstacle map ------------------------
obstacle = Obstacle()
for count in range(350):
    x = np.random.randint(0, 505)
    y = np.random.randint(0, 505)
    width = np.random.randint(2,6)
    height = np.random.randint(2,6)
    obstacle.rectangle(x, y, width, height)
    x = np.random.randint(0, 505)
    y = np.random.randint(0, 505)
    width = np.random.randint(2,6)
    obstacle.triangle(x, y, width)
    x = np.random.randint(0, 505)
    y = np.random.randint(20, 505)
    width = np.random.randint(2,6)
    obstacle.triangleR(x, y, width)
    x = np.random.randint(0, 480)
    y = np.random.randint(0, 480)
    width = np.random.randint(3,7)
    height = np.random.randint(3,7)
    obstacle.Lbuilding(x, y, width, height)
    x = np.random.randint(0, 505)
    y = np.random.randint(20, 505)
    width = np.random.randint(3,7)
    height = np.random.randint(3,7)
    obstacle.LbuildingR(x, y, width, height)
    x = np.random.randint(0, 505)
    y = np.random.randint(20, 505)
    width = np.random.randint(3,7)
    height = np.random.randint(3,7)
    obstacle.diamond(x, y, width, height)
    x = np.random.randint(0, 505)
    y = np.random.randint(0, 505)
    width = np.random.randint(3,7)
    height = np.random.randint(3,7)
    obstacle.diamondR(x, y, width, height)
    
obstacleMap = obstacle.getMap()
x = []
y = []
for i in range(512):
    for j in range(512):
        if obstacleMap[i][j] == 1:
            x.append(i)
            y.append(j)  
plt.figure(figsize = (8, 8), dpi=300)
plt.scatter(x, y, marker = 's',s = 1)
plt.title("obstacle map")
plt.show()

#----------------------------create obstacle map ------------------------
reserveMap = np.zeros((1024,1024)) #ignore it
moveCostMap = np.zeros((1024,1024,8)) + 1 #ignore it
fullastartime = []
fullastarpath = []
particialastartime = []
particialastarpath = []
obstacleRatioList = []

for i in range(10):
    #create the tree object with Maps
    #cut obstacle map
    ratio = 1
    while ratio > 0.7 or ratio < 0.2:
        x = np.random.randint(0, 512 - 2**treeLevel)
        y = np.random.randint(0, 512 - 2**treeLevel)
        selectedobstacleMap = obstacleMap[x : x + 2**treeLevel][: , y : y + 2**treeLevel]
        ratio = obstacleRatio(selectedobstacleMap)
    tree = Tree(treeLevel, selectedobstacleMap, reserveMap, moveCostMap) #modify here to adjust map size
    #         size of map, 6->2^6 =64, 7->2^7 = 128 etc...
    obstacleRatioList.append(ratio)
    for element in obstacleRatioList:
        textfile.write(element + "\t")
    textfile.write("\n")
    #create agent object
    #AstarAgent = agent(tree, [2.5,2.5],    [61.5,61.5],      2, printb = True)
    dist = 0
    bad = True
    while dist < 2**treeLevel or bad:
        startx = np.random.randint(0, 2**treeLevel)
        starty = np.random.randint(0, 2**treeLevel)
        destinationx = np.random.randint(0, 2**treeLevel)
        destinationy = np.random.randint(0, 2**treeLevel)
        xd = (startx - destinationx)**2
        yd = (starty - destinationy)**2
        dist = np.sqrt(xd + yd)
        bad = False
        if selectedobstacleMap[startx][starty] == 1 or selectedobstacleMap[destinationx][destinationy] == 1:
            bad = True
            
    
    startPosition = [startx, starty]
    destination = [destinationx + 0.5 , destinationy + 0.5]
    time_start = time.time()
    AstarAgentf = agent(tree, startPosition,destination,eDistance  = 100, printb = True) 
    #                       start position, target postion, explore distance 
    #---------------------------full map----------------------------------
    #AstarAgentf = agent(tree, [2.5,2.5],[60.5,60.5],1) #modify here to change start and end position. open all the node because explore distance is very large
    centerHistory = []
    startIndex = AstarAgentf.getCurrentNodeIndex() #find the currentNode
    nodeList = AstarAgentf.getRequiredNode() #get the current opened node list
    graph = AstarAgentf.getGraph() #get the graph  
    for i in range(len(graph[0])):
        possiblePath = graph[i]
        avaliable = []
        cost = []
        for j in range(len(possiblePath)):
            if possiblePath[j] < 100000:
                avaliable.append(j)
                cost.append(possiblePath[j])
        nodeList[i].setAvaliable(avaliable)
        nodeList[i].setMovingCost(cost)# time_accumlation = 0
    
    targetIndex = AstarAgentf.getTargetNodeIndex()
    frontier = PriorityQueue(nodeList)
    startnode = nodeList[startIndex]
    startnode.path = [startnode.mark]
    frontier.insert(startnode)
    explored = []
    path, cost, atimep= search(frontier, explored, targetIndex, nodeList)
    AstarAgentf.setBestPath(path)
    time_end = time.time()
    timep = time_end - time_start
    AstarAgentf.buildBestGraph()
    print(path)
    print('total step of the path:' , len(path))
    print('full map Astar: ',timep,'s')
    fullastartime.append(timep)
    for element in fullastartime:
        textfile.write(element + "\t")
    textfile.write("\n")
    fullastarpath.append(len(path))
    for element in fullastarpath:
        textfile.write(element + "\t")
    textfile.write("\n")
    #---------------------------------------------------------------------------------
    #--------------------------------partial tree--------------------------------------
    AstarAgentf = None
    #tree = Tree(treeLevel, selectedobstacleMap, reserveMap, moveCostMap) 
    time_start = time.time()
    AstarAgentp = agent(tree, startPosition,destination,eDistance  = 1, printb = True) 
    time_accumlation = time_end - time_start
    centerHistory = []
    while AstarAgentp.getCurrentNodeIndex() != AstarAgentp.getTargetNodeIndex():
        time_start = time.time()
        center = AstarAgentp.position
        centerHistory.append(center)
        startIndex = AstarAgentp.getCurrentNodeIndex() #find the currentNode
        nodeList = AstarAgentp.getRequiredNode() #get the current opened node list
        graph = AstarAgentp.getGraph() #get the graph  
        for i in range(len(graph[0])):
            possiblePath = graph[i]
            avaliable = []
            cost = []
            for j in range(len(possiblePath)):
                if possiblePath[j] < 100000:
                    avaliable.append(j)
                    cost.append(possiblePath[j])
            nodeList[i].setAvaliable(avaliable)
            nodeList[i].setMovingCost(cost)
        targetIndex = AstarAgentp.getTargetNodeIndex()
        frontier = PriorityQueue(nodeList)
        startnode = nodeList[startIndex]
        startnode.path = [startnode.mark]
        frontier.insert(startnode)
        explored = []
        path, cost, atimep= search(frontier, explored, targetIndex, nodeList)
        if path:
    
            AstarAgentp.setBestPath(path)
            
            AstarAgentp.buildBestGraph()
            
            
            AstarAgentp.move(1)
            time_end = time.time()
            timep = time_end - time_start
            time_accumlation += timep
            print(path)
        else:
            break
    print('partial map Astar:',time_accumlation, 's')
    #AstarAgent.buildBestGraph()
    print(centerHistory)
    print('total step of the path:' , len(centerHistory))
    particialastartime.append(time_accumlation)
    for element in particialastartime:
        textfile.write(element + "\t")
    textfile.write("\n")
    particialastarpath.append(len(centerHistory))
    for element in particialastarpath:
        textfile.write(element + "\t")
    textfile.write("\n")
    #--------------------------------part tree--------------------------------------
textfile.close()



