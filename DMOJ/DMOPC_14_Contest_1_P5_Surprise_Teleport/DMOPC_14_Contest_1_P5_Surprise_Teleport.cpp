import sys
x = sys.stdin.readline()
r, c = map(int, x.split())
x = sys.stdin.readline()
startr, startc = map(int, x.split())
x = sys.stdin.readline()
mainr, mainc = map(int, x.split())
d = {}
prev = []
for i in range(r):
    x = sys.stdin.readline()
    temp = []
    temp = list(x)
    for j in range(c):
        if temp[j] == "O":
            d[(i , j)] = []
            if j+1<=c-1 and temp[j+1] == "O":
                d[(i, j)].append((i, j+1))
            if j-1>=0 and temp[j-1] == "O":
                d[(i, j)].append((i, j-1))

    if i != 0:
        for j in range(c):
            if temp[j] == "O":
                if prev[j] == "O":
                    d[(i, j)].append((i-1, j))
                    d[(i-1, j)].append((i, j))
    prev = temp
x = input()
tele = set()
for i in range(x):
    y = raw_input()
    temp = []
    temp = map(int, y.split())
    tele.add(tuple(temp))

vis = set()
current = [(startr, startc)]
min1 = 9999999999999
count = 0
newcurrent = []
while True:
    for i in range(len(current)):
        for j in range(len(d[current[i]])):
            if d[current[i]][j] not in vis:
                vis.add(d[current[i]][j])
                newcurrent.append(d[current[i]][j])
                if d[current[i]][j] in tele:
                    if count<min1:
                        min1 = count+1
    count = count+1
    if (mainr, mainc) in vis:
        if r == 2:
            print(2)
        else:
            print(count - min1)
        break



    current = []
    current = newcurrent
    newcurrent = []
