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


## Problem 3: Choosing a team!  
**The goal State:** A team of robots with maximum possible skills formed using the given budget.  
**Set of valid states:** A team consisting of whole robots, having maximum skill and cost less than budget.  
**The Successor function:** Successor function will return all the possible teams of a current node (i.e. a robot or a team)  
**The cost function:** Cost of a given robot. Adding a robot in the team will deduct the cost of that robot from the budget.  

•	The initial code given used greedy approach to solve the puzzle where the problem was that it included a fraction of a particular robot to completely use the budget. However, the problem demanded a whole robot. First, we thought of using a the best first greedy search using skill/cost ratio to solve the problem. However, we soon realized that it won’t give us the optimal solution as it will work in  the same manner as the given code. Since this was an optimization problem similar to 0/1 knapsack, so we considered using Dynamic Programming, but we came know that DP doesn’t work for floating point values, therefore we dropped the idea of using that as well. Finally decided to work the problem using a normal blind search (DFS) and then work our way to optimize the problem, which later gave us best results.  
•	The design implementation involves creation of a fringe data structure which contains all the valid nodes (i.e. teams), and a successor function called ‘SUCC’ which generates valid child nodes or team of each node in the fringe. We have maintained a list of visited nodes to not include any permutation or combination of a particular node/team in the fringe which reduces the search space. A team/node is sorted before pushing into the visited node and when a particular node  is checked for being visted, that node/team is aslo first sorted and then compared. We have also applied constraint to check that the cost of the team is not greater than the given budget. Apart from that we’ve also maintained maximum cost (cost_o) and skill (skill_o). We calculate the total cost and skill of each node and if it’s greater than maximum we update cost_o and skill_o else the particular node is ignored. Thus, this way finally in the end we get a team with maximum skill within a given budget.  
