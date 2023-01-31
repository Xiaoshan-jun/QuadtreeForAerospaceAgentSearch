# Quadtree for Aerospace Agent Saearch
Quadtree represents a 2d grid-base world

## Description
DynamicEnv.py: DynamicEnv manages all the agents and the airspace
This manager can receive the move plan from all the agents, and approve the move for a specific time. 
Meanwhile, this manager can publish all the air space control information. Reserve the airspace the agents should not enter.

agent.py: agent has function divide the airspace into nodes with quadtree method. the agent can find a path to the destination with MRA*, reserve some space, and save the move plan.

Node.py: Nodes represent areas in the world. Each parent node has four children.  Node saves the location of the area, the cost to reach this area, and the cost to leave this area and the number of available space.

global reservedMap: it is a 2d-array save the map information. Agent, DynamicEnv, Node share a same array.




## Important function for search algorithm
Tree(maxDepth,costMap, moveCostMap): Create the Tree. costMap/moveCostMap is predefined map property. maxDepth determined the size of the world. for example, if the size of world is 32*32, the maxDepth should be 5.

agent(tree, position, target): Create the agent. **position** is the agent's start position, **target** is the destination of the agent.

agent.getRequiredNode(): get all the node we need to build the path graph

agent.getGraph(): get path graph

agent.getCurrentNodeIndex(): get the index denotes the agent currently locate

agent.getTargetNodeIndex(): get the index denotes the node the target currently locate

agent.move(step): move the agent to desired position

## Getting Started
*testRun.py is the sample code show how we build the path graph and move agent on the graph

you should be fine if you can understand how **testRunAstar** work. If you run it correctly, the output results should look like:

![alt text](https://github.com/Xiaoshan-jun/QuadtreeForAerospaceAgentSearch/blob/main/Figure%202021-11-01%20165843.png)


all the code is comment, please contact me if you have any question. 


### Dependencies
python 3.7

numpy

matplotlib

## Authors

@author:Jun Xiang 

@email: jxiang@ucsd.edu, jxiang9143@sdsu.edu 



## Acknowledgments
related paper
Dynamic Unmanned Aircraft System Traffic Volume Reservation Based on Multi-Scale A* Algorithm 
https://arc.aiaa.org/doi/10.2514/6.2022-2236

