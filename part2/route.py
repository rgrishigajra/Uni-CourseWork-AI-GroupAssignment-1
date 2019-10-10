#!/usr/local/bin/python3
#
# Code by: michheta rgajra jaymadhu :Milan Chheta, Rishabh Gajra, Jay Madhu
# put your routing program here!
import sys
# test cases

def successors(city,miles, hours, gas, hway, d):
  c_city=city[-1]
  s=[]
  succ=[]
  vel=0
  for i in d[c_city].keys():
    s=city+[i,]
    vel=((miles + int(d[c_city][i]['miles']))/(hours+ (float(d[c_city][i]['miles']) / float(d[c_city][i]['speed']))))
    mpg=400*(vel/150)*((1-(vel/150))**4)
    #the structure of return is cities travelled[0], total miles[1], total hours[2], list of high ways[3], hway path[4], mpg[5] and gas gallons[6]
    h=[s,(miles + int(d[c_city][i]['miles'])),hours + (float(d[c_city][i]['miles']) / float(d[c_city][i]['speed'])), (hway +" " +d[c_city][i]['hway']),mpg,((miles + float(d[c_city][i]['miles']))/mpg)]
    succ = succ +[h,]
  #print(succ)


  #print([succ,hway,miles,hours])
  #print("\n")
  #print(s)
  return succ


def solve(start_city, end_city, cost_function,d ):
  miles=0
  mpg=0
  visited=[]
  hours=0.00
  gas=0
  segments=0
  index=0
  hway=""
  cities=""
  path=""
  city=[start_city, ]
  fringe=[(city, miles, hours, gas, segments, hway, mpg)]
  visited.append(start_city)
  while len(fringe) > 0:
    if(sys.argv[3]=="segments"):
      index=0
    if(sys.argv[3]=="distance"):
      index=fringe.index(min(fringe, key=lambda x: x[1]))
    if(sys.argv[3]=="time"):
      index=fringe.index(min(fringe, key=lambda x: x[2]))
    if(sys.argv[3]=="mpg"):
      index=fringe.index(min(fringe, key=lambda x: x[6]))
    (city,miles, hours, gas, segments, hway, mpg) = fringe.pop(index)
    for succ in successors(city, miles, hours, gas, hway, d):
      if succ[0][-1] == end_city:
        #print(d[succ[0][-2]][end_city]['hway']) d[current successor][end city][highway for it]
        hway+=" "
        hway+= d[succ[0][-2]][end_city]['hway']
        path= hway.split()
        for i in succ[0]:
          cities+=i
          cities+=" "
        print("For going from "+str(start_city).replace('_', ' ')+" to " + str(end_city).replace('_', ' ') + " take the following route:\n")
        for i in range(0,(len(succ[0])-1)):
          print("Go from " +str(succ[0][i]).replace('_', ' ') + " to " +str(succ[0][i+1]).replace('_', ' ')+ " using Highway " + path[i].replace('_', ' '))
        print("\nPlease maintain an avg speed of " +str(round(succ[1]/succ[2],2))+ ", it should take you around "+ str(round(succ[2],2))+ " hours on this trip.\nHave a safe journey!")
        print(segments+1, succ[1], succ[2], succ[5], cities) #[total-segments] [total-miles] [total-hours] [total-gas-gallons] [start-city] [city-1] [city-2] ... [end-city]
        return ''
      if succ[0][-1] not in visited:
        fringe.append([succ[0], succ[1], succ[2], succ[5], segments+1, succ[3], succ[4]]) #(city,miles, hours, gas, segments, hway, mpg)
        visited.append(succ[0][-1])

  print("Inf")
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
