# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 01:38:05 2022

the normal a*
"""
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

def collisionCheck(reservedMap, position, maxDepth):
    s = 2**maxDepth
    s = s - 1
    if position[0] < 0 or position[1] < 0 or position[0] > s or position[1] > s:
        return True
    if reservedMap[position[0]][position[1]] != 0 or reservedMap[position[0]][position[1]] == 100:
        return True
    return False        

def aStarSearch(xI,xG, reservedMap ,maxDepth,heuristic='euclidean'):
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
            print("search failed")
            return False, False, False, False, False
        currentposition = visited.pop()
        if currentposition == xG:
            print("goal found")
            break
        explored.append(currentposition)
        current = nodeList[currentposition]
        for a in actions:
            # check collision
            newposition = (currentposition[0] + a[0], currentposition[1] + a[1])
            if collisionCheck(reservedMap, newposition, maxDepth) == False:
                if reservedMap[newposition[0]][newposition[1]] == 100:
                    newg = current.g + 100
                else:
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