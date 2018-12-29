import sys
n, q = map(int, raw_input().split())
temp = []
temp = map(int, sys.stdin.readline().split())
maxesleft = []
maxesright = []
frequencyleft = []
frequencyright = []
frequencyleft.append(0)
frequencyright.append(0)
currentmax = 0
count = 0
maxesleft.append(0)
maxesright.append(0)
for i in range(n):
    if temp[i]>currentmax:
        currentmax = temp[i]
        count = 1
        frequencyleft.append(count)
        maxesleft.append(temp[i])
    elif temp[i]<currentmax:
        maxesleft.append(currentmax)
        frequencyleft.append(count)
    elif temp[i] == currentmax:
        count = count+1
        frequencyleft.append(count)
        maxesleft.append(temp[i])
currentmax = 0
count = 0
for i in range(n-1, -1, -1):
    if temp[i]>currentmax:
        currentmax = temp[i]
        maxesright.append(temp[i])
        count = 1
        frequencyright.append(count)
    elif temp[i]<currentmax:
        maxesright.append(currentmax)
        frequencyright.append(count)
    elif temp[i] == currentmax:
        count = count+1
        frequencyright.append(count)
        maxesright.append(temp[i])
    
maxesright.append(0)
frequencyright.append(0)
maxesright.reverse()
frequencyright.reverse()
maxesleft.append(0)
frequencyleft.append(0)


for j in xrange(q):
    a, b = map(int, sys.stdin.readline().split())
    print(max(maxesleft[a-1], maxesright[b+1])),
    if a!= 1 and maxesleft[a-1] == maxesright[b+1]:
        print(frequencyleft[a-1]+frequencyright[b+1])
    else:
        if a != 1 and maxesleft[a-1]>maxesright[b+1]:
            print(frequencyleft[a-1])
        else:
            print(frequencyright[b+1])
