# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:57:26 2022
test if the code working,  unimportant
@author: dekom
"""
from include.obstacle import obstacle
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm
import time
import numpy as np
# ----------------------------Astar Search Algorithm start-----------
class node:
    def __init__(self, position, g, gh):
        self.position = position
        self.gh = gh #real cost to come + heuristic value
        self.g = g #real cost to come
        self.path = []
    def updateC(self, gh):
        self.gh = gh


class PriorityQueue:
    def __init__(self, NodeList):
        self.queue = [] #position
        self._index = 0
        self.NodeList = NodeList
        
    def remove(self, p):
        self._index = -1
        self.queue.remove(p)
        
    def insert(self, node):
        last = True
        for i in range(len(self.queue)):
            if self.NodeList[self.queue[i]].gh > node.gh:
                self.queue.insert(i, node.position)
                last = False
                self._index += 1
                break
        if last:
            self.queue.append(node.position)
            self._index += 1

    def pop(self):
        self._index -= 1
        return self.queue.pop(0)
    
def manhattanHeuristic(state, goal):
   """ewg, newc)
   A heuristic function estimates the cost from the current state to the nearest
   goal.  This heuristic is trivial.
   """
   return abs(goal[0] - state[0]) + abs(goal[1] - state[1]) 

def euclideanHeuristic(state, goal):
    return ((goal[0] - state[0])**2 + (goal[1] - state[1])**2)**0.5

def getCostOfActionsEuclideanDistance(a):
    return (a[0]**2 + a[1]**2)**0.5

def collisionCheck(position, maxDepth):
    s = 2**maxDepth
    s = s - 1
    if position[0] < 0 or position[1] < 0 or position[0] > s or position[1] > s:
        return True
    if reservedMap[position[0]][position[1]] != 0:
        return True
    return False        

def aStarSearch(xI,xG, maxDepth,heuristic='euclidean'):
    "Search the node that has the lowest combined cost and heuristic first."
    """The function uses a function heuristic as an argument. We have used
  the null heuristic here first, you should redefine heuristics as part of 
  the homework. 
  Your algorithm also needs to return the total cost of the path using
  getCostofActions functions. 
  Finally, the algorithm should return the number of visited
  nodes during the search."""
  #             E
    #actions = [(1, 1), (0, 1), (-1, 1), (-1, 0), (1, 0), (1,-1), (0, -1), (-1, -1)]
    actions = [ ( 0, 1), ( -1, 0), ( 1, 0),  ( 0, -1)]
    #actions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    root = node(xI, 0, euclideanHeuristic(xI, xG))
    root.path = []
    nodeList = {} #{position：node}
    nodeList[xI] = root
    visited = PriorityQueue(nodeList) 
    visited.insert(root)
    count = 0
    explored = []
    while True:
        count = count + 1
        #print(count)
        if visited._index == 0:
            return [], [], [], [], []
        currentposition = visited.pop()
        if currentposition == xG:
            print("goal found")
            break
        explored.append(currentposition)
        current = nodeList[currentposition]
        for a in actions:
            # check collision
            newposition = (currentposition[0] + a[0], currentposition[1] + a[1])
            if collisionCheck(newposition, maxDepth) == False:
                newg = current.g + getCostOfActionsEuclideanDistance(a)
                if heuristic == 'manhattan':
                    newc = newg + manhattanHeuristic(newposition, xG)
                if heuristic == 'euclidean':
                    newc = newg + euclideanHeuristic(newposition, xG)
                # check if new node found add to nodeList and pripority queue
                if newposition not in nodeList:
                    newnode = node(newposition, newg, newc)
                    nodeList[newposition] = newnode
                    visited.insert(newnode)
                    newnode.path = current.path.copy()
                    newnode.path.append(newposition)
                else:
                    if newc < nodeList[newposition].gh:
                        newnode = node(newposition, newg, newc)
                        newnode.path = current.path.copy()
                        newnode.path.append(newposition)
                        nodeList[newposition] = newnode
                        if newposition in  visited.queue:
                            visited.remove(newposition)
                        visited.insert(newnode)
                        

    path = nodeList[xG].path
    actionList = []
    for i in range(len(path) - 1):
        node1 = path[i]
        node2 = path[i + 1]
        action = (node2[0] - node1[0], node2[1] - node1[1])
        actionList.append(action)
    return actionList, path, nodeList, count, explored

#test parameter
NUM_TESTING = 100
RANDOM_POSITION = True
maxDepth = 10 # 9 = 512*512
global reservedMaps
original = obstacle(maxDepth)
reservedMap = original.getMap()
start = np.genfromtxt('start10.csv', delimiter=',', dtype = int)
target = np.genfromtxt("target10.csv", delimiter=',', dtype = int)
PATHLENGTH = []
Succesful = 0
t1 = time.time()
for i in range(NUM_TESTING):
    current = tuple(start[i])
    destination = tuple(target[i])
    actionList, path, nodeList, count, explored = aStarSearch(current,destination, maxDepth)
    PATHLENGTH.append(len(path))
t2 = time.time()
print("average total Length: " ,np.mean(PATHLENGTH))
print("time:" , t2 - t1)    
Succesful=(np.count_nonzero(PATHLENGTH)/NUM_TESTING)
# maxDepth = 9
# target = (511,511)
# position = (10, 10)
# actionList, path, nodeList, count, explored = aStarSearch(position,target, maxDepth)
# for i in path: 
#     if i[0] > 10 and i[0] < 502 and i[1] > 10 and i[1] < 502:
#         reservedMap[i] = 2
    
# lensum.append(len(path))
# target = (507,507)
# position = (7, 7)


plt.figure(figsize = (8, 8), dpi=100)
plt.axes()
my_cmap = cm.get_cmap('Greys')
min_val = 0
max_val = 7
norm = matplotlib.colors.Normalize(min_val, max_val)
for i in range(512):
    for j in range(512):
        if reservedMap[i][j] != 0:
            color_i = my_cmap(norm(reservedMap[i][j]))
            square = plt.Rectangle((i, j), 1, 1, fc=color_i )
            plt.gca().add_patch(square)
plt.axis('scaled')
plt.show()