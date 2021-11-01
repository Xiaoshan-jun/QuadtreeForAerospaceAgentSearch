# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:23:00 2021

@author: dekom
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
        self.openTree()
        
        
    def openTree(self):
        tree = self.tree
        openedNode = [tree.getRoot()]
        ac = self.position
        tc = self.target
        while openedNode:
            #check if the Node should be open
            node = openedNode.pop(0)
            while node == None: #skip None
                node = openedNode.pop(0)
            if node.getIsLeaf():
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
                if dist <= 2**(node.getDepthFromBottom()) or dist2 <= 2**(node.getDepthFromBottom()): #open the Node
                    openedNode.extend(tree.openNode(node))
        return tree

    def getCurrentNode(self):
        return self.currentNode
    
    def getTargetNode(self):
        return self.targetNode
    
    
        
    def move(self, step):
        self.position = step
    
"""        
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
        """
    