# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:24:46 2022
astar for MSA*
@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""
import time
import numpy as np

# PriorityQueue for A star search------------------------don't change
# the node is sorted by lowest gh to highest gh.
class PriorityQueue:
    def __init__(self, NodeList):
        self.queue = [] #queue of mark of the frontier node
        self._index = 0 #length of the queue
        self.NodeList = NodeList # all the node in the map

    def insert(self, node):
        #insert the new found node mark. sort by the gh
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
            
    def remove(self, mark):
        self.queue.remove(mark)
        self._index -= 1

    def pop(self):
        self._index -= 1
        return self.queue.pop(0)

    def firstGh(self):
        #return the node with the least gh
        return self.NodeList[self.queue[0]].gh
    


# --------------------------PriorityQueue------------

# ----------------------------Astar Search Algorithm start -----------don't change
def search(frontier, explored, targetIndex, NodeList):  # code freeze
    time_start = time.time()
    goalNode = NodeList[targetIndex]
    while True:
        if frontier._index == 0: #no more frontier node
            time_end = time.time()
            print('fail time cost', time_end - time_start, 's')
            return False, False, time_end - time_start
        node = NodeList[frontier.pop()] #get the node with the lowest gh
        if node.mark == targetIndex:
            
            #print("shortest path found")
            time_end = time.time()
            #print('Search time cost: ', time_end - time_start, 's')
            path = node.path
            return path, node.gh, time_end - time_start
        explored.append(node.mark) #add the node into the explored list
        #find avaliable next action
        if node.neibornoFound():
            #find its neibor
            for j in range(len(NodeList)):
                node2 = NodeList[j]
                neibor, dist = ifNeibor4(node, node2)
                if neibor:
                    node.setAvaliable(j) #add node of into
                    node.setMovingCost(dist) #add distance 
            
        for mark in node.avaliable:
            child = NodeList[mark]
            #new g is node.g + distance + cost to arrive new node
            newg = node.g + child.cost * (node.movingCost[node.avaliable.index(mark)])
            if newg < child.g:
            # print(mark)
                if mark not in frontier.queue: #node does not found in frontier queue
                    child.setG(newg)
                    child.setH(child.cost * euclideanHeuristic(child.getCenter(), goalNode.getCenter()))
                    child.setGH(newg + child.h)
                    child.path = node.path.copy()
                    child.path.append(child.mark)
                    frontier.insert(child)
                elif mark in frontier.queue:#found in frontier queue, h has been found, reinsert
                    child.setG(newg)
                    child.setGH(newg + child.h)
                    child.path = node.path.copy()
                    child.path.append(child.mark)
                    frontier.remove(child.mark)
                    frontier.insert(child)
                
    time_end = time.time()
    #print('Search time cost', time_end - time_start, 's')
    
def ifNeibor8(node1, node2):
    #definition: check if two nodes are neibor by check if they share vertex
    #Parameters: node1, node2
    #Returns: True or False
    c1 = node1.getCenter()
    c2 = node2.getCenter()
    x1 = c1[0]
    x2 = c2[0]
    y1 = c1[1]
    y2 = c2[1]
    xd = abs(x2 - x1)
    yd = abs(y2 - y1)
    maxd = max(xd, yd)
    dist = getDistance(c1, c2)
    maxNeiborDist = (node1.getSize() + node2.getSize()) / 2
    return maxd <= maxNeiborDist and maxd > 0, dist

def ifNeibor4(node1, node2):
    #definition: check if two nodes are neibor by check if they share vertex
    #Parameters: node1, node2
    #Returns: True or False
    c1 = node1.getCenter()
    c2 = node2.getCenter()
    x1 = c1[0]
    x2 = c2[0]
    y1 = c1[1]
    y2 = c2[1]
    xd = abs(x2 - x1)
    yd = abs(y2 - y1)
    maxd = max(xd, yd)
    dist = getDistance(c1, c2)
    maxNeiborDist = (node1.getSize() + node2.getSize()) / 2
    return maxd <= maxNeiborDist and maxd > 0 and dist < (node1.getSize() + node2.getSize()) * np.sqrt(2) / 2, dist
def findNeibor(node):
    # 0 denotes SW(bottom-left), 1 denotes SE(bottom-right), 2 denotes NW(top-left), 3 denotes NE(top east)
    #find north
    pass
            


def getDistance( c1, c2):
    x = c1[0] - c2[0]
    y = c1[1] - c2[1]
    return np.sqrt(x**2 + y**2)

def manhattanHeuristic(state, goal):
   """ewg, newc)
   A heuristic function estimates the cost from the current state to the nearest
   goal.  This heuristic is trivial.
   """
   return abs(goal[0] - state[0]) + abs(goal[1] - state[1]) 
def euclideanHeuristic(state, goal):
    return ((goal[0] - state[0])**2 + (goal[1] - state[1])**2 )**0.5