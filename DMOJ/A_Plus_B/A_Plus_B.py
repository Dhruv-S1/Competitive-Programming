import sys
x = input()
for i in xrange(x):
    num1, num2 = map(int, sys.stdin.readline().split())
    print num1+num2
