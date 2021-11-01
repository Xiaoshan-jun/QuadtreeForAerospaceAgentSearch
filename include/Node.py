# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 14:38:19 2021

@author:Jun Xiang 
"""
from matplotlib.pylab import *
import matplotlib.cm as cm
import matplotlib.patches as patches


class Node(object):
    def __init__(self, maxDepth, depth, vertex, size, parent, position):
        self.maxDepth = maxDepth
        self.eOccupy = 0 #expected number of how many airplane will reserve this node
        self.capacity = 1 * pow(4, maxDepth - depth)
        self.depth = depth #depth in the tree
        self.depthFromBottom = maxDepth - depth
        self.parent = parent
        self.positionInParentNode = position
        # 0 denotes SW(bottom-left), 1 denotes SE(bottom-right), 2 denotes NW(top-left), 3 denotes NE(top east)
        self.children = {"0":None,
                         "1":None,
                         "2":None,
                         "3":None,   } #children dictionary 
        self.neibor = {"NW" : None,
                       "N" : None,
                       "NE" : None,
                       "W" : None,
                       "E" : None,
                       "SW" : None,
                       "S" : None,
                       "SE" : None
            } #N means the neibor which is above the current node, S: below, E: right, W: left
        self.isOpen = False
        self.isLeaf = depth == maxDepth #whether that node is a leaf of the tree
        self.vertex = vertex #vertex is the position of the bottom left of the vertex
        self.center = [vertex[0] + 1/2 *size,  vertex[1] + 1/2 *size]
        self.vertex_ne =  [vertex[0] + size,  vertex[1] + size] #vertex is the position of the top right of the vertex
        self.size = size #size is the length of the side of square the node represents
        self.cost = 1
        

    def clear(self):
        self.children["0"] = None
        self.children["1"] = None
        self.children["2"] = None
        self.children["3"] = None
        self.isLeaf = True
    #create a new children at position i with value val
        return None
        
    def addChild(self):
        if self.isLeaf == False and self.isOpen == False:
            self.isOpen = True
        # 0 denotes SW, 1 denotes SE, 2 denotes NW, 3 denotes NE
 #add SW child node, vertex is the same as the parent node
            self.children["0"] = Node(self.maxDepth, self.depth + 1, self.vertex, self.size/2, self, 0)
#add SE child node, x of vertex increased,  and y remains same
            self.children["1"] = Node(self.maxDepth, self.depth + 1, [self.vertex[0] + self.size/2, self.vertex[1]], self.size/2, self, 1)
#add NW child node, x of vertex is same,  and y increase
            self.children["2"] = Node(self.maxDepth, self.depth + 1, [self.vertex[0], self.vertex[1] + self.size/2], self.size/2, self, 2)
#add NE child node, x and y increase
            self.children["3"] = Node(self.maxDepth, self.depth + 1, [self.vertex[0] + self.size/2 , self.vertex[1] + self.size/2], self.size/2, self, 3)
            return self.children[str(0)], self.children[str(1)], self.children[str(2)], self.children[str(3)]
        elif self.isLeaf == False:
            return self.children[str(0)], self.children[str(1)], self.children[str(2)], self.children[str(3)]

    #checks if child i exists
    def childExists(self, i):
        return self.childExists[i]
        
    #returns child i - creates it if it does not exists
    def getChild(self, i):
        return self.children[str(i)]
    
    def getallChild(self):
        return self.children[str(0)], self.children[str(1)], self.children[str(2)], self.children[str(3)]
    
    def drawSquare(self): 
        my_cmap = cm.get_cmap('jet')
        min_val = 0
        max_val = 50
        norm = matplotlib.colors.Normalize(min_val, max_val)
        color_i = my_cmap(norm(self.cost))
        square = plt.Rectangle(self.vertex, self.size, self.size, fc=color_i,ec="red")
        return square
    
    def drawAgent(self):
        cycle = plt.Circle(self.center,0.35, fc='yellow',ec="red")
        return cycle
    
    def drawTarget(self):
        cycle = plt.Circle(self.center,0.35, fc='green',ec="red")
        return cycle
    """
    find the neibor node in the opened tree. Each node has 8 different neibors.
    """    
    def findNeibor(self):
        #find NW Neibor
        if self.positionInParentNode == 0: #SW
            if self.veterx[0] == 0: #if the node is located at the left edge of the world
                self.neibor["NW"] = None
                self.neibor["W"] = None
                self.neibor["SW"] = None
            elif self.veterx[1] == 0:  #if the node is located at the bottom edge of the world
                self.neibor["SW"] = None
                self.neibor["S"] = None
                self.neibor["SE"] = None
            else:
                #find NW Neibor    
                self.parent. 
                self.neibor["NW"] 
            
            
    #update the current node according to its children, if rec=true, descendant are first updated (full update of the subtree)
    def update(self, rec, prune = True):
        if(self.isLeaf()):
            return self.val
        #pruning variables
        prunable = prune 
        prevVal = -1
        #update
        sumValue = 0
        for i in range(4):
            if self.childExists(str(i)):
                cNode = self.children[str(i)]
                if(rec):
                    cNode.update(rec, prune)
                sumValue += cNode.getValue()
                if(prunable):
                    if prevVal == -1:
                        prevVal = cNode.getValue()
                    elif prevVal != cNode.getValue() or not cNode.isLeaf():
                        prunable = False
            else: 
                prunable = False;          
        self.val = sumValue/4;
        if(prunable):
            self.clear()
            self.isLeaf = True
        return self.val
                
    
    def occupyPlan(self, eOccupy):
        #if it is the smallest space, add estimated occupy to the node.
        if self.isLeaf:
            self.eOccupy += eOccupy
        else:
        #find avaliable child nodes, return False if no avaliable child nodes
            acn1 = 0 #real acn
            acn2 = 4 #predicted acn
            #check how many node has 1/4 space first, if not every node has space, check how many node has 1/acn1
            while True:
                for i in range(3): 
                    a = self.getChild(i)
                    spaceLeft = a.capacity - a.eOccupy
                    if spaceLeft > eOccupy/acn2:
                        acn1 += 1
                if acn1 == acn2 or acn1 == 0:
                    break
                else: 
                    acn2 = acn1
                    acn1 = 0
            if acn1 == 0: #if tell parent eOccupy can not be added
                return False
            else:
                for i in range(3): 
                    a = self.getChild(i)
                    spaceLeft = a.capacity - a.eOccupy
                    if spaceLeft > eOccupy/acn1:
                        a.eOccupyPlan(eOccupy/acn1)
                self.eOccupy += eOccupy
                return True #tell parent eOccupy is successful added
    
    #return the value val_ of the node
    def getValue(self):
        return self.val
    ##return the value val_ of the node
    def getIsLeaf(self):
        return self.isLeaf
    #returns the depth of the node in the tree
    def getDepth(self):
        return self.depth
    
    def getmaxDepth(self):
        return self.maxDepth
        
    def getVertex(self):
        return self.vertex[0], self.vertex[1], self.vertex_ne[0], self.vertex_ne[1]
    
    def getCenter(self):
        return self.center

    def getParent(self):
        return self.parent
    
    def getDepthFromBottom(self):
        return self.depthFromBottom
    
    def findReachableNode(self, avaliableNodeList):
        return None
    
    def openable(self):
        return self.isOpen == False and self.isLeaf == False
    
    def mapReady(self):
        return self.isOpen == False
        



