# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:27:48 2021
original C
Created on: Feb 18, 2015
 *      Author: florian
@author: Jun Xiang 
"""
from include.Node import Node
from include.agent import agent
import matplotlib.pyplot as plt
import numpy as np
class Tree(object): 
    def __init__(self, maxDepth):
        self.root = Node(maxDepth, 0, [0,0], pow(2,maxDepth), None, None) #root of the tree, root is depth 0
        self.maxDepth = maxDepth #max depth of the tree
        self.allNode = [self.root]
        self.agentList = []
        
    def createAgent(self, position, target):
        self.agentList.append(agent(self, position, target))
        
    def drawGraph(self):
        plt.axes()
        mapReadyNode = []
        for node in self.allNode:
            if node.mapReady():
                plt.gca().add_patch(node.drawSquare())
                mapReadyNode.append(node)
        for agent in self.agentList:
            plt.gca().add_patch(agent.getCurrentNode().drawAgent())
            plt.gca().add_patch(agent.getTargetNode().drawTarget())
        plt.axis('scaled')
        plt.show()
        return mapReadyNode
    

    def getAgent(self, i):
        return self.agentList[i]

    def openNode(self, node):
        if node.openable:
            n1, n2, n3, n4 = node.addChild()
            self.allNode.append(n1)
            self.allNode.append(n2)
            self.allNode.append(n3)
            self.allNode.append(n4)
            return n1,n2,n3,n4
        else:
            return None
    
    def getRoot(self):
        return self.root
        
    def getAllNode(self):
        return self.allNode
    
        
    def copyWaveletTransform(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.wavelet_coefficients.append(float(line))
        N = 7
        self.recursiveWavelet(self.root,1, 1, self.wavelet_coefficients[0]*pow(2,-N), N);
    
    def recursiveWavelet(self, node, pt, sz, value, N):
        if sz == pow(4, self.maxDepth):
            node.setValue(abs(value))
            return None
        
        node.setValue(abs(value))
        A = value * pow(2,N)
        H = self.wavelet_coefficients[pt]
        V = self.wavelet_coefficients[pt+sz]
        D = self.wavelet_coefficients[pt+2*sz]
        side_size = np.sqrt(sz)
        m = (pt-sz)% side_size # mod(index, side_size)
        f = np.floor((pt-sz)/side_size) #floor(index/side_size)
        std_pt = 4*(side_size*f + sz) + 2*m
        for child_ind in range(4):
            if child_ind == 0:
                self.recursiveWavelet(node.getChild(0), int(std_pt+np.sqrt(sz*4)), sz*4,  pow(2,-N)*(A+H-V-D) ,N-1);
            if child_ind == 1:
                self.recursiveWavelet(node.getChild(1), int(std_pt+np.sqrt(sz*4))+1 , sz*4,  pow(2,-N)*(A-H-V+D) ,N-1 )
            if child_ind == 2:
                self.recursiveWavelet(node.getChild(2), int(std_pt), sz*4, pow(2,-N)*(A+H+V+D) ,N-1 );
            if child_ind == 3:
                self.recursiveWavelet(node.getChild(3), int(std_pt+1), sz*4, pow(2,-N)*(A-H+V-D) ,N-1 );
        return None
