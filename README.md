# Assignment 1

## Problem 1: The Luddy Puzzle
**The initial State:** A 4x4 board with all the jumbled number (1-15) with an empty space (0)
**The goal State:** Board with all the numbers arranged from 1 – 15
**Set of valid states:** All the permutation and combinations of numbers from 1 – 15 on the tiles of the board with one tile empty (i.e. 0)
**The Successor function:** The successor function will return all the possible moves that can be taken from the current moves i.e. all the possible swaps of numbered tile from a current board state
**The cost function:** Cost of swapping one tile is 1.

**Heuristic used:** Different heuristics have been used for different types of board. They are as follows:
1.	Original: Manhattan Distance
2.	Circular: No. of Misplaced Tiles
3.	Luddy: No. of Misplaced Tiles

- After implementing BFS, I evaluated my code to check for the optimal solution by printing the fringe at every iteration. I found that the search algorithm repeatedly traverses nodes that were already visited. Thus, I maintained a list of visited node and set up a condition in the moves function, (which generates successors of a given node) that if a successor is visited, then don’t include them in the ‘moves’.

- The above implementation took care of the unnecessary node traversal. However, in order to get the string of compass directions, we require the nodes of the shortest path, as the algorithm can follow up other possible paths as well, and thus the visited nodes list includes other nodes as well. I found this part the most difficult. I tried various methods like maintaining a dictionary for the paths (node as the key and path up to that node as value), which did worked for the given map, but when I altered the map for various conditions, It would work sometimes and sometimes not. So, I defined a list called _path_tracer_ which contained lists of paths and made it work like a queue. In the _path_tracer_ the path upto a particular node appears in the same order as the node appear in the fringe. So, when the shortest path is traced, we eventually get the nodes of the path from the _path_tracer_.

- Once I got the nodes for the shortest path, I defined a function called _getDirection_ to get the string of compass directions. I ran a ‘for loop’ over the nodes of the path and subtracted the values of ith row from (i+1)th row and doing the same for the columns as well. Based on the values I got, I defined the direction and appended it to a string variable.

## Problem 3: 
**The initial State:** A map with no friends hiding.
**The goal State:** K friends hiding from each other such that no one can see the other.
**Set of valid states:** All the valid positions where a friend can be placed so that he is not visible to other friends.
**The Successor function:** returns valid successors/child of each node (board/map).
**The cost function:** Cost function of placing one friend on the map is 1.

- The code algorithm uses Depth first search to search a position for a friend to hide. However, the given code is faulty where it places a friend at an available position by popping a successor from the stack. Also, to understand how the successors were generated I evaluated the code by printing the successors and found that the same successors where generated and thus can be repeatedly be visited. So, just like problem1 we maintain a list of all visited nodes to reduce our traversal to unnecessary nodes.

- The main part for this problem was to find valid states or valid positions for a friend to hide. Friends cannot be placed in the same row or column unless a building is present in between. In order to check this constraint, I wrote a function called _getInvalidStates_ which will return a list of all the coordinates that are invalid. So, when a successor is generated, and a new friend is to be added we check the condition whether that coordinate is present in invalid list or not. If it isn’t then the friend is placed, and the successor is generated. Thus, in the end all the k friends are placed on the map such that they are hidden from each other.
