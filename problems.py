'''
This file will contain your the code for your problems. 
'''
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

class Game:
    def __init__(self, problem, pZero, pOne,verbose=True):
      self.problem = problem      
      self.players = [pZero,pOne]   
      self.verbose = verbose   
      if self.verbose:
         self.problem.showState()               
    def playGame(self):
      pCur=0
      while self.problem.isTerminal()==False:           
         move = self.players[pCur].getMove(self.problem)           
         self.problem.doMove(move)
         if self.verbose:
            self.problem.showState()
            print(f"Move {self.problem.ticks}:")
            print(self.problem.state)
         pCur = np.abs(pCur-1)
        
      wIndex = self.problem.getWinner()
      winner = self.players[wIndex]
      if wIndex == -1:
         winner = "DRAW"
      #display final state
      print(f"The Winner is {winner} ({wIndex})!")
      if self.verbose:
         self.problem.showState(4000)
      return wIndex
              
class TicTacToe:
   def __init__(self):
      self.state = np.zeros((3,3))      
      self.ticks=-1      
   def getLegalMoves(self, state=None):
      if state is None:
         state = self.state
      moves = []
      mark = 1
      if np.sum(np.abs(state))%2!=0:
         mark = -1       
      for i in range(state.shape[0]):
         for j in range(state.shape[1]):
            if state[i,j]==0:
               moves.append((mark,(i,j)))
      return moves             
   def getSuccessor(self, move, state):
      mark = move[0]
      loc = move[1]
      state[loc] = mark
      return state
   def doMove(self,move):
      self.state = self.getSuccessor(move,self.state)
      self.ticks+=1
   def isTerminal(self, state=None):
      if state is None:
         state = self.state         
      terminal = False
      val = self.evalTerminal(state)      
      if val ==0 and np.sum(np.abs(state))==9:
         terminal = True
      if val!=0:
         terminal = True
      return terminal
   def evalTerminal(self, state=None):
      if state is None:
         state = self.state
      val = 0      
      #pOne Wins
      pZeroWins = [np.max(np.sum(state,0))==3,np.max(np.sum(state,1))==3,np.trace(state)==3,np.trace(state[:,::-1])==3]
      pOneWins = [np.min(np.sum(state,0))==-3,np.min(np.sum(state,1))==-3,np.trace(state)==-3,np.trace(state[:,::-1])==-3]

      if np.any(pZeroWins):
         val = 1
      if np.any(pOneWins):
         val = -1
      return val
   def getWinner(self, state=None):
      if state is None:
         state = self.state
      val = self.evalTerminal(state)
      if val==1:
         return 0 
      elif val==-1:
         return 1
      else:
         return -1
   def showState(self, ms = 1000,state=None):
      if state is None:
         state = self.state  

      screen = np.zeros((150,150)).astype(np.uint8)         
      screen = cv2.line(screen,(0,49),(149,49),255) 
      screen = cv2.line(screen,(0,99),(149,99),255)
      screen = cv2.line(screen,(49,0),(49,149),255) 
      screen = cv2.line(screen,(99,0),(99,149),255)

      for i in range(state.shape[0]):
         for j in range(state.shape[1]):
            if state[i,j]==1:
               screen = cv2.line(screen,(5 +j*50,5+i*50),(44+j*50,44+i*50),255,2,cv2.LINE_AA) 
               screen = cv2.line(screen,(44+j*50,5+i*50),(5 +j*50,44+i*50),255,2,cv2.LINE_AA) 
            if state[i,j]==-1:
               screen = cv2.circle(screen, (25 +j*50,25+i*50), 20, 255, 2,cv2.LINE_AA) 
               
      cv2.imshow('TicTacToe',screen)
      cv2.waitKey(ms)

class Maze:
   def __init__(self, width, height):
      width = 2*width+1
      height = 2*height+1

      self.width = width
      self.height = height

   def gen_maze(self):

      #Setup for randomized depth-first search (recursive backtracking)
      #--------------------
      #Inspiration for these functions (modified to meet my project specifications):
      #https://learn.64bitdragon.com/articles/computer-science/procedural-generation/maze-generation-with-the-recursive-backtracking-algorithm
      def north(cell):
         return cell[0], cell[1] + 1

      def south(cell):
         return cell[0], cell[1] - 1

      def east(cell):
         return cell[0] + 1, cell[1]

      def west(cell):
         return cell[0] - 1, cell[1]
      
      def possible_moves(visited, cell):
         moves = []
         for direction in [north, south, east, west]:
            new_cell = direction(cell) #propose new cell to visit
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

         #Update currcent cell
         current_cell = new_cell
      

      #Display maze
      #---------------
      maze_display = (maze * 255).astype(np.uint8)
      cv2.namedWindow('Maze', cv2.WINDOW_NORMAL) #https://www.geeksforgeeks.org/python-opencv-namedwindow-function/
      cv2.resizeWindow('Maze', self.width*10, self.height*10) #https://www.geeksforgeeks.org/python-opencv-resizewindow-function/
      cv2.imshow('Maze', maze_display)
      cv2.waitKey(0)
      cv2.destroyAllWindows() #https://www.geeksforgeeks.org/python-opencv-destroyallwindows-function/

      return maze