left = []
right = []
n, b = map(int, raw_input().split())
array = []
array = map(int, raw_input().split())
pos = 0
for i in range(len(array)):
    if array[i] == b:
        pos = i
for i in xrange(100001):
    left.append(0)
    right.append(0)

current = 0
tot = 0
for i in range(pos-1, -1, -1):
    if array[i] < b:
        current = current-1
    else:
        current = current+1
    if current == 0:
        tot +=1
        left[0]+=1
    elif current < 0:
        left[abs(current)] += 1
    elif current > 0:
        left[abs(current)+50000] += 1
current = 0
for i in range(pos+1, n):
    if array[i] < b:
        current = current-1
    else:
        current = current+1
    if current == 0:
        tot +=1
        right[0]+=1
    elif current < 0:
        right[abs(current)] += 1
    elif current > 0:
        right[abs(current)+50000] += 1

for i in xrange(50000):
    if left[i]!=0 and right[i+50000]!=0:
        tot+=right[i+50000]*left[i]
for i in xrange(50000):
    if left[i+50000]!= 0 and right[i]!=0:
        tot+= right[i]*left[i+50000]
tot+= left[0]*right[0]
print(tot+1)
