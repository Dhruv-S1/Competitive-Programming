x = input()
a = []
b = set(a)
tot = 0
for i in range(x):
  a.append(input())
  
pos = []
neg = []
for i in range(len(a)):
  if a[i] != 0:
    if a[i]>0:
      pos.append(a[i])
    else:
      neg.append(a[i])
    
if len(pos) ==0 and len(neg) == 0:
  print(0)
else:
  pos.sort()
  neg.sort()
  tot = 1
  for j in range(len(pos)):
    tot = tot*pos[j]
  if len(neg)%2 == 1:
    g = len(neg)-1
  else:
    g = len(neg)
  for j in range(g):
    tot = tot*neg[j]
  
  if len(pos) == 0 and 0 in a and len(neg)%2 ==1:
    print(0)
  elif len(pos) == 0 and len(a) == 1:
    print neg[0]
  else:
    print(tot)
