a = []
for i in xrange(10000001):
    a.append(0)
b = []
for i in xrange(10000001):
    b.append(False)
i = 2
while i<=10000000:
    if not b[i]:
        for j in range(0, 10000001, i):
            a[j]+=1
            b[j] = True

    i +=1
a[0] = 0
x = input()

for j in xrange(x):
    num1, num2, num3 = map(int, raw_input().split())
    if num3>8:
        print 0
    else:
        count = 0
        for k in xrange(num1, num2+1):
            if a[k] == num3:
                count +=1
        print "Case #%d: %d" % ((j+1), count)
