# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:12:55 2022
DynamicEnv manages all the agents and the airspace
This manager can receive the move plan from all the agents, and approve the move for a specific time. 
Meanwhile, this manager can publish all the air space control information. Reserve the airspace the agents should not enter.
@author: Jun Xiang
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
        self.controltime = 0
        
    def step(self):
        #fn = "history/time" + str(self.t) + '.csv'
        #np.savetxt(fn, self.reservedMap, delimiter=',')
        #check if the agent have path ready and let agent fly
        for agent in self.agentList:
            if agent.arrive:
                fn = "history/agent" + str(agent.agentNumber) + '.csv'
                np.savetxt(fn, agent.history, delimiter=',')
                self.agentList.remove(agent)                
            if agent.bestPath != False:
                agent.move()
        #update reserved map according to the air space control
        
        if self.controltime == 0:
            self.airspaceControl()
            fn = "history/reservedMap" + str(self.t + 1) + '.csv'
            np.savetxt(fn, self.reservedMap, delimiter=',')
        else:
            self.controltime = self.controltime - 1
        if self.t % 200  == 0:
            self.regularAirplane()
            fn = "history/reservedMap" + str(self.t + 1) + '.csv'
            np.savetxt(fn, self.reservedMap, delimiter=',')
        if (self.t - 100)% 200  == 0:
            self.regularAirplanePause()
            fn = "history/reservedMap" + str(self.t + 1) + '.csv'
            np.savetxt(fn, self.reservedMap, delimiter=',')
        #
        print("time: ", self.t)
        self.t = self.t + 1
        
    def airspaceControl(self):
        #clear previous airspaceControl
        self.controltime = random.randint(15, 45)
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
            self.reservedMap[i][251] = 101
            self.reservedMap[i][260] = 101
        for j in range(60, 452):
            self.reservedMap[251][j] = 101
            self.reservedMap[260][j] = 101
            
    def regularAirplanePause(self):
        for i in range(60, 452):
            self.reservedMap[i][251] = 0
            self.reservedMap[i][260] = 0
        for j in range(60, 452):
            self.reservedMap[251][j] = 0
            self.reservedMap[260][j] = 0
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            