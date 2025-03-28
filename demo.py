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
Maze = prb.Maze(16,16)

#Generate maze
prob = 0.51 #probability of generating neighboring wall in grid-cell
maze = Maze.gen_maze(prob)
Maze.display(maze)

#Solve that maze with depth-first search and breadth-first search
print("BFS, (path len, num nodes explored) = ", Maze.solve_maze(maze, 'bfs', True, 1)) # WARNING:This is slow! Make sure prob not too high
print("DFS, (path len, num nodes explored) = ", Maze.solve_maze(maze, 'dfs', True, 0))

