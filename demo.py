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
import numpy as np

#To be set by User/Instructor:
#------------------------
#Define dimensions of empty grid and max_iter for maze gen
dimension = 5 #small maze for computational speed reasons, as this is a demo. (in report used 6).
max_iter = 200 #for demo purposes. (in report used 400).
Maze = prb.Maze(dimension, dimension)
#------------------------

np.random.seed(6)
for metric in ['nodepath','node','deadend']: #path to solution, nodes in search space, num deadends
    for method in ['dfs', 'ucs', 'greedy', 'astar']: #search algo
        if metric == 'nodepath':
            p1 = 0.85
            p2 = 0.1
            max_iter = max_iter
        elif metric == 'node':
            p1 = 0.86
            p2 = 0.1
            max_iter = max_iter//2
        elif metric == 'deadend':
            p1 = 0.92
            p2 = 0.02
            max_iter = max_iter//2
        else:
            #metric == 'path'
            p1 = 0.85
            p2 = 0.15
            max_iter = max_iter//2

        print("-------------------------")
        #Generate starting maze
        maze = Maze.gen_maze_adversarial(None, metric, p1, p2, method, True, max_iter, 1, False, True)

        #Modify that maze
        maze = Maze.gen_maze_adversarial(maze, metric, 1, 0.05, method, True, max_iter, dimension, False, True)

        #Solve that maze
        print(f"metric = {metric} | method = {method} | path len, nodes explored, dead ends = {Maze.solve_maze(maze, method, True, 1, 11, method)}")
        print("-------------------------")
print(f"{Maze.solve_maze(maze, method, True, 0, 11, method)}")