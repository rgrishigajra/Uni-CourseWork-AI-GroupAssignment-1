#!/usr/local/bin/python3
#
# choose_team.py : Choose a team of maximum skill under a fixed budget
#
# Code by: michheta rgajra jaymadhu :Milan Chheta, Rishabh Gajra, Jay Madhu#
# Based on skeleton code by D. Crandall, September 2019
#
import sys

def load_people(filename):
    people={}
    with open(filename, "r") as file:
        for line in file:
            l = line.split()
            people[l[0]] = [ float(i) for i in l[1:] ]
    return people


# This function implements a greedy solution to the problem:
#  It adds people in decreasing order of "skill per dollar,"
#  until the budget is exhausted. It exactly exhausts the budget
#  by adding a fraction of the last person.
#
def succ(people,person,budget):
    # print('name:',name)
    cost=0
    r = person
    s=[]
    for i in person:
        cost=cost+(people.get(i)[1])
    balance=budget-cost
    for (person_next, (skill_next, cost_next)) in people.items():
        b = balance
        if (b-cost_next>0) and person_next not in person:
            b=b-cost_next
            s+=[r+ [person_next,],]
    print(s)
    return s



def nodes(people, budget):
    fringe=[[person] for (person, (skill, cost)) in sorted(people.items(), reverse=True, key=lambda x: x[1][0]/x[1][1])]
    skill_o = 0
    cost_o = 0
    while len(fringe)>0:
        person=fringe.pop()
        cost = 0
        skill = 0
        print(person,skill_o)
        for i in person:
                cost = cost + (people.get(i)[1])
                skill = skill + (people.get(i)[0])
        if skill>skill_o and budget-cost>=0:
                o=person
                skill_o=skill
                cost_o=cost
        for suc in succ(people,person,budget):
            fringe.append(suc)

    return(o,skill_o,cost_o)


if __name__== "__main__":
    if(len(sys.argv) != 3):
        raise Exception('Error: expected 2 command line arguments')

    budget = float(sys.argv[2])
    people = load_people(sys.argv[1])
    people,cost,skill=nodes(people, budget)
    # solution = approx_solve(people, budget)
    print("Found a group with %d people costing %f with total skill %f" % \
               ( len(people), cost, skill))
    d=float(1)
    for s in people:
        print("%s %f" % (s,d))

