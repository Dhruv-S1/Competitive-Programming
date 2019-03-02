import sys
x = input()
a = []
d = {}
max1 = 0
currentmax = 0
freq = []
freq1 = []
vis = []
for i in range(x):
    y = int(sys.stdin.readline())
    a.append(y)
    d[y] = 0

for i in range(x):
    d[a[i]] += 1
for i in range(x):
    if d[a[i]]>=max1 and a[i] not in vis:
        max1 =  d[a[i]]
        vis.append(a[i])
vis = []
for i in range(len(a)):
    if d[a[i]] == max1 and a[i] not in vis:
        freq.append(a[i])
        vis.append(a[i])
vis = []
max1 = 0
for i in range(x):
    if a[i] not in freq:
        if d[a[i]]>=max1 and a[i] not in vis:
            max1 = d[a[i]]
            vis.append(a[i])
vis = []
for i in range(len(a)):
    if d[a[i]] == max1:
        freq1.append(a[i])
        vis.append(a[i])



max1 = 0


if len(freq) > 1:
    freq.sort()
    print(abs(freq[0] - freq[len(freq) - 1]))
else:
    if len(freq1)>1:
        for i in range(len(freq1)):
            if abs(freq[0] - freq1[i])> max1:
                max1 = abs(freq[0] - freq1[i])
        
        print(max1)
    else:
        print(abs(freq[0] - freq1[0]))
