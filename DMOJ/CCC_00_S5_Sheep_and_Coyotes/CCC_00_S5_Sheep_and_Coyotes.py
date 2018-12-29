from math import sqrt
import sys
a = []
x = input()
for i in range(x):
    temp = []
    temp.append(float(sys.stdin.readline()))
    temp.append(float(sys.stdin.readline()))
    a.append(temp)

i = float()
c = set()
while True:
    min1 = 99999
    currentshort = 0
    for j in range(len(a)):
        if sqrt(((a[j][0]-i)**2+(a[j][1])**2)) < min1:
            currentshort = a[j]
            min1 = sqrt(((a[j][0]-i)**2+(a[j][1])**2))
    if currentshort != [] and tuple(currentshort) not in c:
        print("The sheep at (%.2f, %.2f) might be eaten.") % (round(currentshort[0], 2), round(currentshort[1], 2))
        c.add(tuple(currentshort))
    i = i+ 0.01
    if i > 300:
        break
