# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:23:00 2021
Agent Class can choose the appropriate nodes to build path map
@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""
import matplotlib.pyplot as plt
from math import hypot
import numpy as np


class agent(object): 
    def __init__(self, tree, position, target):
        self.tree = tree
        self.position = position
        self.currentNode = None
        self.target = target
        self.targetNode = None
        self.RequiredNode = []
        self.graph = None
        self.findRequiredNode()
        self.buildPathGraph()
        
    def findRequiredNode(self):
        tree = self.tree
        openedNode = [tree.getRoot()]
        ac = self.position
        tc = self.target
        while openedNode:
            #check if the Node should be explore
            node = openedNode.pop(0)
            while node == None: #skip None
                node = openedNode.pop(0)
            if node.getIsLeaf(): 
                self.RequiredNode.append(node)
                #check if the Node is the agent locate
                ax = ac[0]
                ay = ac[1]
                xl, yl, xh, yh = node.getVertex()
                if ax >= xl and ay >= yl and ax < xh and ay < yh: 
            #(consider agent is in the node if on left/bottom edge)
                    self.currentNode = node
                #check if the Node is the agent's target locate
                tx = tc[0]
                ty = tc[1]
                xl, yl, xh, yh = node.getVertex()
                if tx >= xl and ty >= yl and tx < xh and ty < yh: 
            #(consider agent is in the node if on left/bottom edge)
                    self.targetNode = node
            else:  
                nc = node.getCenter()
                xd = (nc[0] - ac[0])**2
                yd = (nc[1] - ac[1])**2
                dist = np.sqrt(xd + yd)
                xd2 = (nc[0] - tc[0])**2
                yd2 = (nc[1] - tc[1])**2
                dist2 = np.sqrt(xd2 + yd2) 
                #check if the Node should be explore
                if dist <= 2**(node.getDepthFromBottom()) or dist2 <= 2**(node.getDepthFromBottom()): 
                    openedNode.extend(node.getallChild())
                else:
                    self.RequiredNode.append(node)
        return self.RequiredNode
    
    def buildPathGraph(self):
        Graph = np.zeros((len(self.RequiredNode), len(self.RequiredNode)))
        for i in range(len(self.RequiredNode)):
            for j in range(i + 1, len(self.RequiredNode)):
                node1 = self.RequiredNode[i]
                node2 = self.RequiredNode[j]
                if self.ifNeibor(node1, node2):
                    direction, dist = self.checkRelativePosition(node1, node2)
                    Graph[i][j] = dist * node1.getMoveCost(direction)
        self.graph = Graph
        
                
                
    def ifNeibor(self, node1, node2):
        list1 = [node1.vertex, node1.vertex_nw, node1.vertex_se, node1.vertex_ne]
        list2 = [node2.vertex, node2.vertex_nw, node2.vertex_se, node2.vertex_ne]
        nt1 = map(tuple, list1)
        nt2 = map(tuple, list2)
        st1 = set(nt1)
        st2 = set(nt2)
        list3 = list(set(st1).intersection(st2))
        if len(list3) > 0 and len(list3) < 4:
            return True
        else:
            return False

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
    
    def getTargetNode(self):
        return self.targetNode
    
    def drawGraph(self):
        plt.axes()
        for node in self.RequiredNode:
            plt.gca().add_patch(node.drawSquare())
        plt.gca().add_patch(self.getCurrentNode().drawAgent())
        plt.gca().add_patch(self.getTargetNode().drawTarget())
        plt.axis('scaled')
        plt.show()
    
        
    def move(self, step):
        self.position = step
       
    def findcurrentNode(self):
        currentNode = self.root
        self.positionInNode = None
        self.openedNode = [currentNode]
        while currentNode.isLeaf != True:
            self.openedNode.append(currentNode.getChild(0))
            self.openedNode.append(currentNode.getChild(1))
            self.openedNode.append(currentNode.getChild(2))
            self.openedNode.append(currentNode.getChild(3))
            nodeCenter = currentNode.getCenter()
            xc = nodeCenter[0]
            yc = nodeCenter[1]
            #SW
            if self.position[0] <= xc and self.position[1] <= yc:
                currentNode = currentNode.getChild(0)
                self.positionInNode = 0 #0 denotes SW, 1 denotes SE, 2 denotes NW, 3 denotes NE
            else:
                self.openedNode.append(currentNode.getChild(0))
            #SE
            if self.position[0] > xc and self.position[1] <= yc:
                currentNode = currentNode.getChild(1)
                self.positionInNode = 1 #1 denotes SE
            #NW
            if self.position[0] <= xc and self.position[1] > yc:
                currentNode = currentNode.getChild(2)
                self.positionInNode = 2 #2 denotes NW
            #NE
            if self.position[0] > xc and self.position[1] > yc:
                currentNode = currentNode.getChild(3)
                self.positionInNode = 3 #3 denotes NE
        self.currentNode = currentNode
        return currentNode

    