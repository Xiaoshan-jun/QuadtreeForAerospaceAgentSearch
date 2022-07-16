# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:12:55 2022

@author: dekom
"""
import multiprocessing
import random
import numpy as np

class DynamicEnv(object):
    def __init__(self, reservedMap, agentList):
        self.t = 0
        self.reservedMap = reservedMap
        self.agentList = agentList
        self.regularAirplane()
        
    def step(self):
        fn = "history/time" + str(self.t) + '.csv'
        np.savetxt(fn, self.reservedMap, delimiter=',')
        #check if the agent have path ready and let agent fly
        for agent in self.agentList:
            if agent.arrive:
                #fn = "history/agent" + str(agent.agentNumber) + '.csv'
                #np.savetxt(fn, agent.history, delimiter=',')
                self.agentList.remove(agent)                
            if agent.bestPath != False:
                agent.move()
        #update reserved map according to the air space control
        if self.t % 30 == 0:
            self.airspaceControl()
        if self.t % 60  == 0:
            self.regularAirplane()
        #
        print("time: ", self.t)
        self.t = self.t + 1
        
    def airspaceControl(self):
        #clear previous airspaceControl
        for i in range(len(self.reservedMap)):
            for j in range(len(self.reservedMap[i])):
                if self.reservedMap[i][j] == 100:
                    self.reservedMap[i][j] = 0
        #random airspace control
        random.seed(self.t)
        #how many air space control event        
        N = random.randint(0, 12)
        for i in range(N):
            x = random.randint(10, 500)
            y = random.randint(10, 500)
            width = random.randint(10, 50)
            length = random.randint(10, 50)
            for i in range(x, x + width):
                for j in range(y , y + length):
                    if i < len(self.reservedMap) and j < len(self.reservedMap):
                        if self.reservedMap[i][j] != 99:
                            self.reservedMap[i][j] = 100
        #regular 
    def regularAirplane(self):
        for i in range(60, 452):
            self.reservedMap[i][251] = 100
            self.reservedMap[i][260] = 100
        for j in range(60, 452):
            self.reservedMap[251][j] = 100
            self.reservedMap[260][j] = 100
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            