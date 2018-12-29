import sys
x = input()
a = set()
for i in xrange(x):
    marker = 0
    temp = map(int, sys.stdin.readline().split())
    temp.sort()
    if tuple(temp) in a:
        print "Twin snowflakes found."
        sys.exit()
    a.add(tuple(temp))

print "No two snowflakes are alike."
