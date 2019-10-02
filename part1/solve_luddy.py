#!/usr/local/bin/python3
# solve_luddy.py : Sliding tile puzzle solver
#
# Code by: [PLEASE PUT YOUR NAMES AND USER IDS HERE]
#
# Based on skeleton code by D. Crandall, September 2019
#
from queue import PriorityQueue
import sys

MOVES = { "R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1,0) }
MOVES_luddy = { "A": (2, 1),"B": (2, -1),"C": (-2, 1),"D": (-2, -1),"E": (1, 2),"G": (-1, 2),"F": (1, -2),"H": (-1, -2)}


def rowcol2ind(row, col):
    if(row==-1):
        row=3
    if (row == 4):
        row = 0
    if (col == -1):
        col = 3
    if (col == 4):
        col = 0
    return row*4 + col

def ind2rowcol(ind):
    return (int(ind/4), ind % 4)

def valid_index(row, col):
    return 0 <= row <= 3 and 0 <= col <= 3

def swap_ind(list, ind1, ind2):
    return list[0:ind1] + (list[ind2],) + list[ind1+1:ind2] + (list[ind1],) + list[ind2+1:]

def swap_tiles(state, row1, col1, row2, col2):
    return swap_ind(state, *(sorted((rowcol2ind(row1,col1), rowcol2ind(row2,col2)))))

def printable_board(row):
    return [ '%3d %3d %3d %3d'  % (row[j:(j+4)]) for j in range(0, 16, 4) ]

# return a list of possible successor states
def successors(state):
    (empty_row, empty_col) = ind2rowcol(state.index(0))
    if(sys.argv[2]=="Original" or sys.argv[2]=="original"):
        return [ (swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c) \
                 for (c, (i, j)) in MOVES.items() if valid_index(empty_row+i, empty_col+j) ]
    elif(sys.argv[2]=="Luddy" or sys.argv[2]=="luddy"):
        return [ (swap_tiles(state, empty_row, empty_col, empty_row+i, empty_col+j), c) \
                 for (c, (i, j)) in MOVES_luddy.items() if valid_index(empty_row+i, empty_col+j) ]
    elif(sys.argv[2] == "Circular" or sys.argv[2]=="circular"):
        return [(swap_tiles(state, empty_row, empty_col, empty_row + i, empty_col + j), c) \
                for (c, (i, j)) in MOVES.items()]
# check if we've reached the goal
def is_goal(state):
    return sorted(state[:-1]) == list(state[:-1]) and state[-1]==0

def heuristic_a(state):
    c=0
    for i in range(0,len(state)):
        if state[i]!=i+1 and state[i]!=0 :
            c=c+1
    return c



# The solver! - using BFS right nowol,m
def solve(initial_board):
    count=0
    h_a=heuristic_a(initial_board)
    fringe = [ (initial_board, "" ) ]
    visited=[]
    hlist=[h_a]

    while len(fringe) > 0:
        (state, route_so_far)= fringe.pop(hlist.index(min(hlist)))
        hlist.pop(hlist.index(min(hlist)))
        print(state,route_so_far)
        if state in visited:
            continue
        visited.append(state)
        count = count + 1
        if is_goal(state):
            print(count)
            return (route_so_far)
        for (succ, move) in successors( state ):
            h_a = heuristic_a(succ)
            fringe.insert(0, (succ, route_so_far + move ))
            hlist.insert(0,h_a+len(route_so_far)+1)
    return False
def valid_board(start_state):
    c=0
    for i in range(0,16):
        for j in range(i,16):
            if start_state[j]<start_state[i] and start_state[i]!=0 and start_state[j]!=0:
                c=c+1
    (row, col) = ind2rowcol(start_state.index(0))
    c=c+row+1
    return c



# test cases
if __name__ == "__main__":
    if(len(sys.argv) != 3):
        raise(Exception("Error: expected 2 arguments"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != 16:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))
    print("Solving...")
    N= valid_board(tuple(start_state))
    if(N % 2==0 and sys.argv[2]=="original"):
        route = solve(tuple(start_state))
        print("Solution found in " + str(len(route)) + " moves:" + "\n" + route)
    else:
        print('Inf')

