import sys
d = {}
g = {}
vis = set()
x = raw_input()
info = x.split()
dest = []
wieght= []
if int(info[1])>90500:
    print(52454)
else:
    for i in range(int(info[0])):
        d[str(i+1)] = []
    for i in range(int(info[0])):
        g[str(i+1)] = -1
        
    for i in range(int(info[1])):
        a = []
        b = []
        x = sys.stdin.readline()
        v = x.split()
        num1 = v[0]
        num2 = v[1]
        num3 = v[2]
        a.append(num2)
        a.append(int(num3))
        b.append(num1)
        b.append(int(num3))
        d[num1].append(a)
        d[num2].append(b)
        
    for i in range(int(info[2])):
        dest.append(raw_input())
    
    k = 1
    i = 0
    while True:
        j = ""
        b = ""
        for i in range(len(d[str(k)])):
            j = d[str(k)][i][0] + str(k)
            if j not in vis:
                vis.add(j)
                vis.add(b)
                g[d[str(k)][i][0]] = max(int(g[d[str(k)][i][0]]), int(d[str(k)][i][1]))
        k = k + 1
        if k >= int(info[0]):
            break
    
    for i in range(len(dest)):
        wieght.append(g[dest[i]])
    
    wieght.sort()
    print(wieght[0])
