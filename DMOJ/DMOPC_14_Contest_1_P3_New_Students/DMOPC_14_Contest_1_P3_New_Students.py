import sys
x = input()
count = 0
for i in xrange(x):
    count+= int(sys.stdin.readline())
y = input()
for i in xrange(y):
    count+=int(sys.stdin.readline())
    print(round((float(count)/(x+(i+1))), 3))
