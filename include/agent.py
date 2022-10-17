# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:23:00 2021
agent has function divide the airspace into nodes with quadtree method.
the agent can find a path to the destination with MRA*, reserve some space, and save the move plan.
@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""
import matplotlib.pyplot as plt
from math import hypot
import numpy as np
from include.Node import Node
from include.astar import search, PriorityQueue
from include.astarastar import aStarSearch
import time

class agent(object): 
    
    def __init__(self, agentNumber, position, target, maxDepth, vertex, leafCapacity, reservedMap, eDistance = 2, alpha = 2, beta = 0.75):
        #definition: initial the agent
        #Parameters: agentNumber, position, target, maxDepth, vertex, leafCapacity, reservedMap, eDistance = 2, alpha = 2, beta = 0.75
        self.agentNumber = agentNumber #the unique number of the agent.
        self.root = Node(maxDepth, 0, vertex, pow(2,maxDepth), None, None, reservedMap, leafCapacity) #the root node
        self.maxDepth = maxDepth #a map attribute
        self.position = position #current position of agent in (x, y)
        self.currentNode = None #current node where the agent locate
        self.currentNodeIndex = 0  #the index of currentNode in RequiredNode list. RequiredNode[currentNodeIndex] == currentNode
        self.target = target #current target position in (x, y)
        self.targetNode = None #target node where the destination locate
        self.targetNodeIndex = 1000000 #the index of targetNode in RequiredNode list. RequiredNode[targetNodeIndex] == targetNode
        self.RequiredNode = [] #a list of nodes that build the search graph
        self.bestPath = False #false means need to search, True means searching, a list of the position means best path is found
        self.eDistance = eDistance #parameter for the node open function
        self.alpha = alpha #parameter for the node open function
        self.beta = beta #parameter for the node open function
        self.alphaboost = 10000000
        self.reservedMap = reservedMap
        self.searchtime = 0
        self.history = [] #move history
        self.arrive = False #a boolean if the agent reach the destination
        self.loop = 0 #key value decide the alpha
        self.MSA = True
        self.bestPathtype = True #false means A*
    
    def searchAndPlot(self):
        #1. find the required nodes.
        #2. save the results of the search
        #3. reserve some space
        #self.MSA = True
        if self.MSA:
            if self.alpha > 2.5:
                self.MSA = False
                self.alpha = 2
                self.beta = 0.25
                return self
            if self.bestPath != False:
                return self
            time_start = time.time()
            t1 = time.time()
            #intelligent alpha modification
            distToDestination = self.getDistance(self.position, self.target)
            if distToDestination < 30:
                self.MSA = False
            if len(self.history) > 10:
                if self.loop > 4 or self.position == self.history[-2]:
                    self.alpha = self.alpha + 0.25
                    self.beta = self.beta + 0.25
                    self.loop = 0
                    self.alphaboost = 15
                    print("agent stuck in a loop current alpha =", self.alpha )  
            if self.alphaboost > 0:
                self.alphaboost = self.alphaboost- 1
            else:
                self.alpha = self.alpha - 0.25
                self.beta = self.beta - 0.25
                self.alphaboost = 10000000
            #find required nodes
            if self.alpha < 2:
                self.alpha = 2
            self.findRequiredNode()
            #
            #check if the agent arrive the destination
            self.arrive = self.ifArrive()
            #search
            if self.arrive == False:
                nodeList = self.getRequiredNode() #get the current opened node list
                targetIndex = self.getTargetNodeIndex()
                frontier = PriorityQueue(nodeList)
                startIndex = self.getCurrentNodeIndex() #find the currentNode
                print("agent: ", self.agentNumber)
                startnode = nodeList[startIndex]
                startnode.path = [startnode.mark]
                startnode.g = 0
                frontier.insert(startnode)
                explored = []
                path, cost, atimep= search(frontier, explored, targetIndex, nodeList)
                #save search results
                if path == False: #or cost > 500 + len(path):
                    self.setBestPath(False)
                    return False
                self.setBestPath(path)
                self.bestPathtype = True
                #reserve
                self.validStep = 0
                for n, mark in enumerate(self.bestPath):
                    if self.RequiredNode[mark].size == 1:
                        self.validStep = n
                        self.RequiredNode[mark].reserve(self.agentNumber)
                    else:
                        break
            time_end = time.time()
            self.searchtime += time_end - time_start
            #self.plotTree()
            return self
        else:
            #Astar
            time_start = time.time()
            if self.bestPath != False:
                return self
            print("agent", str(self.agentNumber), " searching the best path with A*")
            self.arrive = self.ifArrive()
            if self.arrive == False:
                self.position = (round(self.position[0]), round(self.position[1]))
                self.target = (round(self.target[0]), round(self.target[1]))
                actionList, path, nodeList, count, explored = aStarSearch(self.position, self.target, self.reservedMap, self.maxDepth)
                if path == False:
                    self.setBestPath(path)
                    return False
                self.setBestPath(path)
                self.bestPathtype = False
                #reserve
                for n in path:
                    self.reservedMap[n] = self.agentNumber
            time_end = time.time()
            if time_end - time_start > 5:
                self.MSA = True
            self.searchtime += time_end - time_start
            #self.plotTree()
            return self
    
    def move(self, t):
        #definition: move the agent to the new position
        #Parameters: step: how many steps the agent will go along the path
        #Returns: None
        if self.ifArrive() == False:
            if self.bestPath != False:
                if self.bestPathtype: #MRA
                    current = self.currentNode
                    current.cancel(self.agentNumber) #cancel the current position reservation
                    stepMark = self.bestPath.pop(1)
                    step = self.RequiredNode[stepMark]
                    if step.size  == 1:
                        if step.reservedMap[0][0] != self.agentNumber:
                            print("agent", self.agentNumber, " is blocked, redo search ")
                            for mark in self.bestPath:
                                node = self.RequiredNode[mark]
                                if node.size == 1:
                                    node.cancel(self.agentNumber)
                                else:
                                    break
                            self.bestPath = False
                        else:
                            self.currentNode = step
                            self.position = step.vertex
                            self.arrive = self.ifArrive()
                            if self.position in self.history:
                                self.loop += 1
                            print("agent", self.agentNumber, " has arrived ",self.position )
                            if len(self.bestPath) > 1:
                                stepMark = self.bestPath[1]
                                step = self.RequiredNode[stepMark]
                            
                                if step.size != 1:
                                    current = self.currentNode
                                    current.cancel(self.agentNumber) #cancel the current position reservation
                                    print("agent", self.agentNumber, " out of reservation, redo search ")
                                    for mark in self.bestPath:
                                        node = self.RequiredNode[mark]
                                        if node.size  == 1:
                                            node.cancel(self.agentNumber)
                                        else:
                                            break
                                    self.bestPath = False
                            else:
                                    current = self.currentNode
                                    current.cancel(self.agentNumber) #cancel the current position reservation
                                    print("agent", self.agentNumber, " out of reservation, redo search ")
                                    for mark in self.bestPath:
                                        node = self.RequiredNode[mark]
                                        if node.size  == 1:
                                            node.cancel(self.agentNumber)
                                        else:
                                            break
                                    self.bestPath = False
                                
                    else:
                        for mark in self.bestPath:
                            node = self.RequiredNode[mark]
                            if node.size == 1:
                                node.cancel(self.agentNumber)
                            else:
                                break
                        self.bestPath = False
                        print("agent", self.agentNumber, " out of reservation, redo search ")
                else: #a
                    moveable = True
                    for n in self.bestPath:
                        if self.reservedMap[n] == 100 or self.reservedMap[n] == 101:
                            moveable = False
                    if moveable and self.reservedMap[self.bestPath[0]] == self.agentNumber :
                        self.reservedMap[self.position] = 0
                        self.position = self.bestPath.pop(0)
                        #self.reservedMap[self.position] = 0
                        self.arrive = self.ifArrive()
                        print("agent", self.agentNumber, " has arrived ",self.position )
                    else:
                        #cancel previous resercation
                        for n in self.bestPath:
                            if self.reservedMap[n] == self.agentNumber:
                                self.reservedMap[n] = 0
                        self.bestPath = False
                        print("agent", self.agentNumber, " is blocked, redo search ")
        else:
            print("agent", self.agentNumber, " has arrived")
        #self.bestPath = False
        
    def record(self, t):
        self.history.append(self.position)
    
    def findRequiredNode(self):
        #definition: find the desired nodes of the tree
        #Parameters: None
        #Returns: None
        
        self.RequiredNode = [] #clear the old list
        openedNode = [self.root] #create a list of wait to be open
        ac = self.position #agent center
        tc = self.target #target center
        count = 0
        while openedNode:
            count += 1
            #get the first node in the openedNode list
            node = openedNode.pop(0)
            while node == None: #skip None
                node = openedNode.pop(0)
            #if it is a leaf node, add into RequiredNode, and check if it is the agent/target node
            if node.depth == node.maxDepth:
                if self.__checkInANode(ac, node):  # (consider agent is in the node if on left/bottom edge)
                    self.currentNode = node
                    self.currentNodeIndex = len(self.RequiredNode)
                if self.__checkInANode(tc, node):  #(consider agent is in the node if on left/bottom edge)
                    self.targetNode = node
                    self.targetNodeIndex = len(self.RequiredNode)
                node.setMark(len(self.RequiredNode))
                self.RequiredNode.append(node)
            else:  
                nc = node.getCenter()
                dist = self.getDistance(nc, ac) #the distance between current node and agent position
                dist2 = self.getDistance(nc, tc)
                #check if the Node should be explore, we only explore node is close to the agent and target
                if dist <= self.eDistance * (self.alpha**(node.getDepthFromBottom())):
                #if dist <= self.eDistance**(node.getDepthFromBottom()) or dist2 <= self.eDistance**(node.getDepthFromBottom()) :
                    openedNode.extend(node.addChild())
                else:
                    important = False
                    if self.__checkInANode(tc, node):  #(consider agent is in the node if on left/bottom edge)
                        self.targetNode = node
                        self.targetNodeIndex = len(self.RequiredNode)
                        important = True
                    if dist2 <= 1.5 * (self.alpha**(node.getDepthFromBottom())):
                        important = True
                    if important or node.depth < 3 or node.Cr > self.beta or node.size == 1: #* np.log(node.depth):
                        node.setMark(len(self.RequiredNode))
                        self.RequiredNode.append(node)
        #plt = self.drawGraph()
        #plt.show()
        #print(count)
    
    def ifArrive(self):
        return round(self.position[0]) == round(self.target[0]) and round(self.position[1]) == round(self.target[1]) 
        
    
    def cancelReservation(self):
        for mark in self.bestPath:
            self.RequiredNode[mark].cancel(self.agentNumber)
    
    def plotBestPath(self):
        #definition: plot the best path found by the search algorithm
        #Parameters: None
        #Returns: None
        print("plotting the best path graph for path planing....")
        
        plt = self.drawGraph() #load blocks map

        
        for mark in self.bestPath[1:]: #plot the path founded
                node1 = self.RequiredNode[mark]
                plt.gca().add_patch(node1.drawPathSquare())
        node = self.RequiredNode[self.bestPath[-1]]
        plt.gca().add_patch(node.drawTargetSquare())
        #draw target
        #plt.title('reach destination ')
        plt.show()
        return None
    
    def setBestPath(self, bestPath):
        #set the best path
        self.bestPath = bestPath
    
    
    
    def drawGraph(self):
        #definition: create the plt with required blocks
        #Parameters: None
        #Returns: plt
        plt.figure(figsize = (8, 8), dpi=100)
        plt.axes()
        for node in self.RequiredNode:
            plt.gca().add_patch(node.drawSquare())
        plt.gca().add_patch(self.getCurrentNode().drawAgent())
        plt.gca().add_patch(self.getTargetNode().drawTarget())
        plt.axis('scaled')
        plt.title('searched path from ' + str(self.position) + ' to ' + str(self.target))
        return plt
                
               
        
            
    def getCurrentNode(self):
        return self.currentNode
    
    def getCurrentNodeIndex(self):
        return self.currentNodeIndex
    
    def getTargetNode(self):
        return self.targetNode
    
    def getTargetNodeIndex(self):
        return self.targetNodeIndex
    

    def getGraph(self):
        return self.graph
    
    def getRequiredNode(self):
        return self.RequiredNode
    
    def __checkInANode(self, position, node):
        #important
        x = position[0]
        y = position[1]
        nxl, nyl, nxh, nyh = node.getVertex()
        if x >= nxl and x <nxh and y >= nyl and y < nyh:
            return True
        else:
            return False
    
    def getDistance(self, c1, c2):
        #important
        x = c1[0] - c2[0]
        y = c1[1] - c2[1]
        return np.sqrt(x**2 + y**2)
    