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

There are three variants of this problem which are discussed below:  
**•	Original:** This variant is the normal 15-puzzle where the final goal is to arrange the number from 1-15 on the board by swapping one tile at a time. Since it is given to use the we have to use A* algorithm to solve the puzzle, we considered two types of heuristic for this problem: misplace tiles and Manhattan distance. We finally decided upon the Manhattan distance as it turned out to be a better heuristic than the misplaced tiles. We have a successor function which generates valid child nodes/board of all the other nodes in the fringe and next state/board is selected based on the heuristic applied. Also, visited list also maintained, so prevent unnecessary traversal.
**•	Circular:** This another variant of 15-puzzle wherein the swap can be possible from one side of the board to the opposite side of the board. Again, we had to make decision for which heuristic to be used: misplaced tiles or Manhattan. We finally decided upon misplaced tiles for this one. Design implementation is same as the above problem. The only major difference is the heuristic. The successors are selected based on the heuristic.
**•	Luddy:** This is the third and the final variant of the 15-puzzle problem where the swapping of the tiles is like the move of a knight in the chess game. This was the most difficult one to solve for us as we couldn’t decide on a good heuristic for this one. The design implementation is similar to the above two problems. However, heuristic was the major challenge. Manhattan distance was not an admissible heuristic, so it was out of option, therefore tried to solve the problem with the misplaced titles. While it is an admissible heuristic it takes time to solve the puzzle. Since weren’t able to come up with a good solution we finally decided to implement with the misplaced tiles.


## Problem 3: 
**The initial State:** A map with no friends hiding.
**The goal State:** K friends hiding from each other such that no one can see the other.
**Set of valid states:** All the valid positions where a friend can be placed so that he is not visible to other friends.
**The Successor function:** returns valid successors/child of each node (board/map).
**The cost function:** Cost function of placing one friend on the map is 1.

- The code algorithm uses Depth first search to search a position for a friend to hide. However, the given code is faulty where it places a friend at an available position by popping a successor from the stack. Also, to understand how the successors were generated I evaluated the code by printing the successors and found that the same successors where generated and thus can be repeatedly be visited. So, just like problem1 we maintain a list of all visited nodes to reduce our traversal to unnecessary nodes.

- The main part for this problem was to find valid states or valid positions for a friend to hide. Friends cannot be placed in the same row or column unless a building is present in between. In order to check this constraint, I wrote a function called _getInvalidStates_ which will return a list of all the coordinates that are invalid. So, when a successor is generated, and a new friend is to be added we check the condition whether that coordinate is present in invalid list or not. If it isn’t then the friend is placed, and the successor is generated. Thus, in the end all the k friends are placed on the map such that they are hidden from each other.
