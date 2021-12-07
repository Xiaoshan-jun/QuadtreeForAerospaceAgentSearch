# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 03:21:11 2021

@author: Jun Xiang
"""
import numpy as np

class Obstacle(object):
    def __init__(self):
        self.map = np.zeros((512,512))

        
    def getMap(self):
        return self.map
    
    def rectangle(self, x, y , width, height):
        for i in range(x, x + width):
            for j in range(y , y + height):
                self.map[i][j] = 1
    
    def triangle(self, x, y, width):
        for i in range(x, x + width):
            for j in range(y, y + i - x ):
                self.map[i][j] = 1
    
    def triangleR(self, x, y, width):
        for i in range(x, x + width):
            for j in range(y - i + x, y ):
                self.map[i][j] = 1
    
    def Lbuilding(self, x, y, width, height): 
        for i in range(x, x + height):
            for j in range(y ,y + 2*height):
                self.map[i][j] = 1        
    
        for i in range(x + height, x + height + width):
            for j in range(y, y + height):
                self.map[i][j] = 1
                
    def LbuildingR(self, x, y, width, height): 
        for i in range(x + width, x + height + width):
            for j in range(y- 2*height, y):
                self.map[i][j] = 1        
    
        for i in range(x, x + height + width):
            for j in range(y, y + height):
                self.map[i][j] = 1
                

    def diamond(self, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y + i - x, y + height + i - x):
                self.map[i][j] = 1
                
    def diamondR(self, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y - i + x, y + height - i + x):
                self.map[i][j] = 1

