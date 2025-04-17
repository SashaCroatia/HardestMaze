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

#Define dimensions of empty grid
Maze = prb.Maze(10,10)

#Generate maze
p1 = 0.6 #probability of removing neighboring wall in maze gen
p2 = 0.01 #probability of adding neighboring wall in modifying maze created above
maze = Maze.gen_maze_adversarial_path(p1, p2, 'astar', 100, 2000)
#maze = Maze.gen_maze(0.64)
#Maze.display(maze)

#Solve that maze
print("path len, num nodes explored = ", Maze.solve_maze(maze, 'astar', True, 0))