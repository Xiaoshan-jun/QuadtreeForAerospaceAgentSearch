# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 03:21:11 2021

@author: Jun Xiang
"""
import numpy as np

class obstacle(object):
    def __init__(self):
        self.map = np.zeros((512,512))
        
    def getMap(self):
        return self.map
    
    def Lbuilding(self, x, y, size): 
        for i in range(x, x + 5*size):
            for j in range(y ,y + 10*size):
                self.map[i][j] = 1        
    
        for i in range(x , x + 30*size):
            for j in range(y, y + 5*size):
                self.map[i][j] = 1
                
    def circle(self, x, y, radius):
        for i in range(x, x + radiu):
            for j in range(y, y + i - x):
                self.map[i][j] = 1



obstacleMap = np.zeros((1024,1024))
for i in range(0,5):
    for j in range(57,62):
        obstacleMap[i][j] = 1        

for i in range(0,35):
    for j in range(50,57):
        obstacleMap[i][j] = 1

for i in range(3,128):
    a = [ 9 ,10, 11, 12, 13, 14, 15]
    for j in a:
        obstacleMap[i][j] = 1

for i in range(15,20):
    for j in range(20,30):
        obstacleMap[i][j] = 1
        
for i in range(35,39):
    for j in range(35,50):
        obstacleMap[i][j] = 1
        
        
for i in range(38,52):
    for j in range(25,29):
        obstacleMap[i][j] = 1
        


for i in range(0,90):
    a = [78, 79 ,80, 81]
    for j in a:
        obstacleMap[i][j] = 1
for i in range(100,105):
    for j in range(90,125):
        obstacleMap[i][j] = 1