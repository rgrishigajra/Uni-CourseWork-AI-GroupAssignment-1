#!/usr/local/bin/python3

# put your routing program here!
import sys
# test cases




if __name__ == "__main__":

  start_city=sys.argv[1]
  end_city=sys.argv[2]
  cost_function=sys.argv[3]
  solve(start_city,end_city)
  print(start_city,end_city,cost_function)


