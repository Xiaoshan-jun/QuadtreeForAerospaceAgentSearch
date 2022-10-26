# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 03:21:11 2021

@author: Jun Xiang
"""
import numpy as np
import random

class obstacle(object):
    def __init__(self, d, o, k):
        self.map = np.zeros((2**d,2**d))
        random.seed(k)
        #0 is free space, 99 means permnant obstacle, 100 means temprary obstacle, 101 means regular flight
        if d == 9:
            #4 airport
            self.rectangle(50, 251, 10, 10)
            self.rectangle(452, 251, 10, 10)
            self.rectangle(251, 50, 10, 10)
            self.rectangle(251, 452, 10, 10)
            if o == 1:
                self.rectangle(50, 251, 10, 10)
                self.rectangle(452, 251, 10, 10)
                self.rectangle(251, 50, 10, 10)
                self.rectangle(251, 452, 10, 10)
                self.rectangle(100, 200, 100, 1)
                self.rectangle(100, 300, 100, 1)
                self.rectangle(300, 200, 100, 1)
                self.rectangle(300, 300, 100, 1)
                self.rectangle(300, 100, 1, 100)
                self.rectangle(300, 300, 1, 100)
                self.rectangle(200, 100, 1, 100)
                self.rectangle(200, 300, 1, 100)
            if o== 2:
                N = random.randint(12, 18)
                for i in range(N):
                    x = random.randint(0, len(self.map))
                    y = random.randint(0, len(self.map))
                    width = random.randint(len(self.map)//50, len(self.map)//10)
                    length = random.randint(len(self.map)//50, len(self.map)//10)
                    width2 = random.randint(width//7, width//3)
                    length2 = random.randint(length//7, length//3)
                    self.plusbuilding(x, y, width, length, width2, length2,  99)
            
                N = random.randint(12, 18)
                for i in range(N):
                    x = random.randint(0, len(self.map))
                    y = random.randint(0, len(self.map))
                    width = random.randint(len(self.map)//50, len(self.map)//10)
                    length = random.randint(len(self.map)//50, len(self.map)//10)
                    self.rectangle(x, y, width, length)


        
    def getMap(self):
        return self.map
    
    
    def plusbuilding(self, x, y, width, length, width2, length2,  o):
        #width1 and length1 is the size of big square
        #width 2 and length 2 is the size of small empty square in the four corner
        for i in range(x, x + width):
            for j in range(y , y + length):
                if i < len(self.map) and j < len(self.map):
                    self.map[i][j] = o
        for i in range(x, x + width2):
            for j in range(y , y + length2):
                if i < len(self.map) and j < len(self.map):
                    self.map[i][j] = 0
        for i in range(x, x + width2):
            for j in range(y + length - length2 , y + length):
                if i < len(self.map) and j < len(self.map):
                    self.map[i][j] = 0
        for i in range(x + width - width2, x + width):
            for j in range(y , y + length2):
                if i < len(self.map) and j < len(self.map):
                    self.map[i][j] = 0
        for i in range(x + width - width2, x + width):
            for j in range(y + length - length2 , y + length):
                if i < len(self.map) and j < len(self.map):
                    self.map[i][j] = 0            
                
    def rectangle(self, x, y , width, height):
        for i in range(x, x + width):
            for j in range(y , y + height):
                if i < len(self.map) and j < len(self.map):
                    self.map[i][j] = 99
    
    def triangle(self, x, y, width):
        for i in range(x, x + width):
            for j in range(y, y + i - x ):
                self.map[i][j] = 99
    
    def triangleR(self, x, y, width):
        for i in range(x, x + width):
            for j in range(y - i + x, y ):
                self.map[i][j] = 99
    
    def Lbuilding(self, x, y, width, height): 
        for i in range(x, x + height):
            for j in range(y ,y + 2*height):
                self.map[i][j] = 99       
    
        for i in range(x + height, x + height + width):
            for j in range(y, y + height):
                self.map[i][j] = 99
                
    def LbuildingR(self, x, y, width, height): 
        for i in range(x + width, x + height + width):
            for j in range(y- 2*height, y):
                self.map[i][j] = 99       
    
        for i in range(x, x + height + width):
            for j in range(y, y + height):
                self.map[i][j] = 99
                

    def diamond(self, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y + i - x, y + height + i - x):
                self.map[i][j] = 99
                
    def diamondR(self, x, y, width, height):
        for i in range(x, x + width):
            for j in range(y - i + x, y + height - i + x):
                self.map[i][j] = 99

