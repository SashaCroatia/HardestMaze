import problems as prb

'''
This file will contain the code needed to run a demonstration of your project. 

For the progress report, it should contain code that shows a breif demonstration of random agents attempting to solve each problem. 

For the final report, it should contain code that shows a breif demonstration of each algorithm attempting to solve each problem. 

In both cases, to make sure we can grade these all in time, please ensure that each demonstration is just long enough to show some
meaningful behavior. If your problem is chess playing, for example, you might show 5 moves from each player, where one player uses one 
algorithm and one player uses another. If your problem is snake, you might show game long enough for the player to eat two apples or die
(whichever comes first).
'''
#Define dimensions of maze
Maze = prb.Maze(14,14)

#Generate maze
maze = Maze.gen_maze2(0.5)
Maze.display(maze)

#Solve that maze
print(Maze.solve_maze(maze, 'dfs', True))
