# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 01:33:34 2022

@author: dekom
"""
from include.astarastar import aStarSearch
import time

class astaragent(object): 
    
    def __init__(self, agentNumber, position, target, maxDepth, reservedMap):
        #definition: initial the agent
        #Parameters: tree: search tree #position: the agent's current position #target: the agent's goal position 
        #eDistance: the alpha in the determing function, decide the resolution #plotb: if plot the path
        #Returns: None
        self.agentNumber = agentNumber
        self.maxDepth = maxDepth
        self.position = position #current position of agent in (x, y)
        self.target = target #current target position in (x, y)
        self.bestPath = False #false means need to search, True means searching, 
        self.reservedMap = reservedMap
        self.history = []
        self.arrive = False
        self.searchtime = 0
    
    def searchAndPlot(self):
        #definition: find the required nodes.
        #save the results of the search
        time_start = time.time()
        #print('searching the best path...')
        if self.bestPath != False:
            return self
        self.arrive = self.ifArrive()
        if self.arrive == False:
            actionList, path, nodeList, count, explored = aStarSearch(self.position, self.target, self.reservedMap, self.maxDepth)
            if path == False:
                self.setBestPath(path)
                return False
            self.setBestPath(path)
            #reserve
            for n in path:
                self.reservedMap[n] = self.agentNumber
        time_end = time.time()
        self.searchtime += time_end - time_start
        #self.plotTree()
        return self
    
    def move(self):
        #definition: move the agent to the new position
        #Parameters: step: how many steps the agent will go along the path
        #Returns: None
        self.arrive = self.ifArrive()
        if self.arrive == False:
            #check path movable
            moveable = True
            for n in self.bestPath:
                if self.reservedMap[n] != self.agentNumber:
                    moveable = False
            if moveable:
                self.reservedMap[self.position] = 0
                self.position = self.bestPath.pop(0)
                self.history.append(self.position)
                print("agent", self.agentNumber, " has arrived ",self.position )
            else:
                #cancel previous resercation
                for n in self.bestPath:
                    if self.reservedMap[n] == self.agentNumber:
                        self.reservedMap[n] = 0
                self.bestPath = False
                print("agent", self.agentNumber, " is blocked, redo search ")
                

        else:
            print("agent", self.agentNumber, " has arrived")
    
    def ifArrive(self):
        if self.position[0] == self.target[0] and self.position[1] == self.target[1]:
            return True
        else:
            return False
    
    def setBestPath(self, bestPath):
        #set the best path
        self.bestPath = bestPath
    
