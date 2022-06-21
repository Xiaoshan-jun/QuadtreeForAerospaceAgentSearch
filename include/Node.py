# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 14:38:19 2021
Node class represent areas in the world. Each parent node has four children.
Node save the location of the area, the cost to reach this area, and the cost to leave this area.
@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm
import numpy as np

class Node(object):
    def __init__(self, maxDepth, depth, vertex, size, parent, position):
        
        self.maxDepth = maxDepth 
        self.mark = 0 #the index in the nodeList
        self.reserved = 0
        self.maxCapacity = pow(4, maxDepth - depth)
        self.capacity = 1 * pow(4, maxDepth - depth) #max capacity of this node, leaf node's capacity is 1
        self.depth = depth #depth of this node in the tree
        self.depthFromBottom = maxDepth - depth
        self.parent = parent
        # 0 denotes SW(bottom-left), 1 denotes SE(bottom-right), 2 denotes NW(top-left), 3 denotes NE(top east)
        self.positionInParentNode = position 
        # 0 denotes SW(bottom-left), 1 denotes SE(bottom-right), 2 denotes NW(top-left), 3 denotes NE(top east)
        self.children = {"0":None,
                         "1":None,
                         "2":None,
                         "3":None,   } #children dictionary 
        self.childrenCount = 0
        self.moveCost = np.zeros(8) #the approximated unit cost if the agent leave this node
        #0: NW, 1:N, 2: NE, 3:W, 4:E, 5:SW 6:S,7:SE
        #N means the neibor which is above the current node, S: below, E: right, W: left
        self.isOpen = False #True its children have been generated
        self.isLeaf = depth == maxDepth #whether that node is a leaf of the tree
        self.vertex = vertex #vertex is the position of the bottom left of the vertex(vertex_sw)
        self.center = [vertex[0] + 1/2 *size,  vertex[1] + 1/2 *size]
        self.vertex_nw = [vertex[0] ,  vertex[1] + size] #vertex_nw is the position of the top left of the vertex
        self.vertex_se = [vertex[0] + size,  vertex[1]] #vertex_se is the position of the bottom right of the vertex
        self.vertex_ne = [vertex[0] + size,  vertex[1] + size] #vertex_ne is the position of the top right of the vertex
        self.size = size #size is the length of the side of square the node represents
        self.cost = 0 #cost of reach this node, in this case, cost = number of obastacles and reserve
        self.g = 1000000 #cost to come = previous g + dis + cost to stop
        self.h = 1000000# approximate cost to target
        self.gh = 1000000 #cost to come + approximate cost to target
        self.path = [] #path reach the node, for search
        self.avaliable = [] #the avaliable node can arrive from this node
        self.movingCost = [] #the avaliable node can arrive from this node
        self.importance = False
        

#recursive function
#if the root calls this function, the function will create all the nodes in the tree.
    def addChild(self):
        if self.isLeaf == False and self.isOpen == False: #check if this node can be furthur open
            self.isOpen = True 
        # 0 denotes SW, 1 denotes SE, 2 denotes NW, 3 denotes NE
            #add SW child node, vertex is the same as the parent node
            self.children["0"] = Node(self.maxDepth, self.depth + 1, self.vertex, self.size/2, self, 0)
            self.childrenCount += 1
            self.children["0"].addChild()
            #add SE child node, x of vertex increased,  and y remains same
            self.children["1"] = Node(self.maxDepth, self.depth + 1, [self.vertex[0] + self.size/2, self.vertex[1]], self.size/2, self, 1)
            self.childrenCount += 1
            self.children["1"].addChild()
            #add NW child node, x of vertex is same,  and y increase
            self.children["2"] = Node(self.maxDepth, self.depth + 1, [self.vertex[0], self.vertex[1] + self.size/2], self.size/2, self, 2)
            self.childrenCount += 1
            self.children["2"].addChild()
            #add NE child node, x and y increase
            self.children["3"] = Node(self.maxDepth, self.depth + 1, [self.vertex[0] + self.size/2 , self.vertex[1] + self.size/2], self.size/2, self, 3)
            self.childrenCount += 1
            self.children["3"].addChild()
            return self.children[str(0)], self.children[str(1)], self.children[str(2)], self.children[str(3)]
        elif self.isLeaf == False:
            #return child if the node is already open
            return self.children[str(0)], self.children[str(1)], self.children[str(2)], self.children[str(3)]
#recursive function
#update the cost of the leaf node, then all the parent node of this leaf node will be updated

    def updateCostLeaf(self, cost):
        self.cost = cost
        #parent's cost is equal to sum of its children
        if self.parent != None:
            pcost = 0
            count = 0
            for child in self.parent.getallChild():
                if child:
                    pcost += child.getCost()
                    count += 1
            self.parent.updateCostLeaf(pcost/count)
        return cost
    
    def reserve(self, reserve):
        if self.isLeaf:
            self.reserved = 1
        else:
            self.reserved += reserve
            children = self.getallChild()
            for child in children:
                if child:
                    child.reserve(reserve/self.childrenCount)
        
