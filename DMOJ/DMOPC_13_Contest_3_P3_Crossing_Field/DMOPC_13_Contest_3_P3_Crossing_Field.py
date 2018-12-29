import sys
n, h = map(int, raw_input().split())
a = []
temp = []
for i in range(n+1):
    temp.append(0)
a.append(temp)
temp = []
for i in range(n):
    temp = (map(int, raw_input().split()))
    temp = [0]+temp
    a.append(temp)
current = [(1, 1)]
new = []
vis = set()
vis.add((1, 1))
prevlen = 0
while True:
    prevlen = len(vis)
    for i in range(len(current)):
        val1 = a[current[i][0]][current[i][1]]
        if current[i][0]+1<=n and abs(a[current[i][0]+1][current[i][1]]-val1)<=h:
            if (current[i][0]+1, current[i][1]) not in vis:
                vis.add((current[i][0]+1, current[i][1]))
                new.append((current[i][0]+1, current[i][1]))
        if current[i][0]-1>=1 and abs(a[current[i][0]-1][current[i][1]]-val1)<=h:
            if (current[i][0]-1, current[i][1]) not in vis:
                vis.add((current[i][0]-1, current[i][1]))
                new.append((current[i][0]-1, current[i][1]))
        if current[i][1]+1<=n and abs(a[current[i][0]][current[i][1]+1]-val1)<=h:
            if (current[i][0], current[i][1]+1) not in vis:
                vis.add((current[i][0], current[i][1]+1))
                new.append((current[i][0], current[i][1]+1))
        if current[i][1]-1>=1 and abs(a[current[i][0]][current[i][1]-1]-val1)<=h:
            if (current[i][0], current[i][1]-1) not in vis:
                vis.add((current[i][0], current[i][1]-1))
                new.append((current[i][0], current[i][1]-1))
    if (n, n) in vis:
        print("yes")
        break
    if prevlen == len(vis):
        print("no")
        break
    current = []
    current = new
    new = []
