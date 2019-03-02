import sys
x = input()
count = 0
a = [0]
for i in xrange(x):
    count+= int(sys.stdin.readline())
    a.append(count)
y = input()
for i in xrange(y):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(a[num2+1]-a[num1])