#recursive function
#update the moving cost of the leaf node, then all the parent node of this leaf node will be updated
    def updateMoveCost(self, pathCost):
        self.moveCost = pathCost
        if self.parent != None:
            pcost = 0
            count = 0
            for child in self.parent.getallChild():
                if child:
                    pcost += child.moveCost
                    count += 1
            self.parent.updateMoveCost(pcost/count)
    
    def removeChildren(self, position):
        self.children[str(position)] = None
        self.childrenCount -= 1
        
    def hasNoChild(self):
        children = self.getallChild()
        for child in children:
            if child:
                return False
        return True
        
    def cutLeaf(self):
        if self.isLeaf or self.hasNoChild():
            self.parent.removeChildren(self.positionInParentNode)
            self.parent.cutLeaf()
            
#get move cost for desired direction. #0: NW, 1:N, 2: NE, 3:W, 4:E, 5:SW 6:S,7:SE
    def getMoveCost(self, i):
        return self.moveCost[i]
    
    def setMoveCost(self, i, value):
        self.moveCost[i] += value
        
    #returns child i 
    def getChild(self, i):
        return self.children[str(i)]
    #return all children
    def getallChild(self):
        return self.children[str(0)], self.children[str(1)], self.children[str(2)], self.children[str(3)]
    #draw the area this node represents on the 2d world with the cost value, different color represent different cost value
    def drawSquare(self): 
        my_cmap = cm.get_cmap('Greys')
        min_val = 0
        max_val = 1000
        norm = matplotlib.colors.Normalize(min_val, max_val)
        color_i = my_cmap(norm(self.cost))
        square = plt.Rectangle(self.vertex, self.size, self.size, fc=color_i,ec="gray")
        return square
    
    def drawPathSquare(self): 
        
        my_cmap = cm.get_cmap('Greys')
        min_val = 0
        max_val = 1000
        norm = matplotlib.colors.Normalize(min_val, max_val)
        color_i = my_cmap(norm(self.cost))
        square = plt.Rectangle(self.vertex, self.size, self.size, fc=color_i,ec="red", lw=3)
        return square
    
    def drawTargetSquare(self): 
        
        my_cmap = cm.get_cmap('Greys')
        min_val = 0
        max_val = 1000
        norm = matplotlib.colors.Normalize(min_val, max_val)
        color_i = my_cmap(norm(self.cost))
        square = plt.Rectangle(self.vertex, self.size, self.size, fc=color_i,ec="green", lw=3)
        return square
    
    #draw the symbol of the agent if the agent is here
    def drawAgent(self):
        cycle = plt.Circle(self.center,0.35, fc='yellow',ec="red")
        return cycle
    #draw the symbol of the target if the target is here
    def drawTarget(self):
        cycle = plt.Circle(self.center,0.35, fc='green',ec="red")
        return cycle
        
    #return the value cost of the node
    def getCost(self):
        return self.cost
    
    ##return if the node is leaf node
    def getIsLeaf(self):
        return self.isLeaf
    
    #returns the depth of the node in the tree
    def getDepth(self):
        return self.depth
    
    #return the maxDepth of the tree
    def getmaxDepth(self):
        return self.maxDepth
    
    #return all the vertex of this node
    def getVertex(self):
        return self.vertex[0], self.vertex[1], self.vertex_ne[0], self.vertex_ne[1]
    
    #return the center position of this node
    def getCenter(self):
        return self.center
    
    #return this node's partent node
    def getParent(self):
        return self.parent
    
    #return how many layers under this nodes
    def getDepthFromBottom(self):
        return self.depthFromBottom
    
    def getSize(self):
        return self.size
    
    #return if this node is openable, may be used in the future
    def openable(self):
        return self.isOpen == False and self.isLeaf == False
    
    #return if this node should be plot, may be used in the future
    def mapReady(self):
        return self.isOpen == False
     
    #add neibor node
    def setAvaliable(self, avaliable):
        self.avaliable.append(avaliable)
        

    def setMovingCost(self, movingCost):
        self.movingCost.append(movingCost)
    
    def neibornoFound(self):
        return len(self.avaliable) == 0
        
    #set h value    
    def setH(self, h):
        self.h = h
    
    #set g value
    def setG(self, g):
        self.g = g
        
    #set gh value
    def setGH(self, gh):
        self.gh = gh

    def getCapacityPercentage(self):
        return self.capacity/self.maxCapacity
    
    def CutCapacity(self):
        self.capacity - 1
        if self.parent:
            self.parent.CutCapacity()