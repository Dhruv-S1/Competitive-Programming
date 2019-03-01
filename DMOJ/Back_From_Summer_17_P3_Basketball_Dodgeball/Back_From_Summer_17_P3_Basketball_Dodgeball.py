from math import sqrt
n, m = map(int, raw_input().split())
a = []
b = []
max1 = 0
place = 0
for i in range(n):
    temp = map(int, raw_input().split())
    temp.append(i)
    if temp[1] > max1:
        place = i
        max1 = temp[1]
    a.append(temp)


max2 = 0
place2 = 0
for i in range(m):
    temp = map(int, raw_input().split())
    temp.append(i)
    if temp[1] >max2:
        place2 = i
        max2 = temp[1]
    b.append(temp)

current = [a[place]]
newarray = []
marker = 0
count = 0
vis = set()
vis.add(a[place][3])
while True:
    for i in range(len(current)):
        for j in range(len(a)):
            if a[j][3] not in vis:
                if sqrt((a[j][0]-current[i][0])**2 + (a[j][1] - current[i][1])**2)<=current[i][2]:
                    if a[j][2] == 9001:
                        marker = 1
                        break
                    vis.add(a[j][3])
                    newarray.append(a[j])
        if marker == 1:
            break
    if marker == 1 or len(newarray) == 0:
        break
    else:
        count+=1
    current = []
    current = newarray
    newarray = []
if marker == 1:
    count+=1




current = [b[place2]]
newarray = []
marker = 0
count1 = 0
vis.clear()
vis.add(b[place2][3])
while True:
    for i in range(len(current)):
        for j in range(len(b)):
            if b[j][3] not in vis:
                if sqrt((b[j][0]-current[i][0])**2 + (b[j][1] - current[i][1])**2)<=current[i][2]:
                    if b[j][2] == 9001:
                        marker = 1
                        break
                    vis.add(b[j][3])
                    newarray.append(b[j])
        if marker == 1:
            break
    if marker == 1 or len(newarray) == 0:
        break
    else:
        count1+=1
    current = []
    current = newarray
    newarray = []
if marker == 1:
    count1+=1
if count == 0 and count1>0:
    print ":'("
elif count>0 and count1 == 0:
    print ":'("
elif count<count1:
    print "We are the champions!"
elif count>count1:
    print":'("
else:
    print "SUDDEN DEATH"
