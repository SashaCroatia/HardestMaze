'''
This file will contain code for performing your comparisons. It should perform (or have a setting that lets us perform) ***ALL*** your comparisons when run. 
We recommend adding the ability to run a subset of the comparisons for testing purposes (as illustrated below). 
'''
import problems as prb
import numpy as np

#Setup
#=================
methods = ['dfs', 'ucs', 'greedy', 'astar']
creations = 2 #number of maze creations per method
np.random.seed(10)

#Experiment 1
#=================
metric = 'nodepath'
method_created = []
for method in methods:
  if method == 'ucs':
      p1 = 0.85
      p2 = 0.05
  else:
      p1 = 1
      p2 = 0.05
  max_iter = 400
  created = []
  for creation in range(creations):
    #Define dimensions of empty grid
    Maze = prb.Maze(7,7)

    #Generate starting maze
    maze = Maze.gen_maze_adversarial(None, metric, p1, p2, method, True, max_iter, 2, False, False)

    #Modify that maze
    maze = Maze.gen_maze_adversarial(maze, metric, 1, 0.05, method, True, max_iter, 10, False, False) #30

    #Solve that maze
    result = Maze.solve_maze(maze, method, False, 0)
    created.append(result)
    print(f"method = {method} | path len, nodes explored, dead ends = {result}")
  
  #Compute summary stats
  created = np.array(created)
  means = np.mean(created, axis = 0)
  stds = np.std(created, axis = 0)
  method_created.append(np.array([means, stds]))

method_created = np.array(method_created)
print(method_created)




#Experiment 2
#=================

#Experiment 3
#=================