# 8-Puzzle Solver

This project is a Python-based solver for the classic 8-puzzle problem. The solver uses the Best-First Search algorithm with an evaluation function f, where:

For the **greedy approach**, \( f = h \), where \( h \) is the sum of the Manhattan distances from each tile in the current state to its corresponding tile in the goal state.

For the **A\* approach**, \( f = h + g \), where \( g \) represents the cost to reach the current node from the start state.

## Overview
The 8-Puzzle is a sliding puzzle consisting of a 3x3 grid of numbered tiles with one blank space(here we consider 0 instead of blanck space). The goal is to rearrange the tiles to match a specified target configuration by sliding tiles into the blank space. This solver takes an initial state, verifies if it's solvable, and uses BFS to find the solution steps.

## Data Structs Used 

### States
The states are represented as tuples with two elements: tuple1 and tuple2.
 - `tuple1` is a tuple containing 9 ordered pairs, each representing the position of each number (from 0 to 8) on the board.
 - `tuple2` is a tuple of 9 integers that represent the tile numbers in a one-dimensional manner

### Problem
The problem has the initial_state and goal_state as attributes and some methods useful to do transitions between states.

## Solvability
Not every combination of `(initial_state, goal_state)` is solvable—only half of the possible states are reachable from any given state. This is due to the parity of the permutations within the puzzle. 

In other words, the arrangement of the tiles affects whether a solution path exists. The solver includes a function to check solvability based on this parity, ensuring that only solvable configurations are attempted.

For more information, see:
- [Why is this 15-Puzzle Impossible? - Numberphile](https://www.youtube.com/watch?v=YI1WqYKHi78&t=1021s)
- [GeeksforGeeks: Check if an instance of the 8-puzzle is solvable](https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/)
