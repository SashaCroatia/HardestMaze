'''
This file will contain your the code for your problems. 
'''
import numpy as np
import cv2
import random
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


   def gen_maze(self):
      '''
      Generates a complete, solvable, no-loop maze via the recursive backtracking algorithm.

      Inspiration for possible_moves and backtrack functions (modified to meet my project specifications):
      https://learn.64bitdragon.com/articles/computer-science/procedural-generation/maze-generation-with-the-recursive-backtracking-algorithm 
      '''
      #Setup for randomized depth-first search (recursive backtracking)
      #--------------------     
      def possible_moves(visited, cell):
         moves = []
         for direction in ['north', 'south', 'east', 'west']:
            if direction == 'north':
               new_cell = cell[0], cell[1]+1
            elif direction == 'south':
               new_cell = cell[0], cell[1]-1
            elif direction == 'east':
               new_cell = cell[0]+1, cell[1]
            else:
               new_cell = cell[0]-1, cell[1]
            # check the new cell is in the visited bounds
            if (0 <= new_cell[0] < (self.height-1)//2 and 0 <= new_cell[1] < (self.width-1)//2 and visited[new_cell] == False):
               moves.append(new_cell)
         return moves
      
      def backtrack(visited, path):
         path.pop()
         while len(path) > 0:
            last = path[-1]
            moves = possible_moves(visited, last)
            if len(moves) > 0:
               new_cell = random.choice(moves)
               return last, new_cell
            else:
               path.pop()
         return None
      

      #Setup for Maze drawing
      #----------------------
      #Maze structure
      maze = np.zeros((self.height, self.width),bool)
      start_cell = (1,1) #coordinate on maze

      for i in range(self.height):
         for j in range(self.width):
            if (0 < i < self.height - 1 and 0 < j < self.width - 1):
               if i%2 == 1 and j%2 == 1:
                  current_cell = (i,j) #start at entry
                  maze[current_cell] = True

      #Entry and exit points
      maze[0, 1] = True #entry
      maze[self.height-1, self.width - 2] = True #exit

      def draw_path(current_cell, new_cell):
         #translate visted coordinates to maze coordinates
         current_row = 2*current_cell[0]+1
         current_col = 2*current_cell[1]+1
         new_row = 2*new_cell[0]+1
         new_col = 2*new_cell[1]+1

         if new_col > current_col:
            maze[current_row, (new_col-1)] = True
         elif new_col < current_col:
            maze[current_row, (new_col+1)] = True
         elif new_row > current_row:
            maze[(new_row-1), current_col] = True
         else:
            maze[(new_row+1), current_col] = True
         
         return maze

      #Generate Maze!
      #------------------
      #All grid points unvisited
      visited = np.zeros(((self.height-1)//2, (self.width-1)//2),bool)
      num_unvist = (self.height-1)*(self.width-1)/4
      
      #Starting point
      current_cell = start_cell[0]-1, start_cell[1]-1 #coordinate on visited
      visited[current_cell] = True
      num_unvist -= 1
      path = [current_cell]

      #New points
      while num_unvist > 0:
         #Evaulate possible next moves at current cell
         moves = possible_moves(visited, current_cell)

         if len(moves) > 0:
            #If there's a move, choose one
            new_cell = random.choice(moves)
         else:
            #otherwise backtrack and try again
            current_cell, new_cell = backtrack(visited, path)
         
         path.append(new_cell)

         #Draw path
         maze = draw_path(current_cell, new_cell)

         #Updated visited coordinate
         visited[new_cell] = True
         num_unvist -= 1

         #Update current cell
         current_cell = new_cell

      return maze
   

   def gen_maze2(self, p=0.5):
      '''
      Generates a maze by randomly inserting paths (white spaces) in place of a wall.
      Initially, since each white space (cell) is in a grid it's surronded by 4 walls.
      Now we randomly remove a wall for each cell in the grid.
      Beacuse it's random this maze may not be solveable, so we test its solvability using
      a complete search algorithm like A-star or breadth first search and recreate the maze if it fails
      to find a path.
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
         dfs = alg.dfs(self.start, self.goal, maze, False, None)
         data = dfs.data()
         path_length = data[0]

      return maze
   

   def display(self, maze, ms=1000):
      #Prepare display
      maze_display = np.stack([maze * 255] * 3, axis=-1).astype(np.uint8)
      cv2.namedWindow('Puzzle', cv2.WINDOW_NORMAL) #https://www.geeksforgeeks.org/python-opencv-namedwindow-function/
      cv2.resizeWindow('Puzzle', self.width*10, self.height*10) #https://www.geeksforgeeks.org/python-opencv-resizewindow-function/

      #Show start node
      maze_display[self.start] = [0, 0, 255] #red

      #Show goal node
      maze_display[self.goal] = [0, 0, 255] #red

      #Display
      cv2.imshow('Puzzle', maze_display)
      cv2.waitKey(ms)
   

   def solve_maze(self, maze, method = 'dfs', display = False):
      #Display animation??
      if display == True:
         #Prepare display
         maze_display = np.stack([maze * 255] * 3, axis=-1).astype(np.uint8)
         cv2.namedWindow('Maze', cv2.WINDOW_NORMAL)
         cv2.resizeWindow('Maze', self.width*10, self.height*10)

         #Show start node
         maze_display[self.start] = [0, 0, 255] #red

         #Show goal node
         maze_display[self.goal] = [0, 0, 255] #red

         #Display
         cv2.imshow('Maze', maze_display)
         cv2.waitKey(500)
      else:
         maze_display = None

      #Solving method:
      if method == 'dfs':
         dfs = alg.dfs(self.start, self.goal, maze, display, maze_display)
         data = dfs.data()
      
      return data