import sys
import heapq
v = input()
e = input()
d = {}
g = []
for i in range(1, v+1):
    d[i] = [99999, 0]

temp = []
for i in range(v+1):
    temp.append(0)
g.append(temp)
for i in range(v+1):
    temp = []
    for j in xrange(v+1):
        temp.append(0)
    g.append(temp)





for i in xrange(e):
    num1, num2, num3, num4 = map(int, sys.stdin.readline().split())
    if g[num1][num2] != 0:
        g[num1][num2] = min(g[num1][num2], float(num3)/float(num4))
        g[num2][num1] = min(g[num1][num2], float(num3)/float(num4))
    else:
        g[num1][num2] = float(num3)/float(num4)
        g[num2][num1] = float(num3)/float(num4)
        


vis = set()
vis.add(1)
current = 1
d[current][0] = 0
heap = []
while True:
    for i in range(1, len(g[current])):
        if i not in vis and g[current][i]!=0:
            if d[i][0] == g[current][i]+d[current][0]:
                d[i][1] = min(d[i][1], d[current][1]+1)
                heapq.heappush(heap ,(d[i][0], i))
            elif d[i][0]>g[current][i]+d[current][0]:
                d[i][0] = g[current][i]+d[current][0]
                d[i][1] = d[current][1]+1
                heapq.heappush(heap ,(d[i][0], i))
    if len(heap) == 0:
        break
    a = heapq.heappop(heap)
    vis.add(a[1])
    current = a[1]

delay = 0
d[v][0] = d[v][0]*60
delay = (float(4.0*d[v][0])/3.0)

print(d[v][1])
print(int(round(delay-d[v][0])))
