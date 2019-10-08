#!/usr/local/bin/python3

# put your routing program here!
import sys
# test cases

def successors(city,miles, gas, hours,segments,hway,d):
  c_city=city[-1]
  #print(c_city,city)
  s=[]
  succ=[]
  count = 0
  h=[]

  for i in d[c_city].keys():
    s=city+[i,]
    hway += ","
    hway += d[c_city][i]['hway']
    miles += int(d[c_city][i]['miles'])
    hours += (float(d[c_city][i]['miles']) / float(d[c_city][i]['speed']))
    h=[s,(miles + int(d[c_city][i]['miles'])),hours + (float(d[c_city][i]['miles']) / float(d[c_city][i]['speed'])),(hway + d[c_city][i]['hway'])]
    succ = succ +[h,]
    #print(succ)


  #print([succ,hway,miles,hours])
  #print("\n")
  #print(s)
  return succ


def solve(start_city, end_city, cost_function,d ):
  oye="oye"
  miles=0
  visited=[]
  hours=0
  gas=0
  segments=0
  hway=""
  city=[start_city, ]
  fringe=[(city, miles, hours, gas, segments, hway)]
  visited.append(start_city)
  while len(fringe)>0:
    (city,miles, hours, gas, segments, hway) = fringe.pop(0)
    #succ=successors(city, miles, hours, segments, hway, d)
    #[succ1,miles,hours,segments,hway]=successors(city, miles, hours, segments, hway, d)
    #print(succ1)
    for succ in successors(city, miles, hours, gas, segments, hway, d):
      if succ[0][-1] == end_city:
        print(succ[0],succ[1],succ[2],gas,segments+1,succ[3])
        print('done')
        return ''
      if succ[0][-1] not in visited:
        fringe.append([succ[0],succ[1],succ[2],gas,segments+1,succ[3]])
        visited.append(succ[0][-1])

  return ''





if __name__ == "__main__":

  start_city=sys.argv[1]
  end_city=sys.argv[2]
  cost_function=sys.argv[3]
  # print(start_city,end_city,cost_function)
  d = {}
  with open("road-segments.txt") as f:
    for line in f:
      (city1,city2, miles, speed, hway) = line.split()
      if city1 in d.keys():
        d[city1][city2]={'miles':miles,'speed': speed,'hway': hway}
      else :
        d[city1]={city2:{'miles':miles, 'speed':speed, 'hway':hway}}
      if city2 in d.keys():
        d[city2][city1]={'miles':miles,'speed': speed,'hway': hway}
      else :
        d[city2]={city1:{'miles':miles, 'speed':speed, 'hway':hway}}

  solve(start_city, end_city,cost_function,d)








  # for i in d:
  #   print(i)
  #   print(d[i])
  #   count += 1
  #   if count == 2:
  #     break
