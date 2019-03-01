global x
import sys
# NOTE: This is a partial solution and only yields 8/15 points 

sys.setrecursionlimit(1000000000)
x = input()
a = []
for i in xrange(x):
    temp = []
    temp = map(int, raw_input().split())
    a.append(temp)

a.sort()
start = 0
for i in xrange(len(a)):
    a[i].append(i)
    if a[i][0] == 0:
        start = i
        
taken = set()
temp = []
def findright(current):
    for i in xrange(current, len(a)):
        if a[i][2] not in taken:
            return a[i]
    return 0
def findleft(current):
    for i in xrange(current, -1, -1):
        if a[i][2] not in taken:
            return a[i]
    return 0
finalvalues = []

def recurse(current, energy, totaldistance, pos):
    taken.add(current)
    if energy<0:
        finalvalues.append(totaldistance-a[current][1])
        taken.remove(current)
        return
    energy+=a[current][1]
    if len(taken) == x:
        finalvalues.append(totaldistance)
        taken.remove(current)
        return
    temp = findright(current)
    marker = 0
    if temp!=0:
        if energy-(abs(temp[0]-pos))>=0:
            recurse(temp[2], energy-(abs(temp[0]-pos)), totaldistance+temp[1], temp[0])
        else:
            marker = 1
    else:
        marker = 1
    temp = findleft(current)
    marker1 = 0
    if temp!=0:
        if energy-(abs(temp[0]-pos))>=0:
            recurse(temp[2], energy-(abs(temp[0]-pos)), totaldistance+temp[1], temp[0])
        else:
            marker1 = 1
    else:
        marker1 = 1
    if marker1 == 1 and marker == 1:
        finalvalues.append(totaldistance)
        taken.remove(current)
        return
    taken.remove(current)
taken.add(start)     
recurse(start, 0, a[start][1], 0)
finalvalues.sort()
print finalvalues[len(finalvalues)-1]
