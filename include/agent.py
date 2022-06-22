# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:23:00 2021
agent has function picks the desired nodes in the tree, builds path graph, 
defines the initial node, goal node, and does all the plotting.
@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""
import matplotlib.pyplot as plt
from math import hypot
import numpy as np
from include.Node import Node
from include.astar import search, PriorityQueue
import time

class agent(object): 
    
    def __init__(self, agentNumber, position, target, maxDepth, vertex, leafCapacity, reservedMap, eDistance = 2, alpha = 2, beta = 0.75):
        #definition: initial the agent
        #Parameters: tree: search tree #position: the agent's current position #target: the agent's goal position 
        #eDistance: the alpha in the determing function, decide the resolution #plotb: if plot the path
        #Returns: None
        self.agentNumber = agentNumber
        self.root = Node(maxDepth, 0, vertex, pow(2,maxDepth), None, None, reservedMap, leafCapacity)
        self.maxDepth = maxDepth
        self.eDistance = eDistance #defalut 2 (alpha in the paper) 
        self.position = position #current position of agent in (x, y)
        self.currentNode = None #current node where the agent locate
        self.currentNodeIndex = 0  #the index of currentNode in RequiredNode list. RequiredNode[currentNodeIndex] == currentNode
        self.target = target #current target position in (x, y)
        self.targetNode = None #target node where the destination locate
        self.targetNodeIndex = 1000000 #the index of targetNode in RequiredNode list. RequiredNode[targetNodeIndex] == targetNode
        self.RequiredNode = [] #a list of nodes that build the graph
        self.bestPath = []
        self.alpha = alpha
        self.beta = beta
        self.reservedMap = reservedMap
        self.searchtime = 0
        self.history = []
        self.arrive = False
    
    def searchAndPlot(self):
        #definition: call search function with nodes provide by octree
        #save the results of the search
        time_start = time.time()
        print('searching the best path...')
        t1 = time.time()
        self.__findRequiredNode()
        print("node found, cost ", time.time() - t1, " s")
        self.arrive = self.ifArrive()
        if self.arrive == False:
            nodeList = self.getRequiredNode() #get the current opened node list
            targetIndex = self.getTargetNodeIndex()
            frontier = PriorityQueue(nodeList)
            startIndex = self.getCurrentNodeIndex() #find the currentNode
            startnode = nodeList[startIndex]
            startnode.path = [startnode.mark]
            startnode.g = 0
            frontier.insert(startnode)
            explored = []
            path, cost, atimep= search(frontier, explored, targetIndex, nodeList)
            self.setBestPath(path)
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

    
    def move(self):
        #definition: move the agent to the new position
        #Parameters: step: how many steps the agent will go along the path
        #Returns: None
        if self.arrive == False:
            current = self.currentNode
            current.cancel(self.agentNumber) #cancel the current position reservation
            stepMark = self.bestPath[1]
            step = self.RequiredNode[stepMark]
            #cancel reserved node
            for i in range(self.validStep):
                mark = self.bestPath[i]
                node = self.RequiredNode[mark]
                self.history.append(node.getVertex())
                node.cancel(self.agentNumber)
            self.position = step.getCenter()
            self.history.append(self.history)
            print("agent", self.agentNumber, " has arrived ",self.position )
        else:
            print("agent", self.agentNumber, " has arrived")
        
    def ifArrive(self):
        return self.currentNodeIndex == self.targetNodeIndex
        
    
    def cancelReservation(self):
        for mark in self.bestPath:
            self.RequiredNode[mark].cancel(self.agentNumber)
    
    def plotBestPath(self):
        #definition: plot the best path found by the search algorithm
        #Parameters: None
        #Returns: None
        print("plotting the best path graph for path planing....")
        
        plt = self.__drawGraph() #load blocks map

        
        for mark in self.bestPath: #plot the path founded
                node1 = self.RequiredNode[mark]
                plt.gca().add_patch(node1.drawPathSquare())
        node = self.RequiredNode[self.bestPath[-1]]
        plt.gca().add_patch(node.drawTargetSquare())
        #draw target
        plt.show()
        return None
    
    def setBestPath(self, bestPath):
        #set the best path
        self.bestPath = bestPath
    
    def plotTree(self):
        plt.figure(figsize = (32, 32), dpi=100)
        ax = plt.axes() 
        for node in self.RequiredNode:
            if node:
                ax.add_patch(node.drawSquare())
        plt.axis('scaled') 
        plt.title('Reserved map') 
        plt.show()

        
    def __findRequiredNode(self):
        #definition: find the desired nodes of the tree
        #Parameters: None
        #Returns: None
        
        self.RequiredNode = [] #clear the old list
        openedNode = [self.root] #create a list of wait to be open
        ac = self.position #agent center
        tc = self.target #target center
        while openedNode:
            #get the first node in the openedNode list
            node = openedNode.pop(0)
            while node == None: #skip None
                node = openedNode.pop(0)
            #if it is a leaf node, add into RequiredNode, and check if it is the agent/target node
            if node.depth == node.maxDepth:
                important = False
                if self.__checkInANode(ac, node):  # (consider agent is in the node if on left/bottom edge)
                    self.currentNode = node
                    self.currentNodeIndex = len(self.RequiredNode)
                    important = True
                if self.__checkInANode(tc, node):  #(consider agent is in the node if on left/bottom edge)
                    self.targetNode = node
                    self.targetNodeIndex = len(self.RequiredNode)
                    important = True
                if important or node.cost < 0.5:
                    node.setMark(len(self.RequiredNode))
                    self.RequiredNode.append(node)
            else:  
                nc = node.getCenter()
                dist = self.getDistance(nc, ac) #the distance between current node and agent position
                #check if the Node should be explore, we only explore node is close to the agent and target
                if dist <= self.eDistance * (self.alpha**(node.getDepthFromBottom())) or node.Cr < self.beta :
                #if dist <= self.eDistance**(node.getDepthFromBottom()) or dist2 <= self.eDistance**(node.getDepthFromBottom()) :
                    openedNode.extend(node.addChild())
                else:
                    important = False
                    if self.__checkInANode(tc, node):  #(consider agent is in the node if on left/bottom edge)
                        self.targetNode = node
                        self.targetNodeIndex = len(self.RequiredNode)
                        important = True
                    if important or node.cost < 2:
                        node.setMark(len(self.RequiredNode))
                        self.RequiredNode.append(node)
    
    
    
    def __drawGraph(self):
        #definition: create the plt with required blocks
        #Parameters: None
        #Returns: plt
        plt.figure(figsize = (8, 8), dpi=100)
        plt.axes()
        for node in self.RequiredNode:
            plt.gca().add_patch(node.drawSquare())
        plt.gca().add_patch(self.getCurrentNode().drawAgent())
        #plt.gca().add_patch(self.getTargetNode().drawTarget())
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
    
    def setTree(self, tree):
        self.tree = tree

    def getGraph(self):
        return self.graph
    
    def getRequiredNode(self):
        return self.RequiredNode
    
    def __checkInANode(self, position, node):
        x = position[0]
        y = position[1]
        v = node.getVertex()
        nxl = v[0]
        nyl = v[1]
        size = node.getSize()
        nxh = v[0] + size
        nyh = v[1] + size
        if x >= nxl and x <nxh and y >= nyl and y < nyh:
            return True
        else:
            return False
    
    def getDistance(self, c1, c2):
        x = c1[0] - c2[0]
        y = c1[1] - c2[1]
        return np.sqrt(x**2 + y**2)
    