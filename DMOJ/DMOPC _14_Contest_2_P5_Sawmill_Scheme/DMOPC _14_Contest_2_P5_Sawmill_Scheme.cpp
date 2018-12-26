from collections import OrderedDict
import sys
def main():
    d = {}
    a = []
    OrderedDict(d)
    y = raw_input()
    n, m = map(int, y.split())
    for i in xrange(n+1):
        a.append(0)
        d[i] = []
    for i in xrange(m):
        y = sys.stdin.readline()
        num1, num2 = map(int, y.split())
        d[num1].append(num2)
    a[1] = 1
    for i in xrange(1, n+1):
        if len(d[i]) == 0:
            print(a[i])
            continue
        for j in range(len(d[i])):
            a[d[i][j]] += float(a[i])/float(len(d[i]))
main()
