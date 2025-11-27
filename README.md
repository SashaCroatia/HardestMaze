## Project: AI Algorithm Comparison

---
Note: This originally started as a course project for INFO 550 - Artificial Intelligence.

This program generates adversarial mazes (longest path, greatest number of dead-ends, and largest search space) for various maze-solving algorithms (depth-first, uniform cost, greedy best, A* search). Check [this](https://www.youtube.com/watch?v=IofOjhYj6EQ) YouTube link to see it in action.

## Repository Structure
The repository includes the following files:

### 1. `algorithms.py`  
This file contains the implementations of the following AI search algorithms: depth-first search, breadth-first search (not used in project), uniform-cost search, greedy best search, and A* search.

### 2. `comparisons.py`  
This file contains code performing comparisons between selected algorithms.  

### 3. `demo.py`  
This file demonstrates my project in action.

### 4. `problems.py`  
This file contains the implementation of generating and displaying a maze, along with a method that calls on an search algorithm to solve that maze.  

---

## Instructions for Users

### Step 1: Prepare Python Evironment
- Download and install [Anaconda](https://www.anaconda.com/download)
- Open Terminal (or Anaconda prompt in Windows)- 
- `conda create --name evalenv python=3.9`- 
- `conda activate evalenv`
- `python -m pip install --upgrade pip`
- Open project directory (`cd <your_directory>` in Windows)
- `pip install -r requirements.txt`

### Step 2: Run
- Open Terminal (or Anaconda prompt in Windows)- 
- `conda activate evalenv`
-  Open project directory (`cd <your_directory>` in Windows)
- `python demo.py`
