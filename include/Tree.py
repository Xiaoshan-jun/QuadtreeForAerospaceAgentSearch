# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:27:48 2021
Tree Class save the root node which represents the whole world.
Tree Class has functions that create all the nodes.
@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""
from include.Node import Node
import matplotlib.pyplot as plt
import matplotlib.colorbar as cbar
import numpy as np
import time

class Tree(object): 
    def __init__(self, maxDepth,obstacleMap, reserveMap ,moveCostMap):
        self.root = Node(maxDepth, 0, [0,0], pow(2,maxDepth), None, None) #root of the tree, root's depth is 0, pow(2, self.maxDepth) is the size of the world.
        self.maxDepth = maxDepth #max depth of the tree
        self.openTree() #create all the quadnodes in this world
        self.loadCost(obstacleMap, reserveMap ,moveCostMap) #save all the cost values into the node
        
    #root node calls the addChild() function, which described in Node.py. All the nodes are created
    def openTree(self):
        print("building tree....")
        time_start=time.time()
        self.root.addChild()
        time_end = time.time()
        print('building tree',time_end-time_start,'s')
    
    #load the cost value of nodes
    #--------------------------------------------
    #input:
        #costMap: the size is (x,x), x denotes the length of one edge of this square world. The pre-defined map record the cost value of responded area.
        #moveCostMap: the size is (x,x,8), x denotes the length of one edge of this square world. 8 is the 8 different direction.
        #The pre-defined map records the cost of leaving each area by each direaction.
    #---------------------------------------------
    def loadCost(self, obstacleMap, reserveMap, moveCostMap):
        print("loading cost map....")
        time_start=time.time()
        plt.figure(figsize = (self.maxDepth*1.1, self.maxDepth*1.1), dpi=300)
        ax = plt.axes() 
        for i in range(pow(2, self.maxDepth)): #pow(2, self.maxDepth) is the size of the world.
            for j in range(pow(2, self.maxDepth)):
                node = self.locateNode(i+0.1,j+0.1) #because i,j is on vertex, so we increase a bit. e.g. [0,0] represent the place formed by vertex [0,0] [0,1],[1,0],[1,1]
                if obstacleMap[i][j] == 1:
                    node.updateCostLeaf(1000)
                    node.updateMoveCost(moveCostMap[i][j])
                    ax.add_patch(node.drawSquare())
                else:
                    #node.updateCostLeaf(reserveMap[i][j]) #see Node.py
                    node.updateMoveCost(moveCostMap[i][j]) #see Node.py
                    ax.add_patch(node.drawSquare())
                #ax = plt.gca().add_patch(node.drawSquare())
                
        plt.axis('scaled') 
        plt.title('Obestacle map') 
        plt.show() #draw the cost value picture TO DO: add colorbar 
        time_end = time.time()
        print('loading cost map',time_end - time_start,'s')

        
                
    #return root
    def getRoot(self):
        return self.root
        
    #find the leaf node that represents the input position.
    def locateNode(self, x, y):
        currentNode = self.root
        while currentNode.isLeaf != True:
            nodeCenter = currentNode.getCenter()
            xc = nodeCenter[0]
            yc = nodeCenter[1]
            #SW
            if x <= xc and y <= yc:
                currentNode = currentNode.getChild(0)
            #SE
            if x > xc and y <= yc:
                currentNode = currentNode.getChild(1)
            #NW
            if x <= xc and y > yc:
                currentNode = currentNode.getChild(2)
            #NE
            if x > xc and y > yc:
                currentNode = currentNode.getChild(3)
        return currentNode
    
        

