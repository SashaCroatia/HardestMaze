'''
This file will contain implementations of each algorithm/agent type.
'''
import cv2

class dfs:
  '''
  Implements depth-first search
  '''
  def __init__(self, start, goal, maze, display = False, maze_display = None, name = None):
    #Initials
    frontier = [start] #LIFO stack with start as the only element
    explored = set() #empty set of nodes visited
    path = {} #empty dictionary
    path_len = 0 #length of path

    while True:
      if len(frontier) == 0:
        #print("Error: no solution found")
        break
      current = frontier.pop() #choose shallowest node in frontier
      explored.add(current) #add unique node to explored

      if display == True:
        # Mark current cell as grey (path trace)
        maze_display[current] = [210, 210, 210]
        cv2.imshow(name, maze_display)

      #If goal state found, describe solution
      if current == goal:
        if display == True:
          maze_display[current] = [0, 0, 255]
        while current != start:
            current = path[current]
            path_len += 1
            if display == True:
              # Backtrack the path in red
              maze_display[current] = [0, 0, 255]
              cv2.imshow(name, maze_display)
        break

      #Search for next legal move
      for direction in ['north', 'south', 'east', 'west']:
        neighbor = current

        #Find neighboring cells
        if direction == 'north':
          neighbor = current[0], current[1]+1
        elif direction == 'south':
          neighbor = current[0], current[1]-1
        elif direction == 'east':
          neighbor = current[0]+1, current[1]
        else:
          neighbor = current[0]-1, current[1]

        #Verify neighbor is in white path and not in explored:
        if maze[neighbor] == True and neighbor not in explored:
          frontier.append(neighbor)
          path[neighbor] = current
    
    if display == True:
      cv2.imshow(name, maze_display)
      cv2.waitKey(0)

    #return
    self.path_len = path_len
    self.exp_len = len(explored)

  def data(self):
    return (self.path_len, self.exp_len)


class bfs:
  '''
  Implements breadth-first search
  '''
  def __init__(self, start, goal, maze, display = False, maze_display = None, name = None):
    #Initials
    frontier = [start] #FIFO queue with start as the only element
    explored = set() #empty set of nodes visited
    path = {} #empty dictionary
    path_len = 0 #length of path

    while True:
      if len(frontier) == 0:
        #print("Error: no solution found")
        break
      current = frontier.pop(0) #choose shallowest node in frontier
      explored.add(current) #add unique node to explored

      if display == True:
        # Mark current cell as grey (path trace)
        maze_display[current] = [210, 210, 210]
        cv2.imshow(name, maze_display)

      #If goal state found, describe solution
      if current == goal:
        if display == True:
          maze_display[current] = [0, 0, 255]
        while current != start:
            current = path[current]
            path_len += 1
            if display == True:
              # Backtrack the path in red
              maze_display[current] = [0, 0, 255]
              cv2.imshow(name, maze_display)
        break

      #Search for next legal move
      for direction in ['north', 'south', 'east', 'west']:
        neighbor = current

        #Find neighboring cells
        if direction == 'north':
          neighbor = current[0], current[1]+1
        elif direction == 'south':
          neighbor = current[0], current[1]-1
        elif direction == 'east':
          neighbor = current[0]+1, current[1]
        else:
          neighbor = current[0]-1, current[1]

        #Verify neighbor is in white path and not in explored:
        if maze[neighbor] == True and neighbor not in explored:
          frontier.append(neighbor)
          path[neighbor] = current
    
    if display == True:
      cv2.imshow(name, maze_display)
      cv2.waitKey(0)

    #return
    self.path_len = path_len
    self.exp_len = len(explored)

  def data(self):
    return (self.path_len, self.exp_len)