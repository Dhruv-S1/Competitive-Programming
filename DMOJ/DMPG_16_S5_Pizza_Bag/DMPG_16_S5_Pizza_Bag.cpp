import sys
from collections import deque
def main():
    n, k = map(int, sys.stdin.readline().split())
    a = []
    a = map(int, sys.stdin.readline().split())
    a = a + a
    for i in xrange(1, len(a)):
        a[i] = a[i-1] + a[i]
    d = deque()
    for i in xrange(k):
        while len(d)!= 0 and a[i]<=a[d[0]]:
            d.popleft()
        d.appendleft(i)
    max1 = a[k-1] - a[d[len(d)-1]]
    
    for i in xrange(k, len(a)):
        while len(d)!=0 and d[len(d)-1]<=i-k-1:
            d.pop()
        while len(d)!= 0 and a[i]<=a[d[0]]:
            d.popleft()
        if len(d)!=0 and a[i] -  a[d[len(d)-1]]>max1:
            max1 = a[i] -  a[d[len(d)-1]]
        d.appendleft(i)
        
    print max1
main()
