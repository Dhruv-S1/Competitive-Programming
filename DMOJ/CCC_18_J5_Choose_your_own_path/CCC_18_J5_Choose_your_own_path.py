import sys
x = input()
d = {}

for i in range(x+1):
  d[i]= []
for i in range(1, x+1):
  d[i] = map(int, raw_input().split())
  if len(d[i])>1:
    d[i].pop(0)
vis = set()
minval = 99999999;
cur = [1]
new = []
count = 0
vis.add(1)
while True:
  for i in range(len(cur)):
    for j in range(len(d[cur[i]])):
      if d[cur[i]][j] not in vis:
        if d[cur[i]][j] != 0:
          vis.add(d[cur[i]][j])
          new.append(d[cur[i]][j])
        if d[cur[i]][j] == 0:
          if count<minval:
            minval = count
            
  if len(new) == 0:
    if minval!=99999999 and len(vis) == x:
      print "Y"
      print minval+1
      break
    else:
      print "N"
      print minval+1
      break
  cur = []
  cur = new
  new = []
  count+=1
