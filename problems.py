'''
This file will contain your the code for your problems. 
'''
import numpy as np
import cv2
import algorithms as alg

class Maze:
   def __init__(self, height, width):
      if height < 1:
         raise ValueError("height can't be less than 1")
      if width < 2:
         raise ValueError("width can't be less than 2")
      
      self.height = 2*height+1
      self.width = 2*width+1
      
      self.start = (0,1)
      self.goal = (self.height-1, self.width-2)
   

   def gen_maze(self, p = 0.5, solvable = True):
      '''
      Generates a maze by randomly inserting paths (white spaces) in place of a wall.
      Initially, since each white space (cell) is in a grid it's surronded by 4 walls.
      Now we randomly remove a wall for each cell in the grid.
      Beacuse it's random this maze may not be solveable, so we test its solvability using
      a complete search algorithm like A-star or breadth first search and recreate the maze if it fails
      to find a path.

      - p (float): probability of removing wall for each white cell in grid
      - grid(bool): True = whether this is grid-like maze. False = randomly remove walls from anywhere
      '''   
      #Generate Maze!
      #------------------
      path_length = 0
      while path_length == 0:
         #Maze structure
         maze = np.zeros((self.height, self.width),bool)
         #Entry and exit points
         maze[0, 1] = True #entry
         maze[self.height-1, self.width - 2] = True #exit
         for i in range(self.height):
            for j in range(self.width):
               if (0 < i < self.height - 1 and 0 < j < self.width - 1):
                  current_cell = (i,j) #start at entry
                  #Create grid of white square cells (contained by 4 black walls)
                  if i%2 == 1 and j%2 == 1:
                     maze[current_cell] = True

                  #Randomly remove a wall for each white cell
                  current_cell = (i,j) #start at entry
                  remove = np.random.binomial(1, p, 1)
                  if (i%2 == 1 or j%2 == 1) and remove == 1:
                     maze[current_cell] = True

         #Verify that maze is solvable
         if solvable == True:
            astar = alg.astar(self.start, self.goal, maze)
            data = astar.data()
            path_length = data[0]
         else:
            break

      return maze
   

   def gen_maze_adversarial_path(self, p1 = 0.8, p2 = 0.1, method = 'dfs', max_iter1 = 100, max_iter2 = 1000):
      '''
      Same as gen_maze, except the aim is to create a maze that maximizes the length of the 
      path from the start node to the goal node.
      This version uses hill-climb.
      '''
      #Generate Maze!
      #------------------
      #Intiate params for adversial path search
      path_length = 0
      max_length = 0 #longest path

      iter = 0 #iterations
      print("Init maze")
      while path_length == 0 or iter < max_iter1:
         #Maze structure
         original_maze = self.gen_maze(p1) #initial, solvable maze
         maze = original_maze.copy()
         
         #Verify that maze is solvable and find path_length
         data = self.solve_maze(maze, method = method)
         path_length = data[0]

         #Record hardest maze found
         if max_length < path_length:
            max_length = path_length
            print(max_length)
            hardest_maze = original_maze.copy()

         iter += 1

      iter = 0
      print("Mod maze")
      while iter < max_iter2:
         maze = hardest_maze.copy()
         for i in range(self.height):
            for j in range(self.width):
               if (i%2 == 0 or j%2 == 0) and maze[i,j] != False:
                  #Randomly pick 1 or 0. 1 = Create wall. 0 = nothing.
                  current_cell = (i,j) #start at entry
                  wall = np.random.binomial(1, p2, 1)
                  if (0 < i < self.height - 1 and 0 < j < self.width - 1): #center
                     if wall == 1: 
                        maze[current_cell] = False #Add Wall
                     if wall == 0:
                        maze[current_cell] = True #Remove Wall
                  else:
                     pass
               
         #Verify that maze is solvable and find path_length
         data = self.solve_maze(maze, method = method, display = True, wait = 16)
         path_length = data[0]

         #Record hardest maze found
         if max_length < path_length:
            max_length = path_length
            print(max_length)
            hardest_maze = maze.copy()
         
         iter += 1

      return hardest_maze
   

   def gen_maze_adversarial_path2(self, p1 = 0.8, p2 = 0.1, method = 'dfs', max_iter = 20, max_gen = 10):
      '''
      Same as gen_maze, except the aim is to create a maze that maximizes the length of the 
      path from the start node to the goal node.
      This version uses evolution.
      '''
      #Generate Maze!
      #------------------
      #Intiate params for adversial path search
      path_length = 0
      max_length = 0 #longest path

      print("Initial maze")
      while path_length == 0:
         #Maze structure
         original_maze = self.gen_maze(p1) #initial, solvable maze
         maze = original_maze.copy()
         
         #Verify that maze is solvable and find path_length
         data = self.solve_maze(maze, method = method)
         path_length = data[0]

         #Record hardest maze found
         if max_length < path_length:
            max_length = path_length
            hardest_maze = original_maze.copy()
      
      print("Mod maze")
      print("Path: Gen: Iter:")
      gen = 0
      while gen < max_gen: #Number of generations
         iter = 0
         initial_maze = hardest_maze.copy()
         while iter < max_iter: #Number of iterations in this generation
            path_length = 0
            maze = initial_maze.copy()
            for i in range(self.height):
               for j in range(self.width):
                  if (0 < i < self.height - 1 and 0 < j < self.width - 1):
                     #Randomly pick 1 or 0. 1 = Create wall. 0 = nothing.
                     current_cell = (i,j) #start at entry
                     wall = np.random.binomial(1, p2, 1)
                     if (i%2 == 0 or j%2 == 0) and maze[i,j] != False:#center
                        if wall == 1: 
                           maze[current_cell] = False #Add Wall
                           
                           #Verify that maze is solvable and find path_length
                           data = self.solve_maze(maze, method = method)
                           path_length = data[0]
                           if path_length == 0:
                              maze[current_cell] = True #Remove Wall

                           #Record hardest maze found
                           if max_length < path_length:
                              max_length = path_length
                              hardest_maze = maze.copy()

                        if wall == 0:
                           maze[current_cell] = True #Remove Wall
                     else:
                        pass
            self.solve_maze(maze, method = method, display = True, wait = 1)
            print(max_length, gen, iter, end='\r')

            iter += 1
         gen += 1
      print("\n")

      return hardest_maze


   def display(self, maze, ms=1000):
      '''
      Displays the generated maze.
      - maze (np 2D array): this is the generated maze
      - ms (int): how long to display in cv2
      '''
      #Prepare display
      maze_display = np.stack([maze * 255] * 3, axis=-1).astype(np.uint8)
      cv2.namedWindow('Puzzle', cv2.WINDOW_NORMAL) #https://www.geeksforgeeks.org/python-opencv-namedwindow-function/
      cv2.resizeWindow('Puzzle', self.height*10, self.width*10) #https://www.geeksforgeeks.org/python-opencv-resizewindow-function/

      #Show start node
      maze_display[self.start] = [0, 0, 255] #red

      #Show goal node
      maze_display[self.goal] = [0, 0, 255] #red

      #Display
      cv2.imshow('Puzzle', maze_display)
      cv2.waitKey(ms)
   

   def solve_maze(self, maze, method = 'dfs', display = False, wait = 0):
      '''
      Solves the maze via specified search method.
      - maze (np 2D array): this is the generated maze
      - method (string): method of search. Options = 'dfs', 'bfs'
      - display (bool): True = display the solved maze. False = Don't.
      - wait (int): how long to display solved maze in in cv2 (only if display == True)
      '''
      #Display animation?
      if display == True:
         #Prepare display
         name = method
         maze_display = np.stack([maze * 255] * 3, axis=-1).astype(np.uint8)
         cv2.namedWindow(name, cv2.WINDOW_NORMAL)
         cv2.resizeWindow(name, self.width*10, self.height*10)

         #Show start node
         maze_display[self.start] = [0, 0, 255] #red

         #Show goal node
         maze_display[self.goal] = [0, 0, 255] #red

         #Display
         cv2.imshow(name, maze_display)
      else:
         maze_display = None
         name = None

      #Solving method:
      if method == 'dfs':
         dfs = alg.dfs(self.start, self.goal, maze, display, maze_display, name, wait)
         data = dfs.data()

      if method == 'bfs':
         bfs = alg.bfs(self.start, self.goal, maze, display, maze_display, name, wait)
         data = bfs.data()

      if method == 'ucs':
         ucs = alg.ucs(self.start, self.goal, maze, display, maze_display, name, wait)
         data = ucs.data()

      if method == 'greedy':
         greedy = alg.greedy(self.start, self.goal, maze, display, maze_display, name, wait)
         data = greedy.data()

      if method == 'astar':
         astar = alg.astar(self.start, self.goal, maze, display, maze_display, name, wait)
         data = astar.data()
      
      return data