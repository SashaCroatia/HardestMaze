'''
This file will contain implementations of each algorithm/agent type.
'''
import cv2

class dfs:
  '''
  Implements depth-first search
  '''
  def __init__(self, start, goal, maze, display = False, maze_display = None, name = None, wait = 0):
    #Initials
    frontier = [start] #LIFO stack with start as the only element
    explored = set() #empty set of nodes visited
    path = {} #empty dictionary
    path_len = 0 #length of path
    dead_ends = 0 #deadends

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
      valid_neighbors = 0
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
          valid_neighbors += 1

      #If no valid neighbors found, it's a deadend
      if valid_neighbors == 0:
        dead_ends += 1
    
    if display == True:
      cv2.imshow(name, maze_display)
      cv2.waitKey(wait)

    #return
    self.path_len = path_len
    self.exp_len = len(explored)
    self.dead_ends = dead_ends

  def data(self):
    return (self.path_len, self.exp_len, self.dead_ends)


class bfs:
  '''
  Implements breadth-first search
  '''
  def __init__(self, start, goal, maze, display = False, maze_display = None, name = None, wait = 0):
    #Initials
    frontier = [start] #FIFO queue with start as the only element
    explored = set() #empty set of nodes visited
    path = {} #empty dictionary
    path_len = 0 #length of path
    dead_ends = 0 #deadends

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
      valid_neighbors = 0
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
          valid_neighbors += 1

      #If no valid neighbors found, it's a deadend
      if valid_neighbors == 0:
        dead_ends += 1
    
    if display == True:
      cv2.imshow(name, maze_display)
      cv2.waitKey(wait)

    #return
    self.path_len = path_len
    self.exp_len = len(explored)
    self.dead_ends = dead_ends

  def data(self):
    return (self.path_len, self.exp_len, self.dead_ends)
  

class ucs:
  '''
  Implements uniform cost search
  '''
  def __init__(self, start, goal, maze, display = False, maze_display = None, name = None, wait = 0):
    #Initials
    frontier = [(0, start)] #priority queue. has (path-)cost and node
    node_cost = {start: 0} #like explored set, but each explored node has a cost attached.
    path = {} #empty dictionary
    path_len = 0 #length of path
    dead_ends = 0 #deadends

    while True:
      if len(frontier) == 0:
        #print("Error: no solution found")
        break
      frontier.sort(key=lambda x: x[0], reverse=True) #sort frontier in descending order (lowest cost last) 
      current_cost, current = frontier.pop() #choose shallowest node in frontier

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
      valid_neighbors = 0
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

        new_current_cost = current_cost + 1 #all costs from current are equal

        #Verify neighbor is in white path and not in node_cost dictionary of path:cost
        if maze[neighbor] == True and neighbor not in node_cost:
          node_cost[neighbor] = new_current_cost #attach cost to this neighboring node
          frontier.append((new_current_cost, neighbor))
          path[neighbor] = current
          valid_neighbors += 1

      #If no valid neighbors found, it's a deadend
      if valid_neighbors == 0:
        dead_ends += 1
    
    if display == True:
      cv2.imshow(name, maze_display)
      cv2.waitKey(wait)

    #return
    self.path_len = path_len
    self.exp_len = len(node_cost)
    self.dead_ends = dead_ends

  def data(self):
    return (self.path_len, self.exp_len, self.dead_ends)
  

class greedy:
  '''
  Implements greedy best-first search
  '''
  def __init__(self, start, goal, maze, display = False, maze_display = None, name = None, wait = 0):
    #Manhatten distace heuristic from goal to start node:
    dist = lambda node: abs(goal[0] - node[0]) + abs(goal[1] - node[1])
    frontier = [(dist(start), start)] #priority queue. has (path-)cost and node
    node_cost = {start: dist(start)} #like explored set, but each explored node has a cost attached.
    path = {} #empty dictionary
    path_len = 0 #length of path
    dead_ends = 0 #deadends

    while True:
      if len(frontier) == 0:
        #print("Error: no solution found")
        break
      frontier.sort(key=lambda x: x[0], reverse=True) #sort frontier in descending order (lowest cost last) 
      total_cost, current = frontier.pop() #choose shallowest node in frontier

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
      valid_neighbors = 0
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

        new_cost = dist(neighbor)

        #Verify neighbor is in white path and not in node_cost dictionary of path:cost
        if maze[neighbor] == True and neighbor not in node_cost:
          node_cost[neighbor] = new_cost #attach cost to this neighboring node
          frontier.append((new_cost, neighbor))
          path[neighbor] = current
          valid_neighbors += 1

      #If no valid neighbors found, it's a deadend
      if valid_neighbors == 0:
        dead_ends += 1
    
    if display == True:
      cv2.imshow(name, maze_display)
      cv2.waitKey(wait)

    #return
    self.path_len = path_len
    self.exp_len = len(node_cost)
    self.dead_ends = dead_ends

  def data(self):
    return (self.path_len, self.exp_len, self.dead_ends)
  

class astar:
  '''
  Implements astar search
  '''
  def __init__(self, start, goal, maze, display = False, maze_display = None, name = None, wait = 0):
    #Manhatten distace heuristic from goal to start node:
    dist = lambda node: abs(goal[0] - node[0]) + abs(goal[1] - node[1]) #h(node)
    start_cost = 0 #g(node)
    start_total_cost = dist(start) + start_cost #f(node) = h(node) + g(node)
    frontier = [(start_total_cost, start_cost, start)] #priority queue. has (path-)cost and node
    node_cost = {start: start_total_cost} #like explored set, but each explored node has a cost attached.
    path = {} #empty dictionary
    path_len = 0 #length of path
    dead_ends = 0 #deadends

    while True:
      if len(frontier) == 0:
        #print("Error: no solution found")
        break
      frontier.sort(key=lambda x: x[0], reverse=True) #sort frontier in descending order (lowest cost last) 
      total_cost, current_cost, current = frontier.pop() #choose shallowest node in frontier

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
      valid_neighbors = 0
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

        new_current_cost = current_cost + 1
        new_total_cost = dist(neighbor) + new_current_cost

        #Verify neighbor is in white path and not in node_cost dictionary of path:cost
        if maze[neighbor] == True and neighbor not in node_cost:
          node_cost[neighbor] = new_total_cost #attach cost to this neighboring node
          frontier.append((new_total_cost, new_current_cost, neighbor))
          path[neighbor] = current
          valid_neighbors += 1

      #If no valid neighbors found, it's a deadend
      if valid_neighbors == 0:
        dead_ends += 1
    
    if display == True:
      cv2.imshow(name, maze_display)
      cv2.waitKey(wait)

    #return
    self.path_len = path_len
    self.exp_len = len(node_cost)
    self.dead_ends = dead_ends

  def data(self):
    return (self.path_len, self.exp_len, self.dead_ends)