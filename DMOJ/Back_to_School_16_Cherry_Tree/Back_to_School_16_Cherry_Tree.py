import sys
sys.setrecursionlimit(1000000000)
def wieght(curnode):
    if len(d[curnode]) == 0:
        heavy[curnode-1] = store[curnode]
        return heavy[curnode-1]
    heavy[curnode-1] = store[curnode]
    for i in range(len(d[curnode])):
        heavy[curnode-1] +=  wieght(d[curnode][i])
            
    return heavy[curnode-1]


def cherry(curnode):
    if len(d[curnode]) == 0:
        cherrystore[curnode-1] = cherries[curnode-1]
        return cherrystore[curnode-1]
    cherrystore[curnode-1] = cherries[curnode-1]
    for i in range(len(d[curnode])):
        cherrystore[curnode-1] += cherry(d[curnode][i])

    return cherrystore[curnode-1]
    


x = raw_input()

totcherry, want, maxweight = map(int, x.split())

x = raw_input()

cherries = map(int, x.split())

d = {}

store = {}

for i in range(1, totcherry+1):
    d[i] = []
store[1] = 0
for i in range(totcherry-1):
    x = raw_input()
    num1, num2, num3 = map(int, x.split())
    d[num1].append(num2)
    store[num2] = num3


heavy = []

cherrystore = []

for i in range(totcherry):
    heavy.append(0)
    cherrystore.append(0)
wieght(1)
cherry(1)
count = 0
for i in range(1, totcherry):
    if heavy[i] <= maxweight and cherrystore[i] >=want:
        count = count+1
print(count)
