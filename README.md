# Assignment 1

## Problem 1: The Luddy Puzzle  
**The initial State:** A 4x4 board with all the jumbled number (1-15) with an empty space (0)  
**The goal State:** Board with all the numbers arranged from 1 – 15  
**Set of valid states:** All the permutation and combinations of numbers from 1 – 15 on the tiles of the board with one tile empty (i.e. 0)  
**The Successor function:** The successor function will return all the possible moves that can be taken from the current state i.e. all the possible swaps of numbered tile with the empty tile(0). 
**The cost function:** Cost of swapping one tile is 1.  
**Heuristic used:** Different heuristics have been used for different types of board. They are as follows:
1.	Original: Manhattan Distance
2.	Circular: Modified Manhattan Distance for circular
3.	Luddy: No. of Misplaced Tiles

There are three variants of this problem which are discussed below:  
**•	Original:** This variant is the normal 15-puzzle where the final goal is to arrange the number from 1-15 on the board by swapping one tile at a time with the empty tile. Since it is given that we have to use A* algorithm to solve the puzzle, two types of heuristic functions were considered for this problem: misplaced tiles and Manhattan distance. We finally decided upon the Manhattan distance as it turned out to be a better heuristic than misplaced tiles. A successor function is used to generate successor states by swapping one numbered tile with the empty tile. Also, visited list is maintained that avoids adding the already visited states to the fringe. A parallel list of heuristic values is maintained with the Fringe and the State is popped from fringe based on the least heuristic value from the heuristic list.  
**•	Circular:** This is another variant of 15-puzzle wherein the swap can be possible from one side of the board to the opposite side of the board. Again, we had to make decision for which heuristic to be used: misplaced tiles or Manhattan. We finally decided upon Manahattan heuristic function that was modified a little for the Circular Moves. The Manhattan distance was modoified in such a way that the circular distance as well and the normal Manhattan distance is calculated, and the minimum distance of the two is considered. All the circular moves and its condition were added. Design implementation is same as the above problem. The only major difference is the heuristic. States with smaller heuristic values are considered first over other states, i.e., they are popped from the fringe first.  
**•	Luddy:** This is the third and the final variant of the 15-puzzle problem where the swapping of the tiles is like the move made by the knight in the chess game. This was the most difficult one to solve for us as we couldn’t decide upon a good heuristic for this one. The design implementation is similar to the above two problems. However, heuristic was the major challenge. Manhattan distance was not an admissible heuristic, so it was out of option, therefore tried to solve the problem with the misplaced titles. While it is an admissible heuristic it takes time to solve the puzzle. Since weren’t able to come up with a good solution we finally decided to implement with the misplaced tiles. A heuritic function was thought where the movement from one position to its actual value could be hardcoded into a python dictionary and this dictionary could have been used as a lookup up table while calculating the required number of moves.  

## Problem 2: Road trip!  
**The initial State:** Start city with a cost function that we ave to optimize while we reach till the end city  
**The goal State:** Reaching the end city with the optimum value of cost function.   
**Set of valid states:** Set all the possible cities that can be visited.  
**The Successor function:** Will return all the cities that can be visited from the current city. 
**The cost function:** Distance between two cities. (edge weight)

•	We first create a dictionary of the given file where key is the main city and the second key would be the list of connected cities from the main city. In this we create an inner dictionary in which we store highway name, miles, and max speed. We've also calculated an mpg (miles per gallon) value based on given formula.  
•	What we've implemented is basically a priority queue. Based on the requirement we created a fringe data structure containing all the basic parameters. While the successor function generates all the valid successors of a node the fringe data structure updates all the corresponding parametres like total miles, gas, mpg, hours, etc. till path followed so far.  
•	Once the successors are added to the fringe we use the cost function and pop out the minimum value of either number of segments until now or total number of hours. For mpg cost function we pop the minimum value of gas gallons used until now in the list.  
•	If the end city is found we print the path, miles, mpg as required in the ouput and also print human readable instructions. Also, We thought of adding a heuristic function based on the longitudes and latitudes of coordinates but it would have been useful only for the case of miles cost function and moreover, we weren't sure that whether the heuristic would be admissible and consistent or not so decided against implementing it. The output was generated really fast so we didn't feel the need to use the heuristic function. 

## Problem 3: Choosing a team  
**The Initial State:** A list of robots with their corresponding skill and cost with a given budget.  
**The Goal State:** A team of robots with maximum possible skills formed using the given budget.  
**Set of Valid States:** A team consisting of whole robots, having maximum skill and cost less than budget.  
**The Successor Function:** Successor function will return a successor with a valid robot added to the current team.  
**The Cost Function:** Cost of a given robot. Adding a robot in the team will deduct the cost of that robot from the budget.  

•	The given code uses greedy approach to maximize the skill for the team of robots where the problem was that it included a fraction of a particular robot to completely use the budget, but we require a complete unit of a robot or none at all. First, we thought of using the best first greedy search using the skill/cost ratio to solve the problem, where the maximum skill/cost ratio will be considered first, but it won’t give the optimal solution. Since this is an optimization problem similar to 0/1 knapsack, Dynamic Programming was considered but since the problem consists of floating point skill and cost values, it won't work. Therefore the idea to use DP was dropped. Thus, decision to use a normal blind search (DFS) was made.  
•	The design implementation involves creation of a fringe data structure which contains all the valid nodes (i.e. teams), and a successor function called ‘SUCC()’ which generates valid child nodes of each node in the fringe. We have maintained a list of visited nodes to avoid same set of teams in the fringe which reduces the search space. A team/node is sorted before pushing into the visited node and when a particular node  is checked for being visted, that node/team is first sorted and then compared. We have also applied constraint to check that the cost of the team is not greater than the given budget. Apart from that we’ve also maintained maximum cost (cost_o) and skill (skill_o). Total cost and skill of each node was calculated, and if it’s greater than maximum values we update the cost_o and the skill_o else the particular node is ignored. Thus, this way finally in the end we get a team with maximum skill within a given budget.  
