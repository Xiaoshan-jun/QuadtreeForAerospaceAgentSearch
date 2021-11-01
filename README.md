# Quadtree for Aerospace Agent Saearch
Quadtree represents a 2d grid-base world

## Description
Node.py: Nodes represent areas in the world. Each parent node has four children.  Node saves the location of the area, the cost to reach this area, and the cost to leave this area.

Tree.py: Tree save the root node which represents the whole world. Tree Class has functions that create all the nodes.

agent.py: agent pick the appropriate nodes and build the path graph as we want. The path graph shoule be able to further used by search algorithm.

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

you should be fine if you can understand how **testRun.py** work

all the code is comment, please contact me if you have any question.

### Dependencies
python 3.7

numpy

matplotlib

## Authors

@author:Jun Xiang 

@email: jxiang9143@sdsu.edu 

## Version History

* 0.1
    * Initial Release



## Acknowledgments


