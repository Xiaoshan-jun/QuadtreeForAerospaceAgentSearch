# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:32:45 2021

@author:Jun Xiang 
@email: jxiang9143@sdsu.edu 
"""

from include.Tree import Tree
from include.agent import agent
import numpy as np

"""
Generate path information
"""

costMap = np.random.random((32,32))*10
moveCostMap = np.random.random((32,32,8))*10
original_tree = Tree(5, costMap, moveCostMap)
tree = original_tree
node = original_tree
agent1 = agent(tree, [2,2],[30,30])
list1 = agent1.findRequiredNode()
agent1.drawGraph()




