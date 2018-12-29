x = input()
y = input()
global counter1
counter1 = 0
a = []
for i in range(x+1):
    temp = []
    for j in xrange(y+1):
        temp.append(0)
    a.append(temp)

def pie(n,m):
    if n>m:
        return 0
    if n == 1:
        return 1
    if a[m][n] != 0:
        return a[m][n]
    a[m][n] = pie(n-1, m-1) + pie(n, m-n)
    return a[m][n]

pie(y, x)
if a[x][y] == 0:
    print 1
else:
    print a[x][y]
