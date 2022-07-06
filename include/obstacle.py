# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 03:21:11 2021

@author: Jun Xiang
"""
import numpy as np

class Obstacle(object):
    def __init__(self, d, t):
        self.map = np.zeros((2**d,2**d))
        if d == 9:
            self.plusbuilding(50, 50, 410, 410, 120, 120, 1)
            self.rectangle(250, 15, 10, 20)
            self.rectangle(250, 482, 10, 20)
            self.rectangle(15, 250, 20, 10)
            self.rectangle(482, 250, 20, 10)
        if d == 10:
            self.plusbuilding(100, 100, 820, 820, 240, 240, 1)
            self.rectangle(500, 30, 20, 40)
            self.rectangle(500, 980, 20, 40)
            self.rectangle(30, 500, 40, 20)
            self.rectangle(980, 500, 40, 20)
            if t == 10:
                self.rectangle(300, 0, 20, 100)
        
        
    def getMap(self):
        return self.map
    
    def plusbuilding(self, x, y, width, length, width2, length2,  o):
        #width1 and length1 is the size of big square
        #width 2 and length 2 is the size of small empty square in the four corner
        for i in range(x, x + width):
            for j in range(y , y + length):
                self.map[i][j] = o
        for i in range(x, x + width2):
            for j in range(y , y + length2):
                self.map[i][j] = 0 #lb
        for i in range(x, x + width2):
            for j in range(y + length - length2 , y + length):
                self.map[i][j] = 0 #lt
        for i in range(x + width - width2, x + width):
            for j in range(y , y + length2):
                self.map[i][j] = 0 #rb
        for i in range(x + width - width2, x + width):
            for j in range(y + length - length2 , y + length):
                self.map[i][j] = 0 #rt               
                
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

