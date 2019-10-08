#!/usr/local/bin/python3

# put your routing program here!
import sys
# test cases

def successors(city,miles, hours, gas,hway, d):
  c_city=city[-1]
  s=[]
  succ=[]
  count = 0
  h=[]
  vel=0
  for i in d[c_city].keys():
    s=city+[i,]
    #print("miles,speed,time")
    #print((float(d[c_city][i]['miles']), float(d[c_city][i]['speed'])),(float(d[c_city][i]['miles']) / float(d[c_city][i]['speed'])))
    vel=((miles + int(d[c_city][i]['miles']))/(hours + (float(d[c_city][i]['miles']) / float(d[c_city][i]['speed']))))
    mvg=400*(vel/150)*((1-vel/150)**4)
    h=[s,(miles + int(d[c_city][i]['miles'])),hours + (float(d[c_city][i]['miles']) / float(d[c_city][i]['speed'])), (hway +", " +d[c_city][i]['hway']),mvg,((miles + int(d[c_city][i]['miles']))/mvg)]
    succ = succ +[h,]
  #print(succ)


  #print([succ,hway,miles,hours])
  #print("\n")
  #print(s)
  return succ


def solve(start_city, end_city, cost_function,d ):
  oye="oye"
  miles=0
  mvg=0
  visited=[]
  hours=0.00
  gas=0
  segments=0
  index=0
  hway=""
  path=""
  city=[start_city, ]
  fringe=[(city, miles, hours, gas, segments, hway, mvg)]
  visited.append(start_city)
  while len(fringe)>0:
    if(sys.argv[3]=="segments"):
      index=0
    if(sys.argv[3]=="distance"):
      index=fringe.index(min(fringe, key=lambda x: x[1]))
    if(sys.argv[3]=="time"):
      index=fringe.index(min(fringe, key=lambda x: x[2]))
    if(sys.argv[3]=="mpg"):
      index=fringe.index(min(fringe, key=lambda x: x[2]))
    (city,miles, hours, gas, segments, hway, mvg) = fringe.pop(index)
    for succ in successors(city, miles, hours, gas, hway, d):
      if succ[0][-1] == end_city:
        for i in succ[0]:
          path+=i
          path+=" "
        print(segments+1,succ[1],succ[2],succ[5],path)
        return ''
      if succ[0][-1] not in visited:
        fringe.append([succ[0],succ[1],succ[2],succ[5],segments+1,succ[3],succ[4]])
        visited.append(succ[0][-1])

  print()
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
