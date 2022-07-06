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
    def __init__(self, maxDepth, depth, vertex, size, parent, position, reservedMap, leafCapacity = 1):
        
        self.maxDepth = maxDepth 
        self.mark = 0 #the index in the nodeList
        self.reservedMap = reservedMap
        self.reserved = np.count_nonzero(self.reservedMap)
        self.maxCapacity = pow(4, maxDepth - depth)
        self.leafCapacity = leafCapacity
        self.capacity =  pow(4, maxDepth - depth) - self.reserved #max capacity of this node, leaf node's capacity is 1
        self.Cr = self.capacity/self.maxCapacity
        self.depth = depth #depth of this node in the tree
        self.depthFromBottom = maxDepth - depth
        self.parent = parent
        # 0 denotes SW(bottom-left), 1 denotes SE(bottom-right), 2 denotes NW(top-left), 3 denotes NE(top east)
        self.positionInParentNode = position 
        # 0 denotes SW(bottom-left), 1 denotes SE(bottom-right), 2 denotes NW(top-left), 3 denotes NE(top east)
        self.children = {"SW":None,
                         "SE":None,
                         "NW":None,
                         "NE":None,   } #children dictionary 
        #N means the neibor which is above the current node, S: below, E: right, W: left
        self.isLeaf = depth == maxDepth #whether that node is a leaf of the tree
        self.vertex = vertex #vertex is the position of the bottom left of the vertex(vertex_sw)
        self.center = [vertex[0] + 1/2 *size,  vertex[1] + 1/2 *size]
        self.vertex_nw = [vertex[0] ,  vertex[1] + size] #vertex_nw is the position of the top left of the vertex
        self.vertex_se = [vertex[0] + size,  vertex[1]] #vertex_se is the position of the bottom right of the vertex
        self.vertex_ne = [vertex[0] + size,  vertex[1] + size] #vertex_ne is the position of the top right of the vertex
        self.size = size #size is the length of the side of square the node represents
        self.cost = 1/(self.Cr + 0.0000001) #cost of reach this node, in this case, cost = number of obastacles and reserve
        self.g = 1000000 #cost to come = previous g + dis + cost to stop
        self.h = 1000000# approximate cost to target
        self.gh = 1000000 #cost to come + approximate cost to target
        self.path = [] #path reach the node, for search
        self.avaliable = [] #the avaliable node can arrive from this node
        self.movingCost = [] #the avaliable node can arrive from this node
        self.reserveCode = {}
        self.importance = False
        

#recursive function
#if the root calls this function, the function will create all the nodes in the tree.
    def addChild(self):
        if self.depth != self.maxDepth: #check if this node can be furthur open
            # 0 denotes SW(bottom-left), 1 denotes SE(bottom-right), 2 denotes NW(top-left), 3 denotes NE(top east)
            mid = int(self.size/2)
            self.children["SW"] = Node(self.maxDepth,  self.depth + 1, self.vertex, self.size/2, self, 0,                                                                              [i[0:mid] for i in self.reservedMap[0:mid]] ,self.leafCapacity)
            self.children["SE"] = Node(self.maxDepth,  self.depth + 1, [self.vertex[0] + self.size/2, self.vertex[1]], self.size/2, self, 1,                           [i[mid:] for i in self.reservedMap[0:mid]] , self.leafCapacity)
            self.children["NW"] = Node(self.maxDepth, self.depth + 1, [self.vertex[0] , self.vertex[1] + self.size/2], self.size/2, self, 2,                          [i[0:mid] for i in self.reservedMap[mid:]] ,  self.leafCapacity)
            self.children["NE"] = Node(self.maxDepth, self.depth + 1, [self.vertex[0] + self.size/2, self.vertex[1] + self.size/2], self.size/2, self, 3,             [i[mid:] for i in self.reservedMap[mid:]] , self.leafCapacity)
        return self.children["SW"], self.children["SE"], self.children["NW"], self.children["NE"]


    def reserve(self, agentnumber):
        self.reserveCode[agentnumber] = []
        #i = 0
        # while i < self.size:
        #     x = random.randint(0, self.size - 1)
        #     y = random.randint(0, self.size - 1)
        #     z = random.randint(0, self.size - 1)
        #     if self.reservedMap[x][y][z] == 0:
        #         self.reservedMap[x][y][z] = agentnumber
        #         self.reserveCode[agentnumber].append([x,y,z])
        #         i = i + 1
        x = round(self.size/2)
        y = round(self.size/2)
        if self.reservedMap[x][y] == 0:
            self.reservedMap[x][y] = agentnumber
            self.reserveCode[agentnumber].append([x,y])
    
                
    
    def cancel(self, agentnumber):
        #print(self.reserveCode)
        for i in self.reserveCode[agentnumber]:
            x = i[0]
            y = i[1]
            self.reservedMap[x][y] = 0
            
#get move cost for desired direction. #0: NW, 1:N, 2: NE, 3:W, 4:E, 5:SW 6:S,7:SE
    def getMoveCost(self, i):
        return self.moveCost[i]
    
    def setMoveCost(self, i, value):
        self.moveCost[i] += value
        
    #draw the area this node represents on the 2d world with the cost value, different color represent different cost value
    def drawSquare(self): 
        my_cmap = cm.get_cmap('Greys')
        min_val = 0
        max_val = 1
        norm = matplotlib.colors.Normalize(min_val, max_val)
        color_i = my_cmap(norm(1 - self.Cr))
        square = plt.Rectangle(self.vertex, self.size, self.size, fc=color_i,ec="gray")
        return square
    
    def drawPathSquare(self): 
        
        my_cmap = cm.get_cmap('Greys')
        min_val = 0
        max_val = 1
        norm = matplotlib.colors.Normalize(min_val, max_val)
        color_i = my_cmap(norm(1 - self.Cr))
        square = plt.Rectangle(self.vertex, self.size, self.size, fc=color_i,ec="red", lw = 3)
        return square
    
    def drawTargetSquare(self): 
        
        my_cmap = cm.get_cmap('Greys')
        min_val = 0
        max_val = 1
        norm = matplotlib.colors.Normalize(min_val, max_val)
        color_i = my_cmap(norm(self.Cr))
        square = plt.Rectangle(self.vertex, self.size, self.size, fc=color_i,ec="green", lw = 3)
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
        
    #set mark
    def setMark(self, mark):
        self.mark = mark