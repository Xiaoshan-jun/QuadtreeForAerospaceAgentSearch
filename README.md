# Quadtree for Aerospace Agent Search
this repository we release code from the papers

- [Hybrid Multiscale Search for Dynamic Planning of Multi-Agent Drone Traffic](https://arc.aiaa.org/doi/full/10.2514/1.G007343)
![](https://github.com/Xiaoshan-jun/QuadtreeForAerospaceAgentSearch/blob/main/paper/figure/jdcgpapergif.gif)
## Usage
main.py will do the following
1. generate the simulated airspace
2. generate random tasks for agents
3. assign tasks to the agents
4. create the **dynamicEnv**
5. record experience results

search mode switch:
include/agent.py, modify the function searchAndPlot() at line 52. 
## Description
to navigate the flight agent, we transfer airspace to a grid world. 

the proposed quadtree A* search algorithm can divide the airspace in multiple vary grids. The more important partial of airspace will be divided into a larger amount of grid(each grid is smaller and accurate), and the less important partial of airspace will be divided into a smaller amount of grid(each grid is larger and inaccuate). 

then, we can decrease the search space and search time while keep optimization. 


## Important function for search algorithm
DynamicEnv.py: DynamicEnv manages all the agents and the airspace
This manager can receive the move plan from all the agents, and approve the move for a specific time. 
Meanwhile, this manager can publish all the air space control information. Reserve the airspace the agents should not enter.

agent.py: agent has function divide the airspace into nodes with quadtree method. the agent can find a path to the destination with search methods, reserve some space, and save the move plan.

Node.py: Nodes represent areas in the world. Each parent node has four children.  Node saves the location of the area, the cost to reach this area, and the cost to leave this area and the number of available space.

obstacle.py: creat the global reservedMap, which is a 2d-array save the map information. Agent, DynamicEnv, Node share a same array.

astar.py: A* functions for MSA* search

astarastar.py: A* functions for A* search


### Dependencies
python 3.7

numpy

matplotlib

time

random

## Authors

@author:Jun Xiang 

@email: jxiang@ucsd.edu, jxiang9143@sdsu.edu 



## Bibtex

```
@article{xiang2023hybrid,
  title={Hybrid Multiscale Search for Dynamic Planning of Multi-Agent Drone Traffic},
  author={Xiang, Jun and Chen, Jun and Liu, Yanchao},
  journal={Journal of Guidance, Control, and Dynamics},
  volume={46},
  number={10},
  pages={1963--1974},
  year={2023},
  publisher={American Institute of Aeronautics and Astronautics}
}
```

