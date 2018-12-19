import sys
import heapq

k, n, m = map(int, raw_input().split())
d = []
d = [[999999999999 for j in range(k+1)]for i in xrange(n+1)]
a = []
a = [[] for i in range(n+1)]
for i in xrange(m):
    num, num1, num2, num3 = map(int, sys.stdin.readline().split())
    a[num].append((num1, num2, num3))
    a[num1].append((num, num2, num3))
start, dest = map(int, raw_input().split())
for i in range(k+1):
    d[start][i] = 0
vis = []
for i in xrange(n+1):
    vis.append(False)
q = [start]
while q:
    current = q.pop(0)
    vis[current] = False
    for v in a[current]:
        for i in xrange(k-v[2]+1):
            if d[current][i]+v[1]<d[v[0]][i+v[2]]:
                d[v[0]][i+v[2]] = d[current][i]+v[1]
                if not vis[v[0]]:
                    vis[v[0]] = True
                    q.append(v[0])
min1 = 999999999999
for i in range(k):
    if d[dest][i]<min1:
        min1 = d[dest][i]
if min1 == 999999999999:
    print(-1)
else:
    print(min1)
