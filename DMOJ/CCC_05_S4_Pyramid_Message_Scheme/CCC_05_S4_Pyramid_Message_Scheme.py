x = input()
for j in range(x):
    y = input()
    d = {}
    b = []
    newnodes = []
    curnodes = []
    vis = set()
    count = 0
    for i in range(y):
        b.append(raw_input())
    for i in range(y):
        d[b[i]] = []
    for i in range(y):
        if i==0:
            d[b[len(b)-1]].append(b[0])    
        if i!=y-1:
            d[b[i]].append(b[i+1])
    curnodes.append(b[len(b)-1])
    vis.add(b[len(b)-1])
    while True:
        for i in range(len(curnodes)):
            for j in range(len(d[curnodes[i]])):
                if d[curnodes[i]][j] not in vis:
                    newnodes.append(d[curnodes[i]][j])
                    vis.add(d[curnodes[i]][j])
        count = count+10
        curnodes = []
        curnodes = newnodes
        newnodes = []
        if len(vis) == len(d):
            break
    print((y*10)-(count*2))
