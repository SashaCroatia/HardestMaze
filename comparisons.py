'''
This file will contain code for performing your comparisons. It should perform (or have a setting that lets us perform) ***ALL*** your comparisons when run. 
We recommend adding the ability to run a subset of the comparisons for testing purposes (as illustrated below). 
'''
import problems as prb
import numpy as np

#Setup
#=================
#INSTRUCTORS: if you want to run all comparisons, change value below to True (warning: may take a while)
perform_all = False
if perform_all == True:
  #what's used in my experiments
  creations = 30 #number of observations in each experiment
  dimension = 6 #dimension of mazes used in my experiments
else:
  #subset: for testing purposes only (feel free to modify)
  creations = 2
  dimension = 6

print("Experiment 1 - Longest Path")
print("===========================")
metric = 'nodepath'
p1 = 0.86
p2 = 0.1
max_iter = 400
method_created = []
for method in ['dfs', 'ucs', 'greedy', 'astar']:
  created = []
  np.random.seed(10)
  for creation in range(creations):
    #Define dimensions of empty grid
    Maze = prb.Maze(dimension,dimension)

    #Generate starting maze
    maze = Maze.gen_maze_adversarial(None, metric, p1, p2, method, True, max_iter, 2, False, False)

    #Modify that maze
    maze = Maze.gen_maze_adversarial(maze, metric, 1, 0.05, method, True, max_iter, dimension, False, False) #30

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
print("\nSummary statistics: 4 rows for each method. 2 subrows = avg, std of tuple data")
print(method_created)


print("\n\nExperiment 2 - Most Nodes Visited")
print("===========================")
metric = 'node'
p1 = 0.86
p2 = 0.1
max_iter = 200
method_created = []
for method in ['dfs', 'ucs', 'greedy', 'astar']:
  created = []
  np.random.seed(10)
  for creation in range(creations):
    #Define dimensions of empty grid
    Maze = prb.Maze(dimension,dimension)

    #Generate starting maze
    maze = Maze.gen_maze_adversarial(None, metric, p1, p2, method, True, max_iter, 2, False, False)

    #Modify that maze
    maze = Maze.gen_maze_adversarial(maze, metric, 1, 0.05, method, True, max_iter, dimension, False, False) #30

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
print("\nSummary statistics: 4 rows for each method. 2 subrows = avg, std of tuple data")
print(method_created)


print("\n\nExperiment 3 - Most Dead-Ends")
print("===========================")
metric = 'deadend'
p1 = 0.92
p2 = 0.02
max_iter = 200
method_created = []
for method in ['dfs', 'ucs', 'greedy', 'astar']:
  created = []
  np.random.seed(10)
  for creation in range(creations):
    #Define dimensions of empty grid
    Maze = prb.Maze(dimension,dimension)

    #Generate starting maze
    maze = Maze.gen_maze_adversarial(None, metric, p1, p2, method, True, max_iter, 2, False, False)

    #Modify that maze
    maze = Maze.gen_maze_adversarial(maze, metric, 1, 0.05, method, True, max_iter, dimension, False, False) #30

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
print("\nSummary statistics: 4 rows for each method. 2 subrows = avg, std of tuple data")
print(method_created)