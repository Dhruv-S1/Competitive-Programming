import heapq
import sys
n, m = map(int, sys.stdin.readline().split())
d = {}
for i in xrange(1, n+1):
    d[i] = []
for i in xrange(m):
    num1, num2, num3 = map(int, sys.stdin.readline().split())
    d[num1].append((num2, num3))
    d[num2].append((num1, num3))
dist = [0]
for i in range(n):
    dist.append(9999999999)
dist[1] = 0
h = []
vis = set()
vis.add(1)
curnode = 1
while True:
    for i in range(len(d[curnode])):
        if d[curnode][i][0] not in vis:
            if dist[curnode]+d[curnode][i][1]<dist[d[curnode][i][0]]:
                dist[d[curnode][i][0]] = dist[curnode]+d[curnode][i][1]
                heapq.heappush(h, (dist[d[curnode][i][0]], d[curnode][i][0]))
    if len(vis) == n or len(h) == 0:
        break
    curnode = heapq.heappop(h)[1]
    vis.add(curnode)
for i in xrange(1, len(dist)):
    if dist[i] == 9999999999:
        print -1
    else:
        print dist[i]
