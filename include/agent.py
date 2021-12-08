# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:23:00 2021
Agent Class can pick the appropriate nodes and build path graph
@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""
import matplotlib.pyplot as plt
from math import hypot
import numpy as np


class agent(object): 
    
    def __init__(self, tree, position, target, eDistance = 2, printb = True):
        self.tree = tree 
        self.eDistance = eDistance #defalut 2 (alpha in paper)
        self.position = position #current position in (x, y)
        self.currentNode = None #current node where the agent locate
        self.currentNodeIndex = 0  #the index currentNode in RequiredNode. RequiredNode[currentNodeIndex] == currentNode
        self.target = target #current target in (x, y)
        self.targetNode = None #target node where the destination locate
        self.targetNodeIndex = 0 #the index targetNode in RequiredNode
        self.RequiredNode = []
        self.pathmap = None #plt of path
        self.graph = None #[n,n] array save the cost from node1 to node2
        self.bestPath = []
        self.findRequiredNode()
        self.buildPathGraph(printb)
        
    def setTree(self, tree):
        self.tree = tree
    
    def findRequiredNode(self):
        print("finding required node for path planing....")
        tree = self.tree
        openedNode = [tree.getRoot()] #create a list of wait to be open
        ac = self.position #agent center
        tc = self.target #target center
        while openedNode:
            #get the first node in the openedNode list
            node = openedNode.pop(0)
            while node == None: #skip None
                node = openedNode.pop(0)
            #if it is a leaf node, add into RequiredNode, and check if it is the agent/target node
            if node.getIsLeaf(): 
                node.setMark(len(self.RequiredNode))
                nc = node.getCenter()
                xd2 = (nc[0] - tc[0])**2
                yd2 = (nc[1] - tc[1])**2
                dist2 = np.sqrt(xd2 + yd2)
                node.setH(dist2* (1.1 - node.getCapacityPercentage()))
                self.RequiredNode.append(node)
                #check if the Node is the agent locate
                ax = ac[0]
                ay = ac[1]
                xl, yl, xh, yh = node.getVertex()
                if ax >= xl and ay >= yl and ax < xh and ay < yh:  #(consider agent is in the node if on left/bottom edge)
                    self.currentNode = node
                    self.currentNodeIndex = len(self.RequiredNode) - 1

            else:  
                nc = node.getCenter()
                xd = (nc[0] - ac[0])**2
                yd = (nc[1] - ac[1])**2
                dist = np.sqrt(xd + yd) #the distance between current node and agent position
                #check if the Node should be explore, we only explore node is close to the agent and target
                if dist <= (self.eDistance * (2**(node.getDepthFromBottom())))  :
                #if dist <= self.eDistance**(node.getDepthFromBottom()) or dist2 <= self.eDistance**(node.getDepthFromBottom()) :
                    openedNode.extend(node.getallChild())
                else:
                    node.setMark(len(self.RequiredNode))
                    xd2 = (nc[0] - tc[0])**2
                    yd2 = (nc[1] - tc[1])**2
                    dist2 = np.sqrt(xd2 + yd2)  #the distance between current node and targets position
                    node.setH(dist2)
                    self.RequiredNode.append(node)
        #check if the Node is the agent's target locate after requiredNode is created
        tx = tc[0]
        ty = tc[1]
        for index, node in enumerate(self.RequiredNode):
            xl, yl, xh, yh = node.getVertex()
            if tx >= xl and ty >= yl and tx < xh and ty < yh:  #(consider agent is in the node if on left/bottom edge)
                self.targetNode = node
                self.targetNodeIndex = index
        return self.RequiredNode
    
    def buildPathGraph(self, printb):
        print("building path graph for path planing....")
        #plt = 0
        #if printb:
            #plt = self.drawGraph() #load node map
        
        Graph = {}
        for i in range(len(self.RequiredNode)):
            Graph[i] = {}
            for j in range(len(self.RequiredNode)):
                node1 = self.RequiredNode[i]
                node2 = self.RequiredNode[j]
                if self.ifNeibor(node1, node2):
                    x = [node1.getCenter()[0], node2.getCenter()[0]]
                    y = [node1.getCenter()[1], node2.getCenter()[1]]
                    #if plt:
                        #plt.plot(x, y, 'go', linewidth=1 , markersize = 0.1, linestyle="--")
                    direction, dist = self.checkRelativePosition(node1, node2)
                    Graph[i][j] = round(dist * node1.getMoveCost(direction),1)
                    
                    #if dist > 4 and plt:
                        #plt.text((x[0] + x[1])/2, (y[0] + y[1])/2, str(Graph[i][j]))
        self.graph = Graph
        #self.pathmap = plt
        #plt.show()
        return self.graph
    
    def buildBestGraph(self):
        print("building best path graph for path planing....")
        
        plt = self.pathmap #load path map
        
        for mark in self.bestPath:
                node1 = self.RequiredNode[mark]
                plt.gca().add_patch(node1.drawPathSquare())
        node = self.RequiredNode[self.bestPath[-1]]
        plt.gca().add_patch(node.drawTargetSquare())
        #draw target
        plt.show()
        return None
    
    def drawGraph(self):
        plt.figure(figsize = (8, 8), dpi=100)
        plt.axes()
        for node in self.RequiredNode:
            plt.gca().add_patch(node.drawSquare())
        plt.gca().add_patch(self.getCurrentNode().drawAgent())
        #plt.gca().add_patch(self.getTargetNode().drawTarget())
        plt.axis('scaled')
        plt.title('searched path from ' + str(self.position) + ' to ' + str(self.target))
        graph = plt
        return graph
                
    #check if two nodes are neibor by check if they share vertex
    def ifNeibor(self, node1, node2):
        list1 = [node1.vertex, node1.vertex_nw, node1.vertex_se, node1.vertex_ne]

        list2 = [node2.vertex, node2.vertex_nw, node2.vertex_se, node2.vertex_ne]
        
        nt1 = map(tuple, list1)
        nt2 = map(tuple, list2)
        st1 = set(nt1)
        st2 = set(nt2)
        list3 = list(set(st1).intersection(st2)) #share vertex
        
        xs1 = node1.vertex[0]
        xl1 = node1.vertex_ne[0]
        ys1 = node1.vertex[1]
        yl1 = node1.vertex_ne[1]
        
        xs2 = node2.vertex[0]
        xl2 = node2.vertex_ne[0]
        ys2 = node2.vertex[1]
        yl2 = node2.vertex_ne[1]
        
        if xl2 == xs1: #may W
            if yl2 >= ys1 and yl2 <= yl1:
                return True
            elif ys2 >= ys1 and ys2 <= yl1:
                return True
            
        if xs2 == xl1: #may E
            if yl2 >= ys1 and yl2 <= yl1:
                return True
            elif ys2 >= ys1 and ys2 <= yl1:
                return True
            
        if ys2 == yl1: #may N
            if xl2 >= xs1 and xl2 <= xl1:
                return True
            elif xs2 >= xs1 and xs2 <= xl1:
                return True
        
        if yl2 == ys1: #may S
            if xl2 >= xs1 and xl2 <= xl1:
                return True
            elif xs2 >= xs1 and xs2 <= xl1:
                return True
                
        
        if len(list3) > 0 and len(list3) < 4:
            return True
        else:
            return False
        
        #check the node2's position relative to node1, and distance between these two node
    def checkRelativePosition(self, node1, node2):
        c1 = node1.getCenter()
        c1x = c1[0]
        c1y = c1[1]
        c2 = node2.getCenter()
        c2x = c2[0]
        c2y = c2[1]
        xd = (c1x - c2x)**2
        yd = (c2y - c1y)**2
        dist = np.sqrt(xd + yd)
        if c2x > c1x:
            if c2y > c1y: #NE
                return 2, dist
            elif c2y == c1y: #E
                return 4, dist
            elif c2y < c1y: #SE
                return 7, dist
        elif c2x == c1x:
            if c2y > c1y: #N
                return 1, dist
            elif c2y < c1y: #S
                return 6, dist
        elif c2x < c1x:
            if c2y > c1y: #NW
                return 0, dist
            elif c2y == c1y: #W
                return 3, dist
            elif c2y < c1y: #SW
                return 5, dist
            
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
    
    def setBestPath(self, bestPath):
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

    def move(self,step):
        current = self.currentNode
        stepMark = self.bestPath[step]
        step = self.RequiredNode[stepMark]
        direction, dist = self.checkRelativePosition(current, step)
        center = step.getCenter()
        current.setMoveCost(direction, 10000)
        self.position = center
        self.RequiredNode = []
        self.graph = None
        self.findRequiredNode()
        self.buildPathGraph(True)
        
        