x = input()
y = input()
d = []
best = []
bestpeople = []
for i in range(y):
    temp = []
    name = raw_input()
    time = input()
    temp.append(name)
    temp.append(time)
    d.append(temp)
best.append(0)
bestpeople.append([])
for i in range(y):
    temp =[]
    best.append(9999999999)
    bestpeople.append(temp)

for i in range(1, y+1):
    cur = []
    cur1 = []
    j = 0
    while True:
        if j>x-1:
            break
        if j+i > len(d):
            break
        cur.append(d[i+j-1][1])
        cur1.append(d[i+j-1][0])
        cur.sort()
        if best[i-1]+cur[len(cur)-1] < best[i+j]:
            bestpeople[i+j] = bestpeople[i-1] + ["$"] + cur1
        best[i+j] = min(best[i-1]+cur[len(cur)-1], best[i+j])
        j = j+1
a = []
print("Total Time: %d") % (best[len(best)-1])
bestpeople[y].append("$")
for i in range(1, len(bestpeople[y])):
    if bestpeople[y][i] == "$":
        print("".join(a))
        a = []
        continue
    a.append(bestpeople[y][i])
    a.append(" ")
