'''
This file will contain the code needed to run a demonstration of your project. 

For the progress report, it should contain code that shows a breif demonstration of random agents attempting to solve each problem. 

For the final report, it should contain code that shows a breif demonstration of each algorithm attempting to solve each problem. 

In both cases, to make sure we can grade these all in time, please ensure that each demonstration is just long enough to show some
meaningful behavior. If your problem is chess playing, for example, you might show 5 moves from each player, where one player uses one 
algorithm and one player uses another. If your problem is snake, you might show game long enough for the player to eat two apples or die
(whichever comes first).
'''
import problems as prb


#To be set by User:
#------------------------
#Define dimensions of empty grid
Maze = prb.Maze(6,6)

#Define metric ('nodepath', 'node', 'deadend')
metric = 'nodepath'

#Define Method ('astar', 'dfs', 'ucs', 'greedy')
method = 'ucs'
#------------------------


if metric == 'nodepath':
    p1 = 0.86
    p2 = 0.1
    max_iter = 400
elif metric == 'node':
    p1 = 0.86
    p2 = 0.1
    max_iter = 200
elif metric == 'deadend':
    p1 = 0.92
    p2 = 0.02
    max_iter = 200
else:
    #metric == 'path'
    p1 = 0.85
    p2 = 0.15
    max_iter = 200

#Generate starting maze
maze = Maze.gen_maze_adversarial(None, metric, p1, p2, method, True, max_iter, 2, False)

#Modify that maze
maze = Maze.gen_maze_adversarial(maze, metric, 1, 0.05, method, True, max_iter, 6, False) #30

#Solve that maze
print(f"metric = {metric} | method = {method} | path len, nodes explored, dead ends = {Maze.solve_maze(maze, method, True, 0)}")