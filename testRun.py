# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:32:45 2021

@author: dekom
"""

from include.Tree import Tree
from include.agent import agent

"""
Generate path information
"""


original_tree = Tree(6)
tree = original_tree
tree.createAgent([5,27], [28,3])
#tree.createAgent([12,27], [26,30])
mapReady = tree.drawGraph()






